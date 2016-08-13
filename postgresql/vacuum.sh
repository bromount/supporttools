#!/bin/bash

# This script will automate the maintenance of a PostgreSQL database
# by running the vacuumdb command against a specific set of SFEE
# tables. These sets logically divide the database tables into groups
# based on their volatility. The more volatile a table, the higher
# it's maintenance needs (generall).
#
# ASSUMPTIONS:
# This script assumes it is run as an OS user that can login to the db
# in a trusted fashion. You can accomplish this by editing pg_hba.conf
# (OK) or by creating a .psqlrc file in the user's $HOME (better).
# This script further assumes that it runs on the database server
# itself.
# And finally, this script assumes you have pgstatspack installed and
# running

## SET UP OUR NEEDED VARIABLES:

# Set up a sane path. If you installed PostgreSQL into /opt or something
# then you will need to tweak this
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

# The host where the db is
DBHOST=localhost

# The name of the db to connect to
DBNAME=sfdb

# The user to connect to the db as
DBUSER=sfee

## DEFINE OUR FUNCTIONS

# This function will locate the needed utility on the OS or exit the
# script if the utility can't be found
#
# Call it like: whereis FOO foo
# and if it can 'foo' it will export '$FOO' pointing to it
whereis() {
  test -x $2 && export "$1" = "$2"
  test -x /bin/$2 && export "$1" = "/bin/$2"
  test -x /sbin/$2 && export "$1" = "/sbin/$2"
  test -x /usr/bin/$2 && export "$1" = "/usr/bin/$2"
  test -x /usr/sbin/$2 && export "$1" = "/usr/sbin/$2"
  test -x /usr/local/bin/$2 && export "$1" = "/usr/local/bin/$2"
  test -x /usr/local/sbin/$2 && export "$1" = "/usr/local/sbin/$2"

  # pipe the var passed to this function, that was used to make a var,
  # into sh to test the existing external var
  if [ `echo echo '$'$1'' | /bin/sh` ] ; then
    # we found it
    :
  else
    echo "Could not locate $2"
    exit 1
  fi
}

# this is our 'sql' function that actually uses psql to attach to the 
# database and issue the commands
sql() {
  # Where is psql?
  whereis PSQL psql

  $PSQL -h $DBHOST -d $DBNAME -U $DBUSER -q -t "$*"
}

# this is our 'vacuum' function that actually does the maintenance work
vacuum() {
  sql -c "vacuum ${1}";
  sql -c "analyze ${1}";
}

get_yesterday() {
  whereis DATE date
  YESTERDAY=`$DATE -d yesterday +%Y-%m-%d`
}

## MAIN LOGIC

# Determine the data yesterday
get_yesterday

# Determine the first pgstatspack snapshot for yesterday
STARTSNAP=`sql -c "select min(snapid) from pgstatspack_snap where ts
between '$YESTERDAY 00:00:00' and '$YESTERDAY 23:59:59';"`

# Determine the last pgstatspack snapshot for yesterday
STOPSNAP=`sql -c "select max(snapid) from pgstatspack_snap where ts
between '$YESTERDAY 00:00:00' and '$YESTERDAY 23:59:59';"`

# Based on the requested priority, determine what tables we're going to
# perform maintenance on
case $1 in
  high)
    # Find sed
    whereis SED sed

    # Find sort
    whereis SORT sort

    # Determine our highly volatile tables
    HIGH_UPDATE=`sql -c " SELECT a.table_name as table FROM pgstatspack_tables a, pgstatspack_tables b WHERE a.snapid=$STARTSNAP AND b.snapid=$STOPSNAP AND a.table_name=b.table_name AND b.n_tup_upd >= a.n_tup_upd group by table_updates, a.table_name ORDER BY table_updates DESC limit 10;"`

    HIGH_DELETE=`sql -c " SELECT a.table_name as table FROM pgstatspack_tables a, pgstatspack_tables b WHERE a.snapid=$STARTSNAP AND b.snapid=$STOPSNAP AND a.table_name=b.table_name AND b.n_tup_del >= a.n_tup_del group by table_deletes, a.table_name ORDER BY table_deletes DESC limit 10;"`

    TABLES=`echo $HIGH_UPDATE $HIGH_DELETE| $SED -e 's/ /\n/g' | $SORT -u`
    ;;

  low)
    TALES=`sql -c "select relname from pg_stat_all_tables where (last_vacuum < (current_timestamp - interval '72 hour') and last_autovacuum < (current_timestamp - interval '72 hour')) or (last_vacuum is null and last_autovacuum is null);"`
    ;;

  full)
    # Find the vacuumdb command
    whereis VACUUMDB vacuumdb

    # Perform a full vacumm on the entire db
    $VACUUMDB -h $DBHOST -U $DBUSER -f -v -z $DBNAME
    sql -c "REINDEX DATABASE $DBNAME;"
    exit
    ;;
esac

# And now actually do said maintenance
for table in $TABLES
do
  vacuum $table
done

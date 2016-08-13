#!/bin/sh

#INSTALL_DIR=$1
#
# Make sure user is 'root'.
#
if [ "$UID" != "0" ]
then
    echo
    echo "$0 ERROR : Only user 'root' can run this script.  Exiting."
    exit 1
fi

echo "Enter the Installtion directory Path(Default:/opt/collabnet/teamforge/):"
read INSTALL_DIR
#echo $INSTALL_DIR
#exit 1
if [ "$INSTALL_DIR" == "" ] 
then
    INSTALL_DIR="/opt/collabnet/teamforge"
fi
#:${INSTALL_DIR:="/opt/collabnet/teamforge/"}
echo $INSTALL_DIR
#exit 0
# removing existing result.txt file.
if [ -f "ctf_details.txt" ]
then
 rm ctf_details.txt
fi

#exec 1>/tmp/ctf_details.txt

echo "Collecting Teamforge details"

echo "------------------------------------------------------------------" >> ctf_details.txt
echo "---------------------Team Forge Deatils---------------------------" >> ctf_details.txt
echo "------------------------------------------------------------------" >> ctf_details.txt
echo " " >> ctf_details.txt

CTF_version="$(find $INSTALL_DIR/runtime/conf/runtime-options.conf | xargs grep 'PRODUCT_NAME' | cut -d "=" -f2 | uniq)"

echo "-----------------------------------------------------------------" >> ctf_details.txt
echo "CTF VERSION       :       $CTF_version" >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt
echo " " >> ctf_details.txt
echo "-------------------- Box Details --------------------------------" >> ctf_details.txt
echo "$(grep HOST_ $INSTALL_DIR/runtime/conf/runtime-options.conf)" >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt
echo " " >> ctf_details.txt
echo "-------------------- Java Options -------------------------------" >> ctf_details.txt
echo "$(grep JAVA_OPTS $INSTALL_DIR/runtime/conf/runtime-options.conf)" >> ctf_details.txt
echo " " >> ctf_details.txt

echo "Collecting RAM & Databse details"

echo "-----------------------------------------------------------------" >> ctf_details.txt
echo "-------------------- Disk & RAM ---------------------------------" >> ctf_details.txt
echo "DISK USAGE        :" >> ctf_details.txt
df -h >> ctf_details.txt
echo " " >> ctf_details.txt
echo "RAM		:" >> ctf_details.txt
free >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt

#echo "-----------------------------------------------------------------"
echo "----------------------- DataBase details ------------------------" >> ctf_details.txt
echo "$(grep DATABASE_TYPE $INSTALL_DIR/runtime/conf/runtime-options.conf)" >> ctf_details.txt
echo "$(grep PGSQL_MAX_CONNECTIONS $INSTALL_DIR/runtime/conf/runtime-options.conf)" >> ctf_details.txt
echo "Installation directory: $INSTALL_DIR" >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt

echo " " >> ctf_details.txt

echo "Collecting OS & Add-Ons details"

echo "----------------------- OS details ------------------------------" >> ctf_details.txt
echo " " >> ctf_details.txt
cat /etc/*-release >> ctf_details.txt
echo " " >> ctf_details.txt
uname -a >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt
echo " " >> ctf_details.txt
echo "--------------------Add-Ons--------------------------------------" >> ctf_details.txt
ls -lrt /opt/collabnet/teamforge/add-ons/ >> ctf_details.txt
echo "-----------------------------------------------------------------" >> ctf_details.txt
echo""

echo "Find Your Site details in ctf_details.txt"
echo""

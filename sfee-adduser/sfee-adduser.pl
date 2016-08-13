## quick and dirty hack to add users from a tab seperated list of names and usernames
##
#!/usr/bin/perl
use strict;

eval 'exec /usr/bin/perl  -S $0 ${1+"$@"}'
    if 0; # not running under some shell

use SourceForge;

my $user = "dthomas";
my $pass = "w1llyb0b";

my $sfee = new SourceForge;
my $session = $sfee->login($user,$pass);
die("Login failed") unless($session);

while(<STDIN>) {        
	chomp;
        my ($fullname, $username) = split(/\t/, $_);
	# skip malformed input
	next unless($username && $fullname);
	my $ret = $sfee->createUser(
		$session, 
		$username, 
		$username."\@collab.net", 
		$fullname, 
		"en_US", 
		"US/Central", 
		1, 
		0, 
		"ChangeMe"
	);
	print "Failed to add user $username!\n" unless($ret);
}

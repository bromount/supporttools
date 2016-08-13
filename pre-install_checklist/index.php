<?php

include_once('functions.php');

session_start(); 

$values = array ('install_date' => "Contact Information",
		'collab_name' => "Contact Information",
		'collab_work' => "Contact Information",
		'collab_cell' => "Contact Information",
		'collab_email' => "Contact Information",
		'cust_company' => "Contact Information",
		'cust_name' => "Contact Information",
		'cust_tz' => "Contact Information",
		'cust_work' => "Contact Information",	
		'cust_cell' => "Contact Information",
		'cust_email' => "Contact Information");

// fill $_SESSION from POST vars
foreach ($values as $i => $value) {
	if(isset($_POST[$i])){
		$_SESSION[$i] = $_POST[$i];
		print "$i = $_SESSION[$i]<br>\n";
	}
}
// quick jump menu
//print $_POST['next_section'];

$sections = array ('contact_info' => "Contact Information",
		'install_info' => "Installation Information",
		'hardware_env' => "Hardware and Network Environment",
	        'app_server_info' => "Applicatin Server Info",
 	        'scm_server_info' => "SCM Server Info",
 	        'db_server_info' => "Database Server Info",
	        'dns_info' => "DNS Info",
	        'mail_info' => "Mail Info",
        	'firewall_info' => "Firewall Info",
	        'misc_info' => "Misc Info",
	        'special' => "Special Considerations",
	        'support_access' => "Support Access",
		'verify_and_send' => "Verify and Send");


print "<form action=\"$PHP_SELF\"
	method=\"POST\">\n";
print "Jump to Section <select name=\"next_section\">\n";
foreach ($sections as $i => $value) {
	print "<option ";
	if ($i == $_POST['next_section']){
		print "selected";
	}
	print " value=\"$i\">$sections[$i]</option>\n";
}
print "</select>\n";	
					
print "<input type=\"submit\" value=\"Go\">\n";
print "</form>\n";	


// determin which section to show

if($_POST['next_section'] == "verify_and_send"){
	verify_and_send();
}
elseif($_POST['next_section'] == "app_server_info"){
	print_app_server_info();
}
elseif($_POST['next_section'] == "scm_server_info"){
	print_scm_server_info();
}
elseif($_POST['next_section'] == "hardware_env"){
	print_hardware_env();
}
elseif($_POST['next_section'] == "install_info"){
	print_install_info();
} 
elseif($_POST['next_section'] == "db_server_info" && $_POST['scm_coresident'] == "N"){
	print_scm_extra_server_info();
}
elseif($_POST['next_section'] == "db_server_info"){
        print_db_server_info();
}
elseif($_POST['next_section'] == "dns_info" && $_POST['db_type'] == "Oracle"){
	print_db_oracle_info();
}
elseif($_POST['next_section'] == "dns_info"){
	print_dns_info();
}
elseif($_POST['next_section'] == "mail_info"){
	print_mail_info();
}
elseif($_POST['next_section'] == "firewall_info"){
	print_firewall_info();
}  
elseif($_POST['next_section'] == "misc_info"){
	print_misc_info();
}  
elseif($_POST['next_section'] == "special"){
	print_special_considerations();
}  
elseif($_POST['next_section'] == "support_access"){
	print_support_access();
}  
elseif($_POST['next_section'] == "approval"){
	print_verification_approval();
}
elseif($_POST['next_section'] == "mailit"){
	mailit();
}
else {
	print_contact_info();
}
?>

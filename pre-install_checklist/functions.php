<?php
function print_contact_info() {
	print "<h2>Contact Information:</h2>\n";

	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";
	print "<tr><td>Requested Installation Date:</td> 
		<td><input type=\"text\"
		name=\"install_date\">\n</td></tr>";
	print "<tr><td><p/></td></tr>\n";	
	print "<tr><td>Primary CollabNet technical Contact:</td> 
                <td><input type=\"text\"
                name=\"collab_name\"></td></tr>\n";
	print "<tr><td>Work #:</td> <td><input type=\"text\" 
			name=\"collab_work\"></td>\n";
	print "<tr><td>Cell #:</td> <td><input type=\"text\" 
			name=\"collab_cell\"></td></tr>\n";
	print "<tr><td>Email:</td> <td><input type=\"text\" 
			name=\"collab_email\"></td></tr>\n";
	
	print "<tr><td><p/></td></tr>\n";
	print "<tr><td>Company Name:</td>
		<td><input type=\"text\"
		name=\"cust_company\"></td></tr>\n";
	print "<tr><td>Customer Primary Contact:</td>
		<td><input type=\"text\"
		name=\"cust_name\"></td></tr>\n";
	print "<tr><td>Business Hours/Time Zone</td>
		<td><input type=\"text\" name=\"cust_tz\"></td></tr>\n";
	print "<tr><td>Work #:</td> <td><input type=\"text\" 
			name=\"cust_work\"></td>\n";
	print "<tr><td>Cell #:</td> <td><input type=\"text\" 
			name=\"cust_cell\"></td></tr>\n";
	print "<tr><td>Email:</td> <td><input type=\"text\" 
			name=\"cust_email\"></td></tr>\n";
	
	print "</table>\n";		
	print "<input type=\"hidden\" name=\"next_section\" value=\"install_info\">\n";				
	print "<input type=\"submit\" value=\"Next\">\n";
}
function print_install_info() {
	print "<h2>Installation Information:</h2>\n";

	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";
	print "<tr><td>Will SourceForge be on a dedicated server?</td>
	<td><select name=\"ded_server\"><option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>If not, what else will be on the server?</td>
	<td><input type=\"text\" name=\"other_proc\"></td></tr>\n";
	print "<tr><td>Customer accepts and agrees to the recommended hardware<br> and software stack configuration?</td>
		<td><select name=\"cust_agree\"><option>No</option><option>Yes</option></td></tr>\n";
	
	print "</table>\n";		
	print "<input type=\"hidden\" name=\"next_section\" value=\"hardware_env\">\n";				
				
	print "<input type=\"submit\" value=\"Next\">\n";
	print "</form>\n";	
}
function print_hardware_env() {
	print"<h2>Hardware and Network Environment</h2>\n";
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";
	
	print "<tr><td>Total Number of Servers (Application, SCM, Database, etc)</td>\n";
	print "<td><select name=\"num_servers\">
	<option>1</option><option>2</option><option>3</option><option>4</option><option>5+</option></td></tr>\n";
	print "</select>\n";
	print "<tr><td>Defined usage of each server (if multiple servers)<br> 
		e.g. App server, SCM server, Database server etc (Server Breakdown)<br> 
		are they on separate servers?</td>
		<td><select name=\"defined_usage\">
		<option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>Network topology defined?</td>
		<td><select name=\"net_topology\">
		<option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>Hardware procured and installed?</td>
		<td><select name=\"hardware_installed\">
		<option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>Installed OS exactly as defined in 
		SourceForge Installation Guide?</td>
		<td><select name=\"os_installed\">
		<option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>Time synchronization (NTP) configured for all servers?</td>
		 <td><select name=\"ntp_installed\">
		 <option>No</option><option>Yes</option></td></tr>\n";
	print "<tr><td>SSL required for web access?</td>
		<td><select name=\"ssl_required\">
		<option>No</option><option>Yes</option></td></tr>\n";
	
	print "</table>\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"app_server_info\">\n";
	print "<input type=\"submit\" value=\"Next\">\n";
	print "</form>\n";
}
function print_app_server_info() {
	print "<h2>SourceForge Application Server</h2>\n";
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	
	print "<tr><td>Operating System</td>
		<td><select name=\"os\">
		<option>RHEL3</option>
		<option>RHEL4</option>
		<option>CentoOS4</option>
		<option>SLES9</option>
		</select></td></tr>\n";
	print "<tr><td>Server Manufacturer</td>
		<td><input type=\"text\" name=\"server_man\"></td></tr>\n";
	print "<tr><td>Processor Model</td>
		<td><input type=\"text\" name=\"proc\"></td></tr>\n";
	print "<tr><td>Number of CPUs (not cores)</td>
		<td><select name=\"num_cpus\">
		<option>1</option>
		<option>2</option>
		<option>2+</option>
		</select></td></tr>\n";
	print "<tr><td>Number of CPU Cores</td>
		<td><select name=\"cpu_cores\">
		<option>1</option>
		<option>2</option>
		<option>2+</option>
		</select></td></tr>\n";

	print "<tr><td>CPU Speed</td>
		<td><input type=\"text\" name=\"cpu_speed\">
		</td></tr>\n";
	print "<tr><td>Amount of Memory (in GB)</td>
		<td><input type=\"text\" name=\"memory\">
		</td></tr>\n";
	print "<tr><td>Amount of Disk (in GB)</td>
		<td><input type=\"text\" name=\"disk\">
		</td></tr>\n";
	print "<tr><td>K/B and Console?</td>
		<td><select name=\"console\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Hyperthreading Disabled on Intel CPUs (recommended)?</td>
		<td><select name=\"console\">
	        <option>No</option>
	        <option>Yes</option>
	        </td></tr>\n";

	print "</table>\n";		
	print "<input type=\"hidden\" name=\"next_section\" value=\"scm_server_info\">\n";	
	print "<input type=\"submit\" value=\"Next\">\n";
	print "</form>\n";
}	
function print_scm_server_info() {
	print "<h2>SCM Server</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>SCM Type?</td>
		<td><input type=\"checkbox\" name=\"CVS\">CVS<br>
		<input type=\"checkbox\" name=\"SVN\">Subversion<br>
		<input type=\"checkbox\" name=\"Perforce\">Perforce<br>
		<input type=\"checkbox\" name=\"ClearCase\">ClearCase<br>
		<input type=\"checkbox\" name=\"Other\">Other<br>

	</td></tr>\n";	
	print "<tr><td>Data migration from existing SCM?</td>
 		<td><select name=\"scm_migration\">
                <option>No</option>
                <option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Name and version of SCM to be migrated</td>
		<td><input type=\"text\" name=\"scm_migrate_from\"></input>
		</td></tr>\n";
	print "<tr><td>Co-resident on Application Server?</td>
		<td><select name=\"scm_coresident\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n"; 
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"db_server_info\">\n";
	print "</form>\n";
}
function print_scm_extra_server_info() {
	print "<h2>SCM Server (Continued)</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Operating System</td>
		<td><select name=\"scm_os\">
		<option>RHEL3</option>
		<option>RHEL4</option>
		<option>CentoOS4</option>
		<option>SLES9</option>
		</select></td></tr>\n";
	print "<tr><td>Server Manufacturer</td>
		<td><input type=\"text\" name=\"scm_server_man\"></td></tr>\n";
	print "<tr><td>Processor Model</td>
		<td><input type=\"text\" name=\"scm_proc\"></td></tr>\n";
	print "<tr><td>Number of CPUs (not cores)</td>
		<td><select name=\"scm_num_cpus\">
		<option>1</option>
		<option>2</option>
		<option>2+</option>
		</select></td></tr>\n";
	print "<tr><td>CPU Speed</td>
		<td><input type=\"text\" name=\"scm_cpu_speed\">
		</td></tr>\n";
	print "<tr><td>Amount of Memory (in GB)</td>
		<td><input type=\"text\" name=\"scm_memory\">
		</td></tr>\n";
	print "<tr><td>Amount of Disk (in GB)</td>
		<td><input type=\"text\" name=\"scm_disk\">
		</td></tr>\n";
	print "<tr><td>K/B and Console?</td>
		<td><select name=\"scm_console\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Hyperthreading Disabled on Intel CPUs (recommended)?</td>
		<td><select name=\"scm_hyperthread_disabled\">
	        <option>No</option>
	        <option>Yes</option>
	        </td></tr>\n";

	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"db_server_info\">\n";
	print "</form>\n";

}
function print_db_server_info() {
	print "<h2>Database Server</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Database Type</td>
		<td><select name=\"db_type\">
		<option>Postgres</option>
		<option>Oracle</option>
		</select></td></tr>\n";
	print "<tr><td>Database Version</td>
		<td><input type=\"text\" name=\"db_ver\">	
		</td></tr>\n";
	print "<tr><td>Co-resident on Application Server? (if yes, skip rest of this section)</td>
 		<td><select name=\"db_coresident\">
                <option>No</option>
                <option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Operating System</td>
		<td><select name=\"db_os\">
		<option>RHEL3</option>
		<option>RHEL4</option>
		<option>CentoOS4</option>
		<option>SLES9</option>
		</select></td></tr>\n";
	print "<tr><td>Server Manufacturer</td>
		<td><input type=\"text\" name=\"db_server_man\"></td></tr>\n";
	print "<tr><td>Processor Model</td>
		<td><input type=\"text\" name=\"db_proc\"></td></tr>\n";
	print "<tr><td>Number of CPUs (not cores)</td>
		<td><select name=\"db_num_cpus\">
		<option>1</option>
		<option>2</option>
		<option>2+</option>
		</select></td></tr>\n";
	print "<tr><td>CPU Speed</td>
		<td><input type=\"text\" name=\"db_cpu_speed\">
		</td></tr>\n";
	print "<tr><td>Amount of Memory (in GB)</td>
		<td><input type=\"text\" name=\"db_memory\">
		</td></tr>\n";
	print "<tr><td>Amount of Disk (in GB)</td>
		<td><input type=\"text\" name=\"db_disk\">
		</td></tr>\n";
	print "<tr><td>K/B and Console?</td>
		<td><select name=\"db_console\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Hyperthreading Disabled on Intel CPUs (recommended)?</td>
		<td><select name=\"db_hyperthread_disabled\">
	        <option>No</option>
	        <option>Yes</option>
	        </td></tr>\n";

	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
        print "<input type=\"hidden\" name=\"next_section\" value=\"dns_info\">\n";
	print "</form>\n";

}
function print_db_oracle_info() {
	print "<h2>Oracle Specific Options</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Oracle version</td>
		<td><select name=\"oracle_ver\">
		<option>9i</option>
		<option>Standard</option>
		<option>Enterprise</option>
		</select></td></tr>\n";
	print "<tr><td>Oracle 10G Client installed?</td>
		<td><select name=\"oracle_10gclient\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>FQDN of Oracle Server</td>
                <td><input type=\"text\" name=\"oracle_fqdn\">
                </td></tr>\n";
	print "<tr><td>TNSName of Oracle Server</td>
                <td><input type=\"text\" name=\"oracle_fqdn\">
                </td></tr>\n";
	print "<tr><td>Oracle DBA on staff?</td>
		<td><select name=\"oracle_dba\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Name of DBA</td>
                <td><input type=\"text\" name=\"oracle_dba_name\">
                </td></tr>\n";
	print "<tr><td>Phone number of DBA</td>
                <td><input type=\"text\" name=\"oracle_dba_phone\">
                </td></tr>\n";
	print "<tr><td>Email of DBA</td>
                <td><input type=\"text\" name=\"oracle_dba_email\">
                </td></tr>\n";
	print "<tr><td>Will Oracle DBA be avaiable on day of SourceForge installation and configuration?</td>
		<td><select name=\"oracle_dba_avaiable\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
        print "<input type=\"hidden\" name=\"next_section\" value=\"dns_info\">\n";
	print "</form>\n";
}
function print_dns_info() {
	print "<h2>DNS Information</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Primary DNS IP</td>
                <td><input type=\"text\" name=\"dns_primary\">
                </td></tr>\n";
        print "<tr><td>Secondary DNS IP</td>
                <td><input type=\"text\" name=\"dns_secondary\">
                </td></tr>\n";
	print "<tr><td>Network Admin on staff?</td>
		<td><select name=\"net_admin\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Name of Network Admin</td>
                <td><input type=\"text\" name=\"netadmin_name\">
                </td></tr>\n";
	print "<tr><td>Phone number of Network Admin</td>
                <td><input type=\"text\" name=\"netadmin_phone\">
                </td></tr>\n";
	print "<tr><td>Email of Network Admin</td>
                <td><input type=\"text\" name=\"netadmin_email\">
                </td></tr>\n";
	print "<tr><td>DNS records for each server</td>
		<td><select name=\"dns_records\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Forward and Reverse DNS verified functional?</td>
		<td><select name=\"dns_verified\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"mail_info\">\n";	
	print "</form>\n";

}
function print_mail_info() {
	print "<h2>Mail Information</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Corporate Mail Server FQDN</td>
                <td><input type=\"text\" name=\"mail_fqdn\">
                </td></tr>\n";
	print "<tr><td>Corporate Mail Server IP</td>
                <td><input type=\"text\" name=\"mail_ip\">
                </td></tr>\n";
	print "<tr><td>Will SourceForge require a relay to send email to external addresses?</td>
		<td><select name=\"mail_relay\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Can SourceForge recieve email from external clients?</td>
		<td><select name=\"mail_incoming\">
		<option>No</option>
		<option>Yes</option>
		</td></tr>\n";
	print "<tr><td>Special considerations regaurding email relaying:</td>
                <td><input type=\"text\" name=\"mail_relay\">
                </td></tr>\n";
	print "<tr><td>Does the Mail Relay require password authentication?</td>
                <td><select name=\"mail_smtpauth\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
        print "<tr><td>If so, are there examples of how this is done?</td>
                <td><select name=\"mail_smtpauth_examples\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	 print "<tr><td>SourceForge admin e-mail address (e-mail address for special admin account):</td>
                <td><input type=\"text\" name=\"mail_admin\">
                </td></tr>\n";
        print "<tr><td>SourceForge system e-mal address (from address for SourceForge generated e-mails):</td>
                <td><input type=\"text\" name=\"mail_system\">
                </td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"firewall_info\">\n";
	print "</form>\n";

}
function print_firewall_info() {
	print "<h2>Firewall</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Firewall in place?</td>
                <td><select name=\"firewall\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td>Allow outbound email from SourceForge</td>
                <td><select name=\"firewall_outboundemail\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td>Allow inbound email to SourceForge?</td>
                <td><select name=\"firewall_inboundemail\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td>Allow access from public IP (outside the firewall)?</td>
                <td><select name=\"firewall_publicaccess\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"misc_info\">\n";
	print "</form>\n";
}
function print_misc_info() {
	print "<h2>Miscellaneous</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";
	print "<tr><td>Servers installed in final location?</td>
                <td><select name=\"final_location\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td>Network connectivity tested between all SourceForge servers (database, application, scm)?</td>
                <td><select name=\"network_con\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td>Confirmed that all 3rd party software that will support SourceForge matches the<br>
		version defined in the SourceForge Reference Environment?</td>
                <td><select name=\"ref_env\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"special_considerations\">\n";
	print "</form>\n";
}
function print_special_considerations(){
	print "<h2>Special Considerations</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
	print "<tr><td>Customer acknowledges that CVS pserver is not supported by SFEE</td>
                <td><select name=\"cvs_ssh\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";
	print "<tr><td><h4>Please note the following sections are not included in a standard install.</br> They are only relevant if an SOW for the work is included.</h4></td></tr>\n";
	print "<tr><td>Does SFEE need to authenticate users via a corporate authentication mechanism such as LDAP?</td>
		<td><select name=\"external_auth\">
		<option>No</option>
		<option>Yes</option>
                </td></tr>\n";
	print "<tr><td>If so, what type?</td>
                <td><select name=\"auth_type\">
                <option>LDAP</option>
                <option>Kerberos</option>
		<option>ActiveDirectory</option>
		<option>Other</option>
                </td></tr>\n";
        print "<tr><td>Will you be migrating existing data into this install?</td>
		<td><select name=\"data_migrate\">
		<option>No</option>
                <option>Yes - From SFEE</option>
                <option>Yes - From another system</option>
                </td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"support_access\">\n";
	print "</form>\n";
}
function print_support_access() {
	print "<h2>CollabNet Technical Support Access</h2>\n";	
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
	print "<table>\n";	
        print "<tr><td>Will you provide remote access to your SourceForge instance to 
		CollabNet Support</td>
                <td><select name=\"remote_access\">
                <option>No</option>
                <option>Yes</option>
                </td></tr>\n";        
	print "<tr><td>If so, by what method?</td>
                <td><select name=\"ra_method\">
                <option>SSH</option>
                <option>Modem</option>
		<option>VPN</option>
		<option>Web Browser</option>
                </td></tr>\n";
	print "</table>\n";		
	print "<input type=\"submit\" value=\"Next\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"verify_send\">\n";
	print "</form>\n";
}
function verify_and_send() {
	print "<h2>Contact Information</h2>\n";
	print "<table>\n";
	print "<tr><td>Requested Installation Date:</td><td>".$_SESSION['install_date']."</td></tr> \n";
	print "<tr><td>Primary CollabNet Technical Contact:</td><td>".$_SESSION['collab_name']."</td></tr>\n";
	print "<tr><td>Work #:</td><td>".$_SESSION['collab_work']."</td></tr>\n";
	print "<tr><td>Cell #:</td><td>".$_SESSION['collab_cell']."</td></tr>\n";
	print "<tr><td>Email #:</td><td>".$_SESSION['collab_email']."</td></tr>\n";
	print "</table>\n";
	
	print "<table>\n";
	print "<tr><td>Company Name:</td><td>".$_SESSION['cust_company']."</td></tr>\n";
	print "<tr><td>Customer Primary Contact:</td><td>".$_SESSION['cust_name']."</td></tr>\n";
	print "<tr><td>Business Hours:</td><td>".$_SESSION['cust_tz']."</td></tr>\n";
	print "<tr><td>Work #:</td><td>".$_SESSION['cust_work']."</td></tr>\n";
	print "<tr><td>Cell #:</td><td>".$_SESSION['cust_cell']."</td></tr>\n";
	print "<tr><td>Email #:</td><td>".$_SESSION['cust_email']."</td></tr>\n";
	print "</table>\n";

	/*
	print "<h2>Installation Information</h2>\n";
	print "<table>\n";
	print "<tr><td>Will SourceForge be on a dedicated server</td><td>".$_SESSION['ded_server']."</td></tr>\n";
	print "</table>\n";
	*/
	print "By clicking submit you agree that all information is verified to be correct..\n";
	print "<form action=\"$PHP_SELF\"
		method=\"POST\">\n";
        print "<input type=\"submit\" value=\"Send\">\n";
	print "<input type=\"hidden\" name=\"next_section\" value=\"mailit\">\n";
	print "</form>\n";
}
function mailit() {
	$message = "Requested Installation Date:\t".$_SESSION['install_date']."\n";
	$message .= "Primary CollabNet Technical Contact:\t".$_SESSION['collab_name']."\n";
	if (mail("dthomas@collab.net", "Pre-Install Checklist ".$_SESSION['cust_company'], $message, "From: dthomas@collab.net")) {
		print "Message sucessfully sent.\n";
	}
	else {
		print "Message failed.\n";
	}
}
?>

<?php


function showform(){

 echo '<html>';
 echo '<form method="post" action="query-account.php">';
 echo 'Enter the Customer Account Name <input type="text" name="accountname">';

 echo '<input type="submit" name="SubmitForm">';
 echo '</form>';

 echo '<br/> Note : Enter Any SalesForce Account Name';
 echo '</html>';
 
 
 }
 
 

if (!isset($_POST['SubmitForm'])) {

showForm();

} else {


 
// SOAP_CLIENT_BASEDIR - folder that contains the PHP Toolkit and your WSDL
// $USERNAME - variable that contains your Salesforce.com username (must be in the form of an email)
// $PASSWORD - variable that contains your Salesforce.com password

define("SOAP_CLIENT_BASEDIR", "./soapclient");
require_once (SOAP_CLIENT_BASEDIR.'/SforceEnterpriseClient.php');
require_once ('userAuth.php');


try {
  $mySforceConnection = new SforceEnterpriseClient();
  $mySoapClient = $mySforceConnection->createConnection(SOAP_CLIENT_BASEDIR.'/enterprise.wsdl.xml');
  $mylogin = $mySforceConnection->login($USERNAME, $PASSWORD);
  
  $accountname = trim($_POST['accountname']);

// $query = "select CaseNumber, Priority, Status, Subject, Type    from Case where CaseNumber = '". $caseno. "'";  working query


 

//$query = "SELECT Name, (SELECT CaseNumber, Status, Priority,Subject, Type  FROM Cases) FROM Account where Account.Name='Scope International'   ";



$query = "SELECT Name, (SELECT CaseNumber, Status, Priority,Subject, Type  FROM Cases) FROM Account where Account.Name= '" . $accountname ."'";

//print $query;
$response = $mySforceConnection->query(($query));

echo ' <table><th>CaseNumber</th><th>Status</th><th>Priority</th><th>Subject</th><th>Type</th> ';

foreach ($response->records as $case) {

foreach($case->Cases->records as $record) {
  

echo '   <tr> <td>';
       print_r($record->CaseNumber);

echo '  </td>  <td> ';
      print_r($record->Status);
echo '   </td> <td>';
print_r($record->Priority);
echo '  </td> <td>';
   print_r($record->Subject);
echo ' </td> <td>';
print_r($record->Type);
echo '</td></tr>';

}
  
}


echo '</table>';


echo '  <br/><a href="query-account.php">Back</a>';

}

 catch (Exception $e) {
  echo $e->faultstring;
}


}
?>

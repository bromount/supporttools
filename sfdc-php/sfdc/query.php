<?php
function showform(){

 echo '<html>';
 echo '<form method="post" action="query.php">';
 echo 'Enter the case Number <input type="text" name="caseno">';
 echo '<input type="submit" name="SubmitForm">';
 echo '</form>';

 echo '<br/> Note : Enter the case number as CNSC-XXXXXX';
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
  
  $caseno = trim($_POST['caseno']);

 $query = "select CaseNumber, Priority, Status, Subject, Type,  SuppliedCompany from Case where CaseNumber = '". $caseno. "'";
 


  $response = $mySforceConnection->query(($query));
  
 // print_r($response);
  
 // print_r($response->Status);

  foreach ($response->records as $record) {
    
 //       print("<br>");
    
   // print_r($record);
    
 echo '   <table> <tr><td> Case Number </td> <td> ';
       print_r($record->CaseNumber);

echo ' </tr> <tr> <td> Status </td> <td> ';
      print_r($record->Status);
echo ' </tr> <tr> <td> Priority </td> <td>';
print_r($record->Priority);
echo ' </tr> <tr> <td> Subject </td> <td>';
   print_r($record->Subject);
echo '</tr> <tr> <td> type </td> <td>';
print_r($record->Type);
echo '</td></tr> </table>';
    
    
  echo '  <br/><a href="query.php">Back</a>';
  }
} catch (Exception $e) {
  echo $e->faultstring;
}

}
?>





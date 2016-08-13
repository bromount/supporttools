<?php
// Duration grapher
// Obviously, if there's no pageid, we should'nt be here...
if (!isset($_GET['id'])) {
    echo "Hrmms.  You shouldn't be here.  Why don't you do something productive?";
    exit(3);
}

include ("./jpgraph/src/jpgraph.php");
include ("./jpgraph/src/jpgraph_line.php");
include ('./jpgraph/src/jpgraph_date.php');

include ('database.inc.php');
$link = mysql_connect($db_host, $db_user, $db_pass);
if (!is_resource($link)) {
    // Yeah.  This is bad.
    echo "Couldn't connect to the database.  Fatal Error.<br>\n";
    exit(1);
}
mysql_select_db($db_name,$link) or die('Fatal error selecting database.');

$query = sprintf("SELECT * FROM pageduration WHERE pid='%d';",
        mysql_real_escape_string($_GET[id]));
$sql = mysql_query($query, $link);
if (mysql_affected_rows($link) == 0) {
    echo "Yeah.  Something's wrong\n";
    exit();
}
while($row = mysql_fetch_array($sql))
{
    // We need to get the time from the original page ID, so we can generate
    // the baseline times to conincide with the original page time.
    // Actually, screw that, we need to have that in the database.  Let's put
    // that information in the database?
    $idnt[] = $row[0];
    $time[] = $row[2];
    $durat[] = $row[5];
    $updur[] = $row[6];
    $pageid[] = $row[4];
    $memallo[] = $row[8];
    $memused[] = $row[9];
    
}
$graph = new Graph(900,300,"auto");
$graph->SetScale("datlin");
$graph->img->SetMargin(75,30,30,70);
$graph->SetMarginColor('white');
$graph->xaxis->SetTickLabels($time);
$graph->xaxis->SetLabelAngle(90);
$graph->xaxis->scale->SetTimeAlign(MINADJ_10);
$graph->SetScale('intlin');
$graph->title->Set('Duration and Memory usage based on page ID');
$duration = new LinePlot($durat);
$duration->SetLegend("Duration (msec)");
$duration->mark->SetType(MARK_DIAMOND);
$duration->mark->SetWidth(1);
$duration->mark->SetFillColor('orange');
$duration->SetCSIMTargets($idnt,$idnt);
$duration->SetColor('green');
$graph->Add($duration);
$uploadduration = new LinePlot($updur);
$uploadduration->mark->SetType(MARK_DIAMOND);
$uploadduration->mark->SetWidth(5);
$uploadduration->mark->SetFillColor('yellow');
$uploadduration->SetCSIMTargets($idnt,$idnt);
$uploadduration->SetLegend("Upload Duration (msec)");
$uploadduration->SetColor('teal');
$graph->Add($uploadduration);
$graph->StrokeCSIM();

?>
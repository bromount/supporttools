<?php
// Memory usage thingiemabobbie
// (C) 2007-2008 Pop Everything Tart.

if (!isset($_GET['id'])) {
    echo "Hrmms.  You shouldn't be here.  Why don't you do something productive?";
    exit(3);
}
include('./jpgraph/src/jpgraph.php');
include('./jpgraph/src/jpgraph_line.php');
include('./jpgraph/src/jpgraph_date.php');

include('database.inc.php');
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
    // Information from rows: durid, pid, PageID, duration, uploadduration, active, memallo, memused
    $time[] = $row[2];
    $freem[] = $row[7];
    $alloc[] = $row[6];
    $durat[] = $row[3];
    $updur[] = $row[4];
    
}



$graph = new Graph(600,300,"auto");
$graph->SetScale("datlin");
$graph->img->SetMargin(75,30,30,70);
$graph->title->Set("Duration for Logfile " . $_GET['id']);
$graph->xaxis->SetTickLabels($time);
$graph->xaxis->SetLabelAngle(90);
// $graph->xaxis->scale->SetTimeAlign(MINADJ_10);
$graph->yaxis->title->Set("Bytes");

$cplot = new LinePlot($alloc);
$cplot->SetColor("red"); // Fill color
$cplot->SetLegend("Allocated Memory");
$graph->Add($cplot);


$bplot = new LinePlot($freem);
$bplot->SetColor("green"); // Fill color
$bplot->SetLegend("Free Memory");
$graph->Add($bplot);



$graph->Stroke(); ?> 


?>
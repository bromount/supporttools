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

$query = sprintf("SELECT `logtime`,`memallo`,`memused`, `pageid` FROM pagehistory WHERE pid='%d';",
        mysql_real_escape_string($_GET[id]));
$sql = mysql_query($query, $link);
if (mysql_affected_rows($link) == 0) {
    echo "Yeah.  Something's wrong\n";
    exit();
}
while($row = mysql_fetch_array($sql))
{
    $time[]  = $row[0];
    $sfreem[] = $row[2];
    $salloc[] = $row[1];
    $query2 = sprintf("SELECT `memallo`,`memused` from pageduration where pageid = '%d' AND pid = '%d",
        mysql_real_escape_string($_GET[id]),
        mysql_real_escape_string($row[3]));
    $sql2 = mysql_query($query2, $link);
    if (mysql_affected_rows($link) == 0) {
        echo "Yeah.  Something's wrong\n";
    exit();
    $row2 = mysql_fetch_array($sql2);
    $ffreem[] = $row2[1];
    $fslloc[] = $row2[0];
}
    
}



$graph = new Graph(900,300,"auto");
$graph->SetScale("datlin");
$graph->img->SetMargin(75,30,30,70);
$graph->title->Set("Memory Usage for Logfile " . $_GET['id']);
$graph->xaxis->SetTickLabels($time);
$graph->xaxis->SetLabelAngle(90);
$graph->xaxis->scale->SetTimeAlign(MINADJ_10);
$graph->yaxis->title->Set("Bytes");
$aplot = new LinePlot($salloc);
$aplot->SetColor("red"); // Fill color
$graph->Add($aplot);
$bplot = new LinePlot($sfreem);
$bplot->SetColor("black"); // Fill color
$graph->Add($bplot);
$cplot = new LinePlot($salloc);
$cplot->SetColor("blue"); // Fill color
$graph->Add($cplot);
$dplot = new LinePlot($sfreem);
$dplot->SetColor("green"); // Fill color
$graph->Add($dplot);
$graph->StrokeCSIM(); ?> 

<?php
// database.inc.php
// Put information for database here.

$db_host = "localhost";
$db_user = "root";
$db_pass = "4ian1234";
$db_name = "logparser";

// SQL for Creating Table:
/*
-- Yup.  This part of the code is SQL, babieeeee...
--

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `logparser`
--

-- --------------------------------------------------------

--
-- Table structure for table `pageduration`
--

CREATE TABLE IF NOT EXISTS `pageduration` (
  `durid` int(11) NOT NULL auto_increment,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `pid` int(11) NOT NULL,
  `PageID` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `uploadduration` int(11) NOT NULL,
  `active` int(11) NOT NULL,
  `memallo` int(11) NOT NULL,
  `memused` int(11) NOT NULL,
  PRIMARY KEY  (`durid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5541 ;

-- --------------------------------------------------------

--
-- Table structure for table `pagehistory`
--

CREATE TABLE IF NOT EXISTS `pagehistory` (
  `entry` int(11) NOT NULL auto_increment,
  `pid` int(11) NOT NULL,
  `logdate` date NOT NULL,
  `logtime` time NOT NULL,
  `call` varchar(100) NOT NULL,
  `pageid` int(11) NOT NULL,
  `username` varchar(16) NOT NULL,
  `usersess` varchar(33) NOT NULL,
  `method` varchar(5) NOT NULL,
  `uri` varchar(255) NOT NULL,
  `active` int(11) NOT NULL,
  `memallo` int(11) NOT NULL,
  `memused` int(11) NOT NULL,
  `useragent` varchar(255) NOT NULL,
  PRIMARY KEY  (`entry`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5541 ;

-- --------------------------------------------------------

--
-- Table structure for table `pid`
--

CREATE TABLE IF NOT EXISTS `pid` (
  `pid` int(11) NOT NULL auto_increment,
  `user` varchar(50) default NULL,
  `email` varchar(50) default NULL,
  `cnsc` varchar(6) default NULL,
  `ipaddr` varchar(16) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `dts` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY  (`pid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COMMENT='`pid`, `user`, `email`, `cnsc`, `ipaddr`, `fname`, `dts`' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Table structure for table `queryhistory`
--

CREATE TABLE IF NOT EXISTS `queryhistory` (
  `entry` int(11) NOT NULL auto_increment,
  `pid` int(11) NOT NULL,
  `logdate` date NOT NULL,
  `logtime` time NOT NULL,
  `call` varchar(100) NOT NULL,
  `pageid` int(11) NOT NULL,
  `queryid` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `username` varchar(16) NOT NULL,
  `usersess` varchar(33) NOT NULL,
  `query` text,
  PRIMARY KEY  (`entry`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=58501 ;

*/
?>
#!/bin/sh

SERVER=scm.appliedbio.sfee-hosted.com
DATE=`date`

echo -n "$DATE:\tCurrent status of $SERVER....."
nc -z $SERVER 443
if [ $? -eq 0 ]
then
	echo OK
else
	echo FAILED
fi

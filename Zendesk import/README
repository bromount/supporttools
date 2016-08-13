import-into-zendesk-forum
=========================

A Python Script to import bunch of offline HTML files into Zendesk Forum creating Topics in a Forum under Categories

To know more, visit http://developer.zendesk.com/documentation/rest_api/forums.html for the list of possible JSON requests available in Zendesk.

Example request available in the Zendesk developers page is using curl.

 <code> curl https://yoursubdomain.zendesk.com/api/v2/topics.json \
-H "Content-Type: application/json" -v -u email:password -X POST \
-d '{"topic": {"forum_id": 79161, "title": "My Topic", "body":"<code>This is some code</code>", "topic_type": "articles", "access": "logged in users" }' <code>

The above example had a limitation of adding HTML code into`<code>`, which is impossible when we had thousands of files to be uploaded.
Thus I wrote a Python script tweaking the above example, 
so that I can refer an external file to fetch HTML contents and import it as an individual Topic. 

How To Run :
============
1. Download export.py and Alter the Forum ID number with yours.
2. Copy the script into the directory containing bunch of HTML files.
3. grant executable permission to the script
`chmod u+x export.py`
4. Run the script `$ python export.py`

Queries / Issues?
===============

https://github.com/ijeyanthan/import-into-zendesk-forum/issues

Feel free to reach out to me in  ijeyanthan [at] gmail [dot] com

To Migrate the HCN contents to ZENDESK:

ZENDESK Side:

* Create a ZENDESK agent account and from there create a helpcenter

* after creating the help center; create new categories in the same; then please make a note of that Categories number in your browser.

* Do not create any sections (articles)


Script Side:

NOTE: Please make sure you have newhtml, upload, error folders created in your
working copy.

1. Fill the config.txt with the required details

2. create  text files with section names (doc team will provide the forum
names), for all your categories.

example : forums-ctf.txt, forums-faq.txt

3. Run collect_titles.py to collect the titles of the html files. (this step is not mandatory)

--> Run add-text.py if DOC team missed any META TAGS.

--> remove index_frames.html and shindex_frames.html from the HTML files because that doesnot have META TAGS

4. run create_forums.py to create required sections automatically

5. run export.py to export all the html files to zendesk

6. after the export.py script; if the html file uploaded successfully it will
moved to upload folder; if not error folder.

7. Check for output.txt file for the coverage name and the file name (provide
this to doc team).

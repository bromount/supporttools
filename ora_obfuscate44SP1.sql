--
-- Obfuscates SF44SP1 Oracle database by replacing sensitive data with generic values.
-- Needless to say, this should be run on a *copy* of the database.
---- First, create copy of your sf44SP1 database and call it "db_obfuscated".
--
-- To obfuscate database copy:
--     sqlplus dbuser/dbpasswd@db_obfuscated < ora_obfuscate44SP1.sql
--
-- To dump ofuscated database:
--     exp dbuser/dbpasswd@db_obfuscated file="sf44SP1_ora.dmp" log="oracle_exp.log"
--
-- Send the file sf44SP1_ora.dmp.
--
-- Note: Because of the obfuscation, if there is a particular user or project
-- that you want us to look at, you will need to give us the userId or
-- projectId. To determine this, run this on the non-obfuscated database:
--     SELECT id FROM sfuser WHERE username='<username>';
--     SELECT id FROM project WHERE title LIKE '<Project Title Start>%';
--
-- NOTE: *In obfuscated database, all passwords are changed to "admin".
--       *for fields, we just obfuscate the field values of the text fields.
--       *for folder, we don't obfuscate the path, which means that it can contain some information on the folder title.

-- $RCSfile: ora_obfuscate44SP1.sql,v $
-- (C) 2008 CollabNet, Inc, All rights reserved.
--


update item set title=('item ' || id);
update destinationblacklist set destination=id;
update role set title=id, description=rpad(id, length(description));
update pending_change set property_value='';

--uncomment next line if you want to obfuscate the search text value of a saved search
--update search_or_filter_field set string_value=id where name='searchText';

--uncomment next line if you want to obfuscate the filter value for a text field of a saved filter
--update search_or_filter_field set string_value=id where name like '_filter!!%text%';

--just change field_value for text fields
update field_value set value=id where id in (select field_value.id from field_value, field where field.display_type='TEXT' and field_value.field_id=field.id);
update field set default_text_value=id where display_type='TEXT' and is_required=0;

update project_membership_request set request_comment=('request_comment' || id), response_comment=('response_comment' || id);
update relationship set forward_description=('fw_description ' || id), back_description=('back_description ' || id);
delete from stored_message;
update external_system set title=('title ' || id), description=('description ' || id);
update sfcomment set description=('description ' || id);
delete from request;
update folder set title=('title ' || id), description=('description ' || id);
-- delete from user_session;
update audit_change set old_value=('old_value ' || id), new_value=('new_value ' || id) where property_type='String';
update audit_change set old_value=(select to_clob(id) from sfuser where username=to_char(old_value)), new_value=(select to_clob(id) from sfuser where username=to_char(new_value)) where property_type='SfUser';
delete from digest_entry;
update stored_file set file_name=('filename_' || id);
delete from request_namedvalues;
update artifact_statistic set context='projects.' || (select project.id from project where artifact_statistic.context=project.path);
update document_statistic set context='projects.' || (select project.id from project where document_statistic.context=project.path);
update frs_statistic set context='projects.' || (select project.id from project where frs_statistic.context=project.path);
update change_preference set context='projects.' || (select project.id from project where change_preference.context=project.path);
update project set title=('title ' || id), description=('description ' || id),path=('projects.' || id) where path like 'projects.%';
update project set title=('title ' || id), description=('description ' || id),path=('templates.' || id) where path like 'templates.%';
update discussion_forum set list_name=id;
update discussion_post set reply_path=id, content=rpad(id, length(content), ' content');
update report set description='description ' || id;
update news_post set body=rpad(id, length(body), ' body');
update scm_file set filename=id;
update scm_commit set commit_message=rpad(id, length(commit_message), ' commit_message');
update scm_repository set repository_path=id;
delete from scm_authorized_keys;
update linked_application set application_url='http://www.collabnet.com', icon_file_id=null;
delete from integration_data_value;
delete from integration_data_namespace;
update frs_file set description=id;
update taskmgr_task set description=rpad(id, length(description), ' description'), planned=rpad(id, length(planned), ' planned'), accomplishments=rpad(id, length(accomplishments), ' accomplishments'), issues=rpad(id, length(issues), ' issues');
update document set description=rpad(id, length(description), ' description');
update document_review set description=rpad(id, length(description), ' description');
update document_review set title=rpad(id, length(title), ' title');
update document_version set version_comment=rpad(id, length(version_comment), ' version_comment'), stored_file_url='http://www.collabnet.com';
update wiki_page_reference set target_page_name=('name ' || NVL((select item.id from item, item item2 where item.name=wiki_page_reference.target_page_name and wiki_page_reference.wiki_page_id = item2.id and item2.folder_id=item.folder_id),id));
update item set name=('name ' || id) where id like 'wiki%' and name != 'HomePage' and name != '$ProjectHome';
update wiki_page_version set version_comment=rpad(id, length(version_comment), ' version_comment');
update artifact set description=rpad(id, length(description), ' description'), text_0=rpad(id, length(text_0), ' text_0'), text_1=rpad(id, length(text_1), ' text_1'), text_2=rpad(id, length(text_2), ' text_2'), text_3=rpad(id, length(text_3), ' text_3'), text_4=rpad(id, length(text_4), ' text_4'), text_5=rpad(id, length(text_5), ' text_5'), text_6=rpad(id, length(text_6), ' text_6'), text_7=rpad(id, length(text_7), ' text_7'), text_8=rpad(id, length(text_8), ' text_8'), text_9=rpad(id, length(text_9), ' text_9'), text_10=rpad(id, length(text_10), ' text_10'), text_11=rpad(id, length(text_11), ' text_11');
update sfuser set username=id, password='$1$LLNvocqW$Kwuj6du7ywrOCtQUnUXbf0', email='noreply@vasoftware.com', full_name=id where not username in ('system', 'nobody', 'admin');
update sfuser set password='$1$LLNvocqW$Kwuj6du7ywrOCtQUnUXbf0',email='noreply@vasoftware.com' where username='admin';
update search_or_filter set name=('name ' || id);
update sfgroup set full_name=id, description=rpad(id,length(description), ' description');

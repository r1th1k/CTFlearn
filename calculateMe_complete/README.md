#calculate me

if you view the page source you can see a calc.src and on examining it you may notice the `eval()` function 

so for this challenge all you need to know about is the `eval()` function

the eval() function take the input as a string and perform operation 

so we can try for `code execution vulnerability` all you need to do is go to burpsuite and play with the expression input

as we know it is an ubuntu system we can first try for linux commands with the separators

and what i did was at first i added a semicolon with the input and entered pwd command (eg)10;pwd

and surprisingly it returned the command on the output of the burpsuite but it did not evaluate the pwd command it just returned pwd

so i tried different commands like echo, cat * and so on and then you know what, the basic ls command worked...(i.e);ls

and the flag is displayed `ctf{watch_0ut_f0r_th3_m0ng00s3}`


 


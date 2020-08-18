##Up For A Little Challenge?

before we begin i need to say you something that this is a cool challenge!!!!!!!!!!!!!

so the first step is to run strings on the .jpg file `strings *.jpg`

and if you go through all the output you will see the following important stuff

a link `https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg -N17hGnFBfJliykJxXu8`

and two statements describing password:
```
Mp real_unlock_key: Nothing Is As It SeemsU

password: Really? Again

```  

and a flag `flag{Not_So_Simple...}` as you might guess this isn't the flag 

so i just followed the link and i got an another zip file

so i unzip it `unzip *.zip`

and i got a directory so i moved to the directory `cd 'Did I Forget Again?'`

inside there is another image which is no use........

so if you run `ls -la` to check whether there are hidden files then congrats you are guess is correct

there is a hidden zip file, unzip it using `unzip .Processing.cerb4`

and it asks for password so i tried both of the password but didn't work (WTF)

so i tried removing the `U` at the end `Nothing Is As It SeemsU`

and it works so the password is `Nothing Is As It SeemsU`

as a result i got another jpg file and open it surprisingly(actually not surprised:( ) the flag is at the bottom right corner 

it is not clear so if u inspect closely you can identify that the flag is `flag{hack_complete}`



# Regular expression for mail address 
import re
mail_ad = input("enter your mail address: ")
p = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
t = p.fullmatch(mail_ad)

if ( t != None ):
    print("valid mail address")
else:
    print("invalid mail address")
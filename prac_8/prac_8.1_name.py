# Regular expression for name (small)
import re # import regular expressions module

name=input("Enter your name: ")
p = re.compile('[a-z]+')
t=p.fullmatch("zman")

if t is not None: # pep 8
    print("[Valid]")
else:
    print("[Invalid]")
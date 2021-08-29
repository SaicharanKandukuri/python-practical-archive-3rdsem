def boxprint(element,_string):
    header = (element * (len(_string) + 4) + "\n")
    body = (element + " " + _string + " " + element )
    footer = ("\n"+element * (len(_string) + 4) + "\n")
    return(header + body + footer)

def sayhello(name):
    print(boxprint("↔","Hello"+name))
    
sayhello("zman")
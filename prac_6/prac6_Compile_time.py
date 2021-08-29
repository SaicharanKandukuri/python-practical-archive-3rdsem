try:
    eval("if 2 is 2")
except SyntaxError:
    print("Compile Time error: Syntax Error")
finally:
    print("Code Failed")

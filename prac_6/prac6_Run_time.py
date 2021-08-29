# exception Handling Runtime exceptions
def divide(a,b):
    return (a/b)

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = divide(a,b)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print(result)
finally:
    print("This is finally")
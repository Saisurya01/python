def add(a,b):
    return f"Result : {a+b}"
def sub(a,b):
    return f"Result : {a-b}"
def mul(a,b):
    return f"Result : {a*b}"
def div(a,b):
    return f"Result : {a/b}"

choice=input("Choose operation (+ - * /):")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if choice=="+":
    print(add(a,b))
elif choice=="-":
    print(sub(a,b))
elif choice=="*":
    print(mul(a,b))
elif choice=="/":
    print(div(a,b))
else:
    print("Invalid operation")

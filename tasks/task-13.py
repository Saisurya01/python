#even odd checker
print("Even Odd Checker")
i=0
for i in range(5):
    num=int(input("Enter a number: "))   
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

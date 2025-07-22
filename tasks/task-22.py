
while True:
    num=int(input("enter a number: "))
    if num==999:
        print("this is the end")
        break
    if num<0:
        continue
    if num>1000:
        print("this is over my limit")
        break
    print(num)
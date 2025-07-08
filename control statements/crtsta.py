#conditional statements
num=int(input("Enter a number: "))
#it olny runs the staments if the conitions are true
if num > 0:
    print("The number is positive.")
#it runs the statements if the the previous condition is false
elif num == 0:
    print("The number is zero.")
#it runs the statements if all the previous conditions are false
else:
    print("The number is negative.")
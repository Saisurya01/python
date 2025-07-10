student={}
student['name'] = input("Enter your name: ")
student['maths']=int(input("Enter your maths marks: "))
student['science']=int(input("Enter your science marks: "))
student['english']=int(input("Enter your english marks: "))

total= student['maths'] + student['science'] + student['english']
average = total / 3
if average >= 75:
    print("Excellent!")
elif average < 50:
    print("Needs Improvement")
else:
    print("Good job!")
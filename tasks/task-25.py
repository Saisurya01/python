students=[]
print("marks record of a student")
while True:
    print("1. Add a student/n 2. Display a student/n 3. Display all students/n 4. Exit")
    choice=int(input("enter you choice: "))
    if choice==1:
        name=input("enter the name of the student: ")
        marks=int(input("enter the marks of the student: "))
        students.append([name,marks])
    elif choice==2:
        name=input("enter the name of the student: ")
        for student in students:
            if student[0]==name:
                print("student found")
                print("name:",student[0])
                print("marks:",student[1])
          
            else:
                print("student not found")
    elif choice==3:
       for name,marks in students:
            print(name,marks)
    elif choice==4:
        break
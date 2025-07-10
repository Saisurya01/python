person={}

person["name"]=input("Enter your name: ")
person["age"]=int(input("Enter your age: "))
person["gender"]=input("Enter your gender: ")
person["country"]=input("Enter your country: ")


for key, value in person.items():
    print(f"{key}: {value}")
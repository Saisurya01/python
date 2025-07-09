#age calculator
def calculate_age(b_year,current_year):
    return current_year - b_year

byear=int(input("Enter your birth year: "))
current_year=2025
age=calculate_age(byear,current_year)
print(f"You are {age} years old.")
birth_year = input("Enter your birth year: ")
#To handle the base(10) conversion try and except is used. 
try:
    birth_year = int(birth_year)
    current_year = 2025
    age = current_year - birth_year
    print(f"You are approximately {age} years old.")
except ValueError:
    print("Please enter a valid numeric birth year.")
from datetime import date

print("Age Calculator")
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

today = date.today()
dob = date(year, month, day)
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print(f"Your age is: {age} years")

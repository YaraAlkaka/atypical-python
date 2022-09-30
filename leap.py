year = int(input("Enter year:\n"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It is a leap year!")
else:
    print("It is not a leap year")

length = int(input("Enter how tall you are:\n"))
if length >= 170:
    print("tall")
elif length <170 and length > 160 :
    print("normal")
elif length<150:
    print("short")
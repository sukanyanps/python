mon = input("คริสตศักราชที่ ").split(" ")
a = int(mon[0])
if(a % 4 == 0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

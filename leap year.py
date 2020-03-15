x = 1800
print("It is a leap year" if ((x % 100 == 0) and (x % 400 == 0)) or ((x % 100 != 0) and (x % 4 == 0)) else "It is not a leap year") 

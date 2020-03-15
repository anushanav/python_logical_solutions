def tables( ):
    num = int(input("Give the multiplication table of?"))
    i = 1
    while (i<=10):
        print (num,'x', i, '=', num * i )
        i += 1
# while True:  
#     tables()    
#     ask = input("do you want to continue? Yes/ No \n")
#     if (ask == 'No') or (ask == 'no'):
#         print("Thank you")
#         break

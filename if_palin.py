# checking if string is palindrome
def checkpalindrome (inputString):
    i= 0
    j= -1
    while (i <= len(inputString)//2):
        if (inputString [i] != inputString [j]):
           return False
        i +=1
        j -=1
    return True    
inputString = input("enter a word ")      
print (checkpalindrome(inputString)) 

# via recursion

def checkpalindrome_recursion(inputString):
    if inputString =='':
        return True
    elif len(inputString) == 1:
        return True
    elif inputString[0] == inputString[len(inputString)-1]:
        return checkpalindrome_recursion(inputString[1:-1]) 
    else:
        return False

print (checkpalindrome_recursion(inputString))




def palindrome_check(s, f, l):
    if f == l:
        return True
    if s[f] != s[l]:
        return False
    return palindrome_check(s, f+1, l-1)


p = palindrome_check("madama", 0 ,5)
print (p)
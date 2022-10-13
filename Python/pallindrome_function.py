def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
string = "python"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

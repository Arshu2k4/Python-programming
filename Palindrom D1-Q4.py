def ispalindrome(s) :
    rev =''.join(reversed(s))
    if (s==rev):
        return True
    return False
s=input("enter the Number= ")
ans= ispalindrome(s)
if(ans):
    print("The Given Number is a Palindrom")
else:
    print("The Given Number is Not a Palindrom")

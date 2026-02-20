class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if x>0:
            while num!=0:
                digit=num%10
                rev=rev*10+digit
                num=num//10
        if x==rev:
            return True
        else:
            return False
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        def reverse(num,rev):
            if num==0:
                return rev
            return reverse(num//10, rev*10 + num%10)
        return x==reverse(x,0)
        
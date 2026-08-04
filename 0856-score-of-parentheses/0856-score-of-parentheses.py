class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=[0]


        for i in s:
            if i=="(":
                r.append(0)
            elif r and i==")":
                v=r.pop()
                r[-1] += max(2*v, 1)
        return r[0]
                


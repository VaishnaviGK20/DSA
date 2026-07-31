class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=[]
        n=0
        c=""

        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="[":
                r.append((c,n))
                c=""
                n=0
            elif i=="]":
                p,a=r.pop()
                c=p+c*a
            else:
                c+=i
        return c

                
                






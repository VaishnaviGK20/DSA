class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        s=[]
        r=[0]*n
        for i in range(n):
            while s and temperatures[s[-1]]<temperatures[i]:
                x=s.pop()
                r[x]=i-x
            s.append(i)
        return r
       
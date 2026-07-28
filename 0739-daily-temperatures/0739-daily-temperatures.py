class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s=[]
        r=[0]*len(temperatures)

        for i in range(len(temperatures)):

            while s and temperatures[s[-1]]< temperatures[i]:
                x=s.pop()
                r[x]=i-x

            s.append(i)
        return r
            

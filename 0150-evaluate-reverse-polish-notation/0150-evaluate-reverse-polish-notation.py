class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s=[]
        for i in tokens:
            if i not in {"+","-", "*", "/"}:
                s.append(int(i))
            else:
                b=s.pop()
                a=s.pop()
            if i=="+":
                s.append(a+b)
            elif i=="-":
                s.append(a-b)
            elif i=="*":
                s.append(a*b)
            elif i=="/":
                s.append(int(float(a)/b))
        return s[-1]
 
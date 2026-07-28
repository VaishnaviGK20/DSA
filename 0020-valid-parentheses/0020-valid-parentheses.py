class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]

        for i in s:
            if i == "(" :
                a.append(")")
            elif i == "{" :
                a.append("}")
            elif i == "[" :
                a.append("]")

            else:
                if not a or a.pop() != i:
                    return False
        return not a

        return True




        
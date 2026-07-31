class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = []
        r = 0
        n = 0
        op = 1

        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)

            elif i == "+":
                r += n * op
                n = 0
                op = 1

            elif i == "-":
                r += n * op
                n = 0
                op = -1

            elif i == "(":
                res.append(r)
                res.append(op)
                r = 0
                op = 1

            elif i == ")":
                r += op * n
                n = 0
                r *= res.pop()
                r += res.pop()

        r += op * n
        return r
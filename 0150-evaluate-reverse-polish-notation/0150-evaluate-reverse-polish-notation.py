class Solution(object):
    def evalRPN(self, tokens):
        s = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                s.append(int(i))
            else:
                p = s.pop()
                q = s.pop()

                if i == "+":
                    s.append(q + p)
                elif i == "-":
                    s.append(q - p)
                elif i == "*":
                    s.append(q * p)
                elif i == "/":
                    s.append(int(float(q) / p))

        return s[-1]
class Solution(object):
    def backspaceCompare(self, s, t):
        a = []
        b = []

        for i in s:
            if i == "#":
                if a:
                    a.pop()
            else:
                a.append(i)

        for i in t:
            if i == "#":
                if b:
                    b.pop()
            else:
                b.append(i)

        return a == b
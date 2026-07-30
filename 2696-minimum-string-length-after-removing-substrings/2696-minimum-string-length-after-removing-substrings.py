class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = []

        for i in s:
            if r and i == "B" and r[-1] == "A":
                r.pop()
            elif r and i == "D" and r[-1] == "C":
                r.pop()
            else:
                r.append(i)

        return len(r)
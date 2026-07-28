class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        result = [0] * n
        stack = []   # stores indexes

        for i in range(n):

            # Current temperature is warmer than previous temperatures
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day

            # Store current day index
            stack.append(i)

        return result
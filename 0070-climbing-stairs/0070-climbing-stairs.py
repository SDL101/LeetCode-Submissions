class Solution:
    def climbStairs(self, n: int) -> int:
        waysArr = [0 for _ in range(n+1)]

        for i in range(n+1):
            if i == 0 or i == 1:
                waysArr[i] = 1
            else:
                waysArr[i] = waysArr[i-1] + waysArr[i-2]
        return waysArr[-1]

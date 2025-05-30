class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indexMap = {}
        countArr = []
        numArr = []

        for num in nums:
            if num not in indexMap:
                indexMap[num] = len(numArr)
                numArr.append(num)
                countArr.append(1)
            else: 
                idx = indexMap[num]
                countArr[idx] = countArr[idx] + 1
        res = []
        for i in range(k):
            maxCount = 0
            maxCountIndex = 0
            for j in range(len(numArr)):
                currCount = countArr[j]
                if currCount > maxCount:
                    maxCount = currCount
                    maxCountIndex = j
            countArr[maxCountIndex] = -1
            res.append(numArr[maxCountIndex])

        return res
            
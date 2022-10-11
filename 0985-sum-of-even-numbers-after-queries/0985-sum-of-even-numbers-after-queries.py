class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        evenSum = 0
        
        for n in nums:
            if n % 2 == 0:
                evenSum += n
        for q in queries:
            if nums[q[1]] % 2 == 0:
                evenSum -= nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                evenSum += nums[q[1]]
            output.append(evenSum)
        return output
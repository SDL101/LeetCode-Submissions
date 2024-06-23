class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = res = 0
        
        maxQ = collections.deque()
        minQ = collections.deque()
        
        for right in range(len(nums)):
        
            while maxQ and nums[right] > maxQ[-1]:
                maxQ.pop()
            while minQ and nums[right] < minQ[-1]:
                minQ.pop()

            maxQ.append(nums[right])
            minQ.append(nums[right])

            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[left]:
                    maxQ.popleft()
                if minQ[0] == nums[left]:
                    minQ.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0. Overview - sort arr non-descending ord, loop over idxs, use 2ptr squeeze on rest of arr

        # 1. Sort arr in place ( .sort() sorts in place, while sorted() creates new list) 
        #    into non-descending order
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and (nums[i - 1] == nums[i]):
                continue
            l, r = i + 1, len(nums)-1
            while l < r: 
                tripletSum = nums[i] + nums[l] + nums[r]
                if tripletSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif tripletSum < 0:
                    l += 1
                elif tripletSum > 0:
                    r -= 1
        return res

        # Time Complexity:   O(n^2)
        # Space Complexity:  O(n)
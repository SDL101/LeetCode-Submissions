class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 0. Algo Notes - need linear (Big O of n) solution, one solution exactly, nums.length >= 2 

        # 1. Create a hashmap of: {num: index} for each num visited
        numMap = {}
        # 2. Loop over each num in nums
        for i, num in enumerate(nums):
        # 3. Check if (target - num) exists in hashmap keys
            diff = target - num
            # 4. If the diff (the val we're searching for) isn't in the numMap, add it as {num: index}
            if diff not in numMap:
                numMap[num] = [i]
            # 5. Otherwise, the value we need (which is diff) has been visited, 
            # we need to ret: [curr idx in loop, corresponding value of diff's key in map which is its idx]
            else:
                numMap[diff].append(i)
                return numMap[diff]


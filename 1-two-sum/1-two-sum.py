class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
#         create empty hashmap with values as keys, index as corresponding values
#         iterate through the array nums
#         check if target minus num exists in the hashmap
#         if not, add num to hashmap and iterate pointer 
#         to next element
#         return index of element subtracted and index of resulting value
    
        hashmap = {}
        for i, n in enumerate(nums):
            sec_num = target - n
            if sec_num in hashmap:
                return (hashmap[sec_num], i)
            hashmap[n] = i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
#         create empty hashmap, to have given array values added as keys, 
#         their corresponding index as the keys values
#         iterate through the array nums
#         check if target minus num exists in the hashmap
#         if not, add num to hashmap and continue loop 
#         when target minus num is found as a key in hashmap 
#         return two things, the index of num, and the value corresponding to the key of               target minus num (which holds the index)
    
        hashmap = {}
        for i, n in enumerate(nums):
            sec_num = target - n
            if sec_num in hashmap:
                return (hashmap[sec_num], i)
            hashmap[n] = i
        
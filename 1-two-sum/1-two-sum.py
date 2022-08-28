class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         nums = [2,7,11,15]
#         target = 22

#create empty hashmap - keys as nums and values as indeces 
#loop through my nums array
#take my target val and subtract num from each iteration of the loop 
#check if resulting value is in my hashmap 
#if not, add the num
#if it is, return the value index and the num iteration index

        hashy_map = {}
        index_array = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashy_map:
                index_array.append(index)
                index_array.append(hashy_map[diff])
            else:
                hashy_map[num] = index
                
        return index_array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        input is array called nums
        if any value appears 2 or more times
        return true
        if no repeating element values in the array
        return false
        
        create empty set
        iterate through nums array
        if value is in set
        return true
        if not, move to next element and repeat
        if reach end of array and no match 
        return false
        '''
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
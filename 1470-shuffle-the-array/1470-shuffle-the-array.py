# Understand what the interviewer is asking for by using test cases and questions about the problem.
# Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
# Plan the solution with appropriate visualizations and pseudocode.
# Implement the code to solve the algorithm.
# Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
# Evaluate the performance of your algorithm and state any strong/weak or future potential work.


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #create empty array
        #loop through the given array and append index 0, increment
        #append index n, then increment
        #continue while n < len(nums)
        #return new array
        
        #nums = [2,5,1,3,4,7]
        #n = 3
            
        temp = n 
        x = 0
        shuffled_nums = []
        while x < temp:
            shuffled_nums.append(nums[x])
            x += 1
            while n < len(nums):
                shuffled_nums.append(nums[n])
                n +=1
                break
        return shuffled_nums
    
                
                
                
            
            
class Solution:
    def climbStairs(self, n: int) -> int:
        
        count = 0 
        one_steps = n
        two_steps = 0
        
        while one_steps >= 0:    # while there is more than 1 step, continue
        
            
            count += self.helper_1(one_steps, two_steps)
            one_steps -= 2
            two_steps += 1
        return count
    
    
    def helper_1(self, one_steps, two_steps):
        
         # (one_steps + two_steps)!
          # ---------------------------
          # (one_steps)! * (two_steps)!
            
        value_1 = 1
        
        i = one_steps + two_steps
        while i > 0:
            value_1 *= i
            i -= 1
            
        
        value_2 = 1
        
        i = one_steps
        while i > 0:
            value_2 *= i
            i -= 1

    
        value_3 = 1
        
        i = two_steps
        while i > 0:
            value_3 *= i
            i -= 1
            
            
        num_ways = int(value_1 / (value_2 * value_3))
        
        return num_ways
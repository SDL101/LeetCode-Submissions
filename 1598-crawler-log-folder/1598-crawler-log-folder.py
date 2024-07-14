class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for op in logs:
            if op[0] == '.' and op[1] == '.' and count > 0:
                count -= 1
            elif op[0] != '.':
                count += 1
                
        return count 
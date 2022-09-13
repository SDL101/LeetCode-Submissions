class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        row_strings = [""] * numRows
        step = 1
        index = 0
        output = ""
        
        for char in s:
            if index == 0:
                step = 1
                    
            if index == numRows - 1:
                step = -1
                
            row_strings[index] += char
            index += step
            
        for row in row_strings:
            output += ''.join(row)
    
        return output
            
class Solution:
    def intToRoman(self, num: int) -> str:
        romanOut = ""
        symValMap = {          
                     "I":1,
                    "IV":4,
                     "V":5,
                    "IX":9,
                     "X":10,
                    "XL":40,
                     "L":50,
                    "XC":90,
                     "C":100,
                    "CD":400, 
                     "D":500,
                    "CM":900,
                     "M":1000
                    }
        
        for roman in reversed(symValMap):
            if num - symValMap[roman] >= 0:
                symCount = num // symValMap[roman]
                romanOut = romanOut + (roman * symCount)
                num = num - (symValMap[roman]* symCount)
        return romanOut
                
                
                
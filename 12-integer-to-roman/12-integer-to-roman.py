class Solution:
    def intToRoman(self, num: int) -> str:
        
        #num = 1994
        roman_output = ""
        
        roman_map = { 
                     "M": 1000,
                    "CM": 900,
                     "D": 500,
                    "CD": 400,
                     "C": 100,
                    "XC": 90,
                     "L": 50,
                    "XL": 40,
                     "X": 10,
                    "IX": 9,
                     "V": 5,
                    "IV": 4,
                     "I": 1
                    } 

        for each in roman_map.keys():
            if num - roman_map[each] >= 0:
                freq = num // roman_map[each]
                num = num % roman_map[each]   
                for i in range(freq):
                    roman_output = roman_output + each 

        return roman_output
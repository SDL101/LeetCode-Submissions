class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        plantable = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
            return False
        while i <= (len(flowerbed)-1):
            if i == 0:
                if (flowerbed[i] == 0 and 
                    flowerbed[i+1] == 0):
                    
                    flowerbed[i] = 1
                    plantable += 1
                    
            elif i == len(flowerbed)-1:
                if (flowerbed[i] == 0 and 
                    flowerbed[i-1] == 0):
                    
                    flowerbed[i] = 1
                    plantable += 1     
                    
            elif (flowerbed[i] == 0 and 
                flowerbed[i-1] == 0 and 
                flowerbed[i+1] == 0):
                
                flowerbed[i] = 1
                plantable += 1
            i+=1
        
        print(flowerbed)
        if n <= plantable:
            return True
        return False
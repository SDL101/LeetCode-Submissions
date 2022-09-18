
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        original = image[sr][sc]
        # 1
        
        self.fill(image, sr, sc, original, color)
        return image
        
        
    def fill(self, image, sr, sc, original, color):
        print()
        if image[sr][sc] != original:
            
            return
        
        image[sr][sc] = color
        if sr > 0:
            self.fill(image, sr -1, sc, original, color)  #up
        if sr + 1 < len(image): 
            self.fill(image, sr + 1, sc, original, color) #down
        if sc > 0:
            self.fill(image, sr, sc -1, original, color)  #left
        if sc + 1< len(image[0]):
            self.fill(image, sr, sc + 1, original, color) #right
            
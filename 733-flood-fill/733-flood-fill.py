class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
        
    def fill(self, image, sr, sc, original_color, color):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != original_color:
            return 
        image[sr][sc] = color

        self.fill(image, sr-1, sc, original_color, color) #UP
        self.fill(image, sr+1, sc, original_color, color) #DOWN
        self.fill(image, sr, sc-1, original_color, color) #LEFT
        self.fill(image, sr, sc+1, original_color, color) #RIGHT
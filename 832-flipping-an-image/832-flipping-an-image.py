class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #  image = [[1,1,0,0],
        #           [1,0,0,1],
        #           [0,1,1,1],
        #           [1,0,1,0]]
        
        # row_len = len(image[0])
        
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for column in range(len(image[i])):
                if image[i][column] == 0:
                    image[i][column] = 1
                else:
                    image[i][column] = 0
        return image
                
      

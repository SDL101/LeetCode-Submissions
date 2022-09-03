class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            image[i] = image[i][::-1]
            for column in range(len(image[i])):
                if image[i][column] == 0:
                    image[i][column] = 1
                else:
                    image[i][column] = 0
        return image

      

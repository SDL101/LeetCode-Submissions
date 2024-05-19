class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        boolArr = [False for _ in range(len(candies))]
        print(boolArr)
        
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxCandy:
                boolArr[i] = True
        return boolArr
            
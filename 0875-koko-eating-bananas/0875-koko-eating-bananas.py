class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        slowest = max(piles)
        
        while l <= r:
            m = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            if hours <= h:
                slowest = min(m, slowest)
                r = m - 1
            else:
                l = m + 1
        return slowest
    
    
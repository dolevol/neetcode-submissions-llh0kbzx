import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        high = max(piles)
        low = 1
        mid = 1
        
        agg_hours = 0

        # If you have as many or more hours than piles, you must at least eat max pile per hour
        # (this is optional; binary search will handle it)
        if(h == len(piles)):
            return high

        while(low <= high):

            for pile in piles:
                agg_hours += math.ceil(pile / mid)

            if(agg_hours > h):
                low = mid + 1
            else:
                high = mid - 1
            
            agg_hours = 0
            mid = (high+low) // 2

        return low    




        
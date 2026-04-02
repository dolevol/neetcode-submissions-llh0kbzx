import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        high = max(piles)
        low = 1
        mid = 1
        
        agg_hours = 0

        if(h == len(piles)):
            return high

        


        while(low <= high):

            mid = (high+low) // 2

            for pile in piles:
                agg_hours += math.ceil(pile / mid)

            if(agg_hours > h):
                low = mid + 1
            else:
                high = mid - 1
            
            agg_hours = 0

        return low    




        
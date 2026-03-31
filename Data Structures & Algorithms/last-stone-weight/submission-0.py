import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        initial_max = stones[0]

        while(len(stones)>1):
            first_stone = stones[0]
            second_stone = max(stones[1],stones[2]) if len(stones) > 2  else stones[1]
            
            heapq.heappop_max(stones)
            heapq.heappop_max(stones)

            if (first_stone > second_stone):
                heapq.heappush_max(stones, first_stone - second_stone)


        return stones[0] if stones else 0              

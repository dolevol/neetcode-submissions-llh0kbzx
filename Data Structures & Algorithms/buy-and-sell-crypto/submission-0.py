class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_i = prices[0]
        max_diff = 0

        for i in range(len(prices) - 1):
            if(prices[i+1] < min_i):
                min_i = prices[i+1]

            else:
                if(prices[i+1] - min_i > max_diff):
                    max_diff = prices[i+1] - min_i

            print("iter:",i, "min_i",min_i,"max_diff", max_diff)        

        return max_diff               


        
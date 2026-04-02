class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        agg_xor = 0

        for num in nums:
            agg_xor = agg_xor ^ num



        return agg_xor    

        
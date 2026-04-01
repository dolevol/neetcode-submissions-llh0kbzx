# class Node:
#         def __init__(self):
#                 self.val = val
#                 self.next = _next

class Solution:
    def climbStairs(self, n: int) -> int:

        vals = {-2:0, -1:0, 0:0, 1:1, 2:2}

        def climbStairsRec(n: int, vals: dict) -> int:
                if(n not in vals):
                        vals[n] = climbStairsRec(n - 1, vals) + climbStairsRec(n - 2, vals)
                
                return vals[n]                          
        



        return climbStairsRec(n, vals)
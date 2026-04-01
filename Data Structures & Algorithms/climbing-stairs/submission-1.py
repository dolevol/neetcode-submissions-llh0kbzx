class Solution:
    def climbStairs(self, n: int) -> int:

        vals = [-1] * (n)

        if(n > 1):
                vals[0] = 1

        if(n > 2):
                vals[1] =  2       

        def climbStairsRec(n: int) -> int:
                if(n <= 2):
                        return n        

                if(vals[n-1] == -1):        
                        vals[n-1] = climbStairsRec(n-1) + climbStairsRec(n-2)
                
                return vals[n-1]                                   
        



        return climbStairsRec(n)
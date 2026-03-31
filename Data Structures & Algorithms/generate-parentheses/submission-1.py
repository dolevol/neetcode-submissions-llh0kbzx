class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        open_left = n
        balance = 0

        def backtracking(path,open_left,balance):

            if(path is not None and len(path)== 2*n):
                res.append("".join(path))
                return

            if(open_left > 0):
                path.append("(")
                backtracking(path,open_left-1,balance+1)
                path.pop() 

            if(balance > 0):
                path.append(")")
                backtracking(path,open_left,balance-1)
                path.pop()     

        backtracking(["("],open_left-1,balance+1)
        return res    
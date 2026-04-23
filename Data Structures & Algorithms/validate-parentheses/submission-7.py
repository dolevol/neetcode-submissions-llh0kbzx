class Solution:
    def isValid(self, s: str) -> bool:
        stack               = []
        op = ['(','{','[']
        cl = [')','}',']']
        
        for ch in s:

            if ch in op:
                stack.append(ch)

            elif ch in cl:
                if len(stack)==0:
                    return False
                popped = stack.pop()
                print(popped, ch)
                if(op.index(popped) != cl.index(ch)):
                    return False
            
            
            else:
                print(s, stack)
                return False

        if len(stack) != 0:
            return False

        return True        



        
    
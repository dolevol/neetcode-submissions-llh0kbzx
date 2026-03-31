class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(','{','[']
        closing = [')', '}', ']']

        if s is None:
                return True

        for ch in s:
                print("stack:",stack,"ch:", ch)
                if ch not in opening and ch not in closing:
                        return False
                
                if ch == opening[0]:
                        stack.append(closing[0])
                elif ch == opening[1]:
                        stack.append(closing[1])
                elif ch == opening[2]:
                        stack.append(closing[2])        
                else:
                        if(not stack or ch != stack[-1]):
                                return False
                        else:
                                stack.pop()


        return not stack                                        
                        

        
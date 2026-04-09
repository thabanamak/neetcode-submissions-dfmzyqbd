class Solution:
    def isValid(self, s: str) -> bool:
        openbrack = ['(','[',"{"]
        closebrack = [')',']',"}"]
        stack = []
        for char in s:
            if char in openbrack:
                stack.append(char)
            elif char in closebrack:
                if not stack:
                    return False 
                item = stack.pop()
                if openbrack.index(item) != closebrack.index(char):
                    return False 
        return len(stack) == 0

        
class Solution:
    def isValid(self, s: str) -> bool:
        # make a stack that holds all opening brackets.
        # if a closing is found, pop from stack
        # if set is empty or poped isnt the right one, return false

        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in range(len(s)):
            if s[c] in brackets.keys():
                stack.append(s[c])
                continue
        
            if len(stack) < 1 or s[c] != brackets[stack.pop()]:
                return False
        
        return True if len(stack) == 0 else False
        
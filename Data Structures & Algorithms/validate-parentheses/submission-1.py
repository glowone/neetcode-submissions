# given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# s is only valid if opened and closed by same type of bracket
# brackets are closed in correct order
# every close has corresponding open bracket of same type 
# return if s is a valid string and false otherwise 


class Solution:
    def isValid(self, s: str) -> bool: 

        stack= []
        closingKeys = {')': '(', '}': '{', ']': '['}

        for c in s: 
            if c in closingKeys:
                if stack and closingKeys[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

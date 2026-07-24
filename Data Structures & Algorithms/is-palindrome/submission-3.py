#solution 1 - brute force, works

# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned_original = re.sub(r'[^a-zA-Z0-9]', '', s)
#         lower_original = cleaned_original.lower()
#         print(lower_original)
#         #original string in properly formatted
#         reverse_original = lower_original[::-1]
#         print(reverse_original)
#         if lower_original == reverse_original:
#             return True
#         else:
#             return False


# sol = Solution() 

# test_string = "Was it a car or a cat I saw?"

# testing = sol.isPalindrome(test_string)

# neetcode sol 1

# class Solution: 
#     def isPalindrome(self, s: str) -> bool: 
#         newStr = ""

#         for c in s: 
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]

# neetcode sol 2 

class Solution: 
    def isPalindrome(self, s:str) -> bool: 
        l = 0
        r = len(s) - 1

        while l < r: 
            while l < r and not self.alphaNum(s[l]): 
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1 
            r -= 1
        return True 



    def alphaNum(self, c): 
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')) #this is how you get the aski value 
        

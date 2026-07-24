import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_original = re.sub(r'[^a-zA-Z0-9]', '', s)
        lower_original = cleaned_original.lower()
        print(lower_original)
        #original string in properly formatted
        reverse_original = lower_original[::-1]
        print(reverse_original)
        if lower_original == reverse_original:
            return True
        else:
            return False




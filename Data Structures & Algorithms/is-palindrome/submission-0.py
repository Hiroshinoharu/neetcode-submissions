class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Ignore alphanumeric characters
            while left < right and not s[left].isalnum():
                left = left + 1
            
            while left < right and not s[right].isalnum():
                right = right - 1
            
            # Performs checks after the alphanumeric characters are filtered out
            if s[left].lower() != s[right].lower():
                return False
            
            # Adjusts pointers
            left += 1
            right -= 1
        
        return True

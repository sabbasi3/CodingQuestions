class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Early return for empty string
        if not s:
            return True
            
        l, r = 0, len(s) -1

        while l < r:
            # Move left pointer to the next alphanumeric character
            while not s[l].isalnum() and l < r:
                l+= 1
            # Move right pointer to the previous alphanumeric character
            while not s[r].isalnum() and l < r:
                r-= 1
            # Compare characters in a case-insensitive manner
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

                

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize index pointers
        start_i = 0
        end_i = len(s) - 1

        while start_i < end_i:
            # Skip invalid characters
            if not s[start_i].isalnum():
                start_i += 1
                continue
            if not s[end_i].isalnum():
                end_i -= 1
                continue
            
            # Check for equality (condition of palindrome)
            if s[start_i].lower() != s[end_i].lower():
                return False

            # Increment index pointers
            start_i += 1
            end_i -= 1

        return True
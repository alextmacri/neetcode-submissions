class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.getCounts(s) == self.getCounts(t)
    
    def getCounts(self, s: str) -> dict:
        s_counts = {}

        for s_char in s:
            if s_char in s_counts:
                s_counts[s_char] += 1
            else:
                s_counts[s_char] = 1
        
        return s_counts
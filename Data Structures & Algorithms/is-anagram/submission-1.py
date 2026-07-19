class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(str(s))!=len(str(t)):
            return False
        else:
            return sorted(s) == sorted(t)

      
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for char in set(s):
                if t.count(char) != s.count(char):
                    return False
            return True
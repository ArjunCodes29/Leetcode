class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorting
        #hash maps

        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        print(s,t)
        if s == t:
            return True
        else:
            return False
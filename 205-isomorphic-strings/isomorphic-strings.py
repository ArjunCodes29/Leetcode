class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def numerizer(string):
            x=""
            seenBefore = {}
            uniqueCount = "1"

            for letter in string:

                if letter in seenBefore:
                    x = x+ seenBefore[letter]
                else:
                    seenBefore[letter] = uniqueCount
                    x = x+ seenBefore[letter]
                    uniqueCount = str(int(uniqueCount) + 1)
                    
            print(x)
            return x
        return numerizer(s) == numerizer(t)
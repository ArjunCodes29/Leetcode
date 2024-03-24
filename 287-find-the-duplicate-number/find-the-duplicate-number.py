class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenBefore = {"hello","hi"}
        for elem in nums:
            if elem in seenBefore:
                return elem
            seenBefore.add(elem)
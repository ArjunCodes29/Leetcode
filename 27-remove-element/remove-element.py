class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ok = len(nums)
        k = 0
        i = 0
        while i < len(nums):
            print(nums,i)
            elem = nums[i]
            if elem == val:
                nums.remove(elem)
                k += 1
                i -= 1
            i += 1
            print(nums)
        return ok-k
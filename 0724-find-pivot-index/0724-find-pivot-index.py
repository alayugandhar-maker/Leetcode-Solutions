class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            first = sum(nums[:i])
            second = sum(nums[i+1:])

            if first ==second:
                return i 
        return -1
        
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n=len(nums)
        n1=n//2 
        for i in nums:
            if nums.count(i)==n1:
                return i
                break
        
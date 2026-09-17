class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n=len(nums)
        add=0
        for i in range(0,n):
            start=max(0,i-nums[i])
            for j in range(start,i+1):
                add+=nums[j]
        return add


        
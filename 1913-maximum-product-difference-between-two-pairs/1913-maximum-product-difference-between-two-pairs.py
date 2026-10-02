class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        pro1=nums[0]*nums[1]
        pro2=nums[-1]*nums[-2]

        return pro2-pro1
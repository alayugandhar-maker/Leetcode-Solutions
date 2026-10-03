class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum1=sum(nums[:k])
        new=len(nums)-k
        sum2=sum(nums[new:])
        return sum2-sum1
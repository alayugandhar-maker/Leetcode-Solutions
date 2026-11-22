class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            ans=divisior(nums,mid)
            if ans<=threshold:
                total=mid
                high=mid-1
            else:
                low=mid+1
        return total
def divisior(nums,mid):
    totals=0
    for i in range(len(nums)):
        totals+=(nums[i]+mid-1)//mid
    return totals
        
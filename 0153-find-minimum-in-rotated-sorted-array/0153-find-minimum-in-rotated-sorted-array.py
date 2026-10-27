class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        ans=float('inf')
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid] and nums[mid]<=nums[high]:
                ans=min(ans,nums[low])
                break
            
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                high=mid-1
                ans=min(ans,nums[mid])
        return ans

        
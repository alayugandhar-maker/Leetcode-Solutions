class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        low,high=0,n-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if low==high:
                ans=min(ans,nums[low])
            if nums[low]==nums[mid]==nums[high]:
                ans=min(ans,nums[low])
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid] and nums[mid]<=nums[high]:
                ans=min(ans,nums[low])
                break
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans

            
        
        
class Solution:
    def search(self, nums: list[int], x: int) -> int:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==x:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=x and x<=nums[mid]:
                    high=mid-1 
                else:
                    low=mid+1
            else:
                if nums[mid]<=x and x<=nums[high]:
                    low=mid+1 
                else:
                    high=mid-1
        return -1
        
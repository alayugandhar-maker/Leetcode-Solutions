class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        low,high=0,n-1
        lb=lowerbound(nums,low,high,target,n)
        if lb==n or nums[lb]!=target:
            return [-1,-1]
        return [lb,upperbound(nums,low,high,target,n)-1]

def lowerbound(nums,low,high,target,n):
    ans=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid 
            high=mid-1
        else:
            low=mid+1 
    return ans 
def upperbound(nums,low,high,target,n):
    ans=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

        
        
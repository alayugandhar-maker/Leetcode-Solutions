class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ms(nums,0,n-1)
        return nums

def ms(nums,low,high):
    if low==high:
        return 
    mid=(low+high)//2
    ms(nums,low,mid)
    ms(nums,mid+1,high)
    merge(nums,low,mid,high)
def merge(nums,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1
    for i in range(low,high+1):
        nums[i]=temp[i-low]
    

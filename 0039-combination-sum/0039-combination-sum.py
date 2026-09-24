class Solution:
    def combinationSum(self, arr: list[int], target: int) -> list[list[int]]:
        ans=[]
        lst=[]
        back(0,arr,ans,lst,target)
        return ans 

def back(idx,arr,ans,lst,target):
    if idx==len(arr):
        if target==0:
            ans.append(lst.copy())
        return
    if(arr[idx]<=target):
        lst.append(arr[idx])
        back(idx,arr,ans,lst,target-arr[idx])
        lst.pop()
    back(idx+1,arr,ans,lst,target)
        
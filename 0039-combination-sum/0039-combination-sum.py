class Solution:
    def combinationSum(self, arr: list[int], target: int) -> list[list[int]]:
       ans=[]
       lst=[]
       combo(0,ans,lst,arr,target)
       return ans


def combo(idx,ans,lst,arr,target):
    if idx==len(arr):
        if target==0:
            ans.append(lst.copy())
        return 
    if arr[idx]<=target:
        lst.append(arr[idx])
        combo(idx,ans,lst,arr,target-arr[idx])
        lst.pop()
    combo(idx+1,ans,lst,arr,target)
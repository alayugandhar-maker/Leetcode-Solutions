class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        lst=[]
        n=len(nums)
        fun(0,lst,n,nums,ans)
        return ans 
def fun(idx,lst,n,nums,ans):
    if idx>=n:
        ans.append(lst.copy())
        return 
    #pick
    lst.append(nums[idx])
    fun(idx+1,lst,n,nums,ans) 
    #non-pick 
    lst.pop()
    fun(idx+1,lst,n,nums,ans)

        
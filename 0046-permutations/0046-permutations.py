class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        lst=[]
        n=len(nums)
        freq=[0]*(n)
        permute(ans,lst,nums,n,freq)
        return ans 


def permute(ans,lst,nums,n,freq):
    if len(lst)==n:
        ans.append(lst.copy())
        return
    for i in range(n):
        if freq[i]==0:
            freq[i]=1
            lst.append(nums[i])
            permute(ans,lst,nums,n,freq)
            lst.pop()
            freq[i]=0




        
        
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        xor=0
        count=[0]
        for i in nums:
            xor|=i 
        ans=[] 
        sub(0,nums,ans,xor,count)
        return count[0]
    
def sub(idx,nums,ans,xor,count):
    if idx==len(nums):
        xor1=0 
        for i in ans.copy():
            xor1|=i 
        if xor1==xor:
            count[0]+=1
        return
    ans.append(nums[idx])
    sub(idx+1,nums,ans,xor,count)
    ans.pop()
    sub(idx+1,nums,ans,xor,count)

        


        
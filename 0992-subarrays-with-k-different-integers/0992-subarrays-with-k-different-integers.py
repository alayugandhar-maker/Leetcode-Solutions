class Solution:
    def atmost(self,nums,k):
        l,r=0,0
        n=len(nums)
        cnt=0
        d={}
        while r<n:
            d[nums[r]]=d.get(nums[r],0)+1 
            while len(d)>k:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1 
            cnt+=(r-l+1) 
            r+=1
        return cnt 

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        cnt1=self.atmost(nums,k)
        cnt2=self.atmost(nums,k-1)

        return cnt1-cnt2

        
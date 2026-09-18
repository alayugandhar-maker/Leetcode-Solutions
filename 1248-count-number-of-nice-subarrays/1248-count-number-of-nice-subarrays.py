class Solution:
    def atmost(self,nums,k):
        n=len(nums)
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[i]=0 
            else:
                nums[i]=1 
        l,r=0,0 
        cnt=0
        add=0

        while r<n:
            add+=nums[r]
            while add>k:
                add-=nums[l]
                l+=1 
            cnt+=(r-l+1)
            r+=1 
        return cnt

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        cnt1=self.atmost(nums,k)
        cnt2=self.atmost(nums,k-1)

        return cnt1-cnt2

        
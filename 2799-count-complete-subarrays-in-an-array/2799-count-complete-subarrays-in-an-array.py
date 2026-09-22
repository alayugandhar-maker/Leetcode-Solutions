class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        nums1=list(set(nums))
        n=len(nums)
        l,r=0,0
        d={}
        while r<n:
            d[nums[r]]=d.get(nums[r],0)+1 

            while len(d)==len(nums1):
                count+=(n-r) 

                d[nums[l]]-=1 
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1 
            r+=1 
        return count

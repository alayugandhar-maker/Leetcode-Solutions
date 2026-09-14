class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #num=list(set(nums))
        #print(num)
        n=len(nums)
        maxsum,add=0,0
        l,r=0,0
        d={}
        while r<n:
            add+=nums[r]
            d[nums[r]]=d.get(nums[r],0)+1
            if r-l+1==k:
                if len(d)==k:
                  maxsum=max(maxsum,add)
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                add-=nums[l]
                l+=1
            r+=1
        return maxsum
        
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=0,0 
        d={}
        maxlen=0

        while r<n:
            d[nums[r]]=d.get(nums[r],0)+1
            while d[nums[r]]>k:
                d[nums[l]]-=1 
                l+=1
            maxlen=max(maxlen,r-l+1)
             
            r+=1
        return maxlen
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right=0,0
        n=len(nums)
        zero=0
        maxlen=0

        while right<n:
            if nums[right]==0:
                zero+=1 
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            if zero<=k:
                l=right-left+1
                maxlen=max(maxlen,l)
            right+=1 
        return maxlen
        
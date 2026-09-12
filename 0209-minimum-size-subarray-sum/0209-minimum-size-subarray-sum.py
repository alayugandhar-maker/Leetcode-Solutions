class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,0
        minlen=float('inf')
        add=0

        while right<n:
            add+=nums[right]
            while add>=target:
                minlen=min(right-left+1,minlen)
                add-=nums[left]
                left+=1    
            right+=1
        if minlen==float('inf'):
            return 0
        else:
            return minlen

        
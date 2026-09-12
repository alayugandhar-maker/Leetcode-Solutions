class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right=0,0
        n=len(nums)
        maxsum=float('-inf')
        add=0 

        while right<n:
            add+=nums[right]

            if right-left+1==k:
                maxsum=max(maxsum,add)

                add-=nums[left]
                left+=1 
            right+=1
        return maxsum/k

        
        
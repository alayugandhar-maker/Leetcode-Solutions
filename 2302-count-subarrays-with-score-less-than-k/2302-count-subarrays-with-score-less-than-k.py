class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        left,right=0,0
        n=len(nums)
        count,add=0,0
        while right<n:
            add+=nums[right]
            while add*(right-left+1)>=k:
                add-=nums[left]
                left+=1
            count+=(right-left+1)
            right+=1
        return count

        
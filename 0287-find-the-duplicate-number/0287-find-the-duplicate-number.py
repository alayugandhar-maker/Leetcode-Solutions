class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        ans=0
        for i in nums:
            mask=1<<i
            if ans&mask==0:
                ans|=mask 
            else:
                return i
            
        
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n=len(nums)
        d={}
        for i in range(0,n):
            if nums[i] in d and i-d[nums[i]]<=k:
                return True 
            d[nums[i]]=i 
        return False
        
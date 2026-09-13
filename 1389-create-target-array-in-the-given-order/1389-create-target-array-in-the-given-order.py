class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=len(nums)
        target=[]
        for i in range(0,n):
            target.insert(index[i],nums[i])
        return target
        
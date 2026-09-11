class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        n=len(nums)
        valid=True
        for i in range(1,n):
            if nums[i]%2==0 and nums[i-1]%2==0:
                valid=False
                break
            elif nums[i]%2==1 and nums[i-1]%2==1:
                valid=False
                break
        return valid


        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        r=n-1 

        while l<=r:
            if nums[l]==0:
                del nums[l]
                nums.append(0) 
                r-=1
            else:
                l+=1
        return nums
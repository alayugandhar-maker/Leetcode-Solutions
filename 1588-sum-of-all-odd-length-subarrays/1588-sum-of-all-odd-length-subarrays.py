class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        add=0
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                l=j-i+1
                if l%2!=0:
                  add+=sum(nums[i:j+1])
        return add+sum(nums)
        
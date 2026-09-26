class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n=len(nums)
        count=0
        for i in range(0,n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        count+=1
        return count

        
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for m in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]==nums[m]:
                          count+=1 
        return count       
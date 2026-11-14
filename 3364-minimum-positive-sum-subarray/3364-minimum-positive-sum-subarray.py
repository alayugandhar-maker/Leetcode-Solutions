class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        add=float('inf')
        n=len(nums)
        for i in range(0,n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if l<=(j-i+1)<=r and s>0:
                    add=min(add,s)
        if add==float('inf'):
            return -1
        else:
            return add

        
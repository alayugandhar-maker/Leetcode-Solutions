class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        add=0
        n=len(nums)
        for i in range(0,n):
            s=set()
            for j in range(i,n):
                s.add(nums[j])
                add+=(len(s)*len(s))
                
        return add


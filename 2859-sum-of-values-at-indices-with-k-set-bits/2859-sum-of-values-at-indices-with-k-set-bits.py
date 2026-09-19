class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        add=0
        for i in range(0,n):
            count=i.bit_count()
           # print(count)
            if count==k:
              add+=nums[i]
        return add
        
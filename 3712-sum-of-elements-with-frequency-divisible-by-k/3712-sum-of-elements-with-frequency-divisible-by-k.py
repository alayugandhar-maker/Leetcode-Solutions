class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        add=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]%k==0:
                add+=d[i]*i 
        return add
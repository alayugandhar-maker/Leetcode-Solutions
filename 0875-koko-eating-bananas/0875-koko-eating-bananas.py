class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        m=max(piles)
        n=len(piles)
        low,high=1,m
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            time=fun(piles,mid,n)
            if time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
def fun(piles,mid,n):
    total=0
    for i in range(len(piles)):
        total+=(piles[i]+mid-1)//mid
    return total
        



        
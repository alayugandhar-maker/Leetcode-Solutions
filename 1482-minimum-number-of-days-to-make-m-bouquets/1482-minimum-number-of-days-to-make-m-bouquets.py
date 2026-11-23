class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n<m*k:
            return -1
        low,high=min(bloomDay),max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if possible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
def possible(bloomDay,mid,m,k):
    cnt=0
    no=0
    for i in range(len(bloomDay)):
        if bloomDay[i]<=mid:
            cnt+=1
        else:
            no+=(cnt//k)
            cnt=0
    no+=(cnt//k)
    if no>=m:
        return True
    else:
        return False
                
        
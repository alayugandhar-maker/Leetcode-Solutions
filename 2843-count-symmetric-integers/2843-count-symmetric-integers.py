class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            s=str(i)
            l=len(s)
            if l%2==0:
                l1=list(map(int,s))
                if sum(l1[0:l//2])==sum(l1[l//2:]):
                    count+=1
        return count

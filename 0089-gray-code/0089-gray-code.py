class Solution:
    def grayCode(self, n: int) -> list[int]:
        #ans=0
        lst=[]
        for i in range(0,2**n):
            ans=i^(i>>1)
            lst.append(ans)
        return lst

        
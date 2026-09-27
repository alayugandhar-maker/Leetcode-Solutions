class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n=len(s)
        s1=[0]*(n)
        for i in range(0,n):
            s1[indices[i]]=s[i]

               
        return ''.join(s1)
        
        
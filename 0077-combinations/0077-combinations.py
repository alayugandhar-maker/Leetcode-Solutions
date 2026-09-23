class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        lst=[]
        ans=[]
        for i in range(1,n+1):
            lst.append(i)
        back(0,[],lst,ans,k)
         
        return ans

def back(start,path,lst,ans,k):
    if len(path)==k:
        ans.append(path.copy())
        return 
    for i in range(start,len(lst)):
        path.append(lst[i])

        back(i+1,path,lst,ans,k)

        path.pop()
        
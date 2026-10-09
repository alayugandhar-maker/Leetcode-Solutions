class Solution:
    def totalNumbers(self, nums: List[int]) -> int:
        count=set()
        ans=[]
        lst=[]
        n=len(nums)
        freq=[0]*(n)
        select(ans,lst,nums,n,freq)
        for i in ans:
           if i[0]!=0 and i[2]%2==0:
            count.add(tuple(i))
        return len(count)

def select(ans,lst,nums,n,freq):
    if len(lst)==3:
        ans.append(lst.copy())
        return 
    for i in range(n):
        if freq[i]==0:
            freq[i]=1
            lst.append(nums[i])
            select(ans,lst,nums,n,freq)
            lst.pop()
            freq[i]=0
        
class Solution:
    def maximumWealth(self, acc: List[List[int]]) -> int:
        lst=[]
        for i in range(0,len(acc)):
            s=0
            for j in range(0,len(acc[i])):
                s+=acc[i][j]
            lst.append(s)
        return max(lst)
        
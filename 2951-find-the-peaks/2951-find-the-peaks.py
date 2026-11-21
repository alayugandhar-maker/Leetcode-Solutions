class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n=len(mountain)
        lst=[]
        for i in range(1,n-1):
            if mountain[i-1]<mountain[i]>mountain[i+1]:
                lst.append(i)
        return lst
        
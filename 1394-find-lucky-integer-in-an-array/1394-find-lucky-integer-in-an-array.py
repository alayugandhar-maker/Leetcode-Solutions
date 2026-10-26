class Solution:
    def findLucky(self, arr: list[int]) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        count=0
        for i in d:
            if i==d[i]:
                count=max(count,i)
        if count:
            return count
        return -1

        
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        l,r=0,0
        maxlen=0
        d={}

        while r<n:
            d[fruits[r]]=d.get(fruits[r],0)+1
            if len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1 
            #else:
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        
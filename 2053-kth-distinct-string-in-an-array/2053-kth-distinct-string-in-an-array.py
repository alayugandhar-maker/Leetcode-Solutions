class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d={}
        for ch in arr:
            d[ch]=d.get(ch,0)+1 
        count=0
        for i in d:
            if d[i]==1:
                count+=1
                if count==k:
                    return i
        return ""


        
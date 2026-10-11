class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        lst=[]
        for val in d.values():
            lst.append(val)
        for i in range(len(lst)-1):
            if lst[i]!=lst[i+1]:
                return False
        return True
       
        
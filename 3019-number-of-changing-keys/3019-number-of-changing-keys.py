class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        #print(s)
        count=0
        n=len(s)
        i=0
        while i<n-1:
            if s[i]!=s[i+1]:
                count+=1
            i+=1 
        return count
        
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        cnt=0
        lastseen=[-1]*3
        for i in range(0,n):
            lastseen[ord(s[i])-ord('a')]=i;
            if lastseen[0]!=-1 and lastseen[1]!=-1 and lastseen[2]!=-1 :
                cnt=cnt+(1+min(lastseen[0],lastseen[1],lastseen[2]))
        return cnt
        
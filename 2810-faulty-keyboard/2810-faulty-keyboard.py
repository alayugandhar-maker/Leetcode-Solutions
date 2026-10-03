class Solution:
    def finalString(self, s: str) -> str:
        s1=''
        for ch in s:
            if ch=='i':
                s1=s1[::-1] 
            elif ch!='i':
                s1+=ch
        return s1
        
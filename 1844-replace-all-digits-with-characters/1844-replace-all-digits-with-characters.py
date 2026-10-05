class Solution:
    def replaceDigits(self, s: str) -> str:
        a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'] 
        lst=list(s)
        for i in range(0,len(lst)):
            if lst[i] not in a:
                ind=int(lst[i])
                ans=a.index(lst[i-1])
                lst[i]=a[ind+ans]
        return ''.join(lst)

        
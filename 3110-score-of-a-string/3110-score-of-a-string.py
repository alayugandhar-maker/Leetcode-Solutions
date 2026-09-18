class Solution:
    def scoreOfString(self, s: str) -> int:
        add=0
        lst=[]
        for i in s:
            lst.append(ord(i))
        #print(lst) 
        for i in range(0,len(lst)-1):
            add+=(abs(lst[i]-lst[i+1]))
        return add

        
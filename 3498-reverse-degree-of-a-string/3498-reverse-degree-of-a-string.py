class Solution:
    def reverseDegree(self, s: str) -> int:
        lst=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        add=0
        for i in range(0,len(s)):
            add=add+((lst.index(s[i])+1)*(i+1))
        return add
        


        
class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower() 
        ans=""
        for i in s:
            if 'A'<=i<='Z':
                ans+=chr(ord(i)+32)
            #print(ans) 
            else:
                ans+=i 
        return ans      
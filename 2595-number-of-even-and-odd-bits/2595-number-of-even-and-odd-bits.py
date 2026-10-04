class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        bi=bin(n)[2:]
        bi1=bi[::-1]
        odd=0
        even=0
        for i in range(0,len(bi1)):
            if bi1[i]=='1' and i%2==0:
                even+=1
            elif bi1[i]=='1' and i%2==1:
                odd+=1
        return [even,odd]

       
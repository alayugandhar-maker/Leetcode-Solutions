class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            if i<10 and i==digit:
                count+=1 
            else:
                while i>0:
                    d=i%10 
                    if d==digit:
                        count+=1 
                    i//=10
        return count
                

        
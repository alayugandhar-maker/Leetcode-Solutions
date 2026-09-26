class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in nums:
            if i>=10:
                s=str(i)
                lst1=list(map(int,s))
                lst+=lst1 
            else:
                lst.append(i)
        return lst

        
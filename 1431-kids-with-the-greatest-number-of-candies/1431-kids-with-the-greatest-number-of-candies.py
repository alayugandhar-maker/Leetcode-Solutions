class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst=[]
        m1=max(candies)

        for i in candies:
            if i+extraCandies>=m1:
                lst.append(True)
            else:
                lst.append(False)
        return lst
        
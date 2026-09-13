class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], box: List[int]) -> int:
        n=len(box)
        count=0
        for fruit in fruits:
            for j in range(n):
                if box[j]>=fruit:
                    box[j]=0
                    break 
            else:
                count+=1
        return count
        
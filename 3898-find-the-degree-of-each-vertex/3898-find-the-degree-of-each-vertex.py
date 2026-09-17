class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        lst=[]

        for i in range(0,n):
            count=0
            for j in range(0,n):
                if matrix[i][j]==1:
                    count+=1 
            lst.append(count)
        return lst
            
        
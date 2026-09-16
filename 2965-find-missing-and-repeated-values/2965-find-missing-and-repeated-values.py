class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        lst=[]
        for i in range(0,n):
            for j in range(n):
                lst.append(grid[i][j])
        lst1=[]
        for i in range(1,n*n+1):
            if lst.count(i)==2:
               lst1.append(i)
        for i in range(1,n*n+1):
            if i not in lst:
              lst1.append(i)
        return lst1
        
            

        
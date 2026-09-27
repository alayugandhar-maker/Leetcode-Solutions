class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mintime=float('inf')
        n=len(tasks)
        for i in range(0,n):
            ans=0
            for j in range(len(tasks[i])):
                ans+=tasks[i][j] 
            mintime=min(ans,mintime)
        return mintime
                

        
        
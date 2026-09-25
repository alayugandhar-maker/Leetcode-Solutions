class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mindiff=float('inf') 
        for i in range(0,len(arr)-1):
            mindiff=min(mindiff,arr[i+1]-arr[i])
        #print(mindiff)
        n=len(arr)
        lst=[]
        for i in range(0,n-1):
            if arr[i+1]-arr[i]==mindiff:
                lst.append([arr[i],arr[i+1]])
        return lst
        
        
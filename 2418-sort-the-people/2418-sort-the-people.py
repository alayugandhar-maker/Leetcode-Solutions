class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        d={}
        lst=[]
        for i in range(n):
            d[heights[i]]=names[i] 
        #print(d)
        for i in d:
            lst.append(i)
        lst.sort()
        lst1=[]
        for i in range(len(lst)-1,-1,-1):
            lst1.append(d[lst[i]])
        return lst1


        

        
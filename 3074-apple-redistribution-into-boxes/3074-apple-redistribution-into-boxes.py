class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n=len(capacity)
        capacity.sort()
        add=sum(apple)
        count=0

        for i in range(n-1,-1,-1):
            add-=capacity[i]
            count+=1 
            if add<=0:
                return count
            

        
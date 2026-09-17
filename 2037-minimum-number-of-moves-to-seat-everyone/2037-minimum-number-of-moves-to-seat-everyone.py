class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n=len(seats)
        count=0
        for i in range(n):
            count+=abs(students[i]-seats[i])
        return count

        
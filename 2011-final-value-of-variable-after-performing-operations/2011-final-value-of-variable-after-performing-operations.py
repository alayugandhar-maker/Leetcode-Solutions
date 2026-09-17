class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        add=0
        for i in operations:
            if '+' in i:
                add+=1
            else:
                add-=1
        return add

        
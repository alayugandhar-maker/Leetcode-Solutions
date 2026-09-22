class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n=len(encoded)
        arr=[0]*(n+1)
        arr[0]=first

        for i in range(0,len(encoded)):
            arr[i+1]=encoded[i]^arr[i]
        return arr
        
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        st=''
        generate(0,0,ans,st,n)
        return ans

def generate(op,cl,ans,st,n):
    if op==cl==n:
        ans.append(st)
        return 
    if op<n:
        generate(op+1,cl,ans,st+'(',n)
    if cl<op:
        generate(op,cl+1,ans,st+')',n)

        
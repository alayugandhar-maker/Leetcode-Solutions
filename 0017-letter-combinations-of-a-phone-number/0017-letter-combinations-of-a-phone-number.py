class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans=[]
        lst=[]
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        back(0,digits,ans,lst,d)
        return ans

def back(idx,digits,ans,lst,d):
    if idx==len(digits):
        ans.append(''.join(lst.copy()))
        return 
    
    digit=d[digits[idx]]

    for i in range(0,len(digit)):
        lst.append(digit[i])

        back(idx+1,digits,ans,lst,d)
        lst.pop()




        
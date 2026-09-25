class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        s=paragraph.lower().split()
        lst=[]
        for word in s:
            for ch in string.punctuation:
                word = word.replace(ch, " ")
            lst.extend(word.split())
        #print(lst)
        d={}
        for word in lst:
            d[word]=d.get(word,0)+1 
        
        ans=''
        max_count=0 

        for word in d:
            if word not in banned and d[word]>max_count:
                max_count=d[word]
                ans=word 
        return ans


        
def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        A,B = len(word1), len(word2)
        i,j=0,0
        while i<= (A-1) or j<= (B-1):
            if i<= (A-1):
                result+=word1[i]
                i+=1
            if j<= (B-1):
                result+=word2[j]
                j+=1
        return result
        
        
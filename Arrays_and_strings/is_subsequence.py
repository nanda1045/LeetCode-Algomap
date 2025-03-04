def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        while i<=len(s)-1 and j<=len(t)-1:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
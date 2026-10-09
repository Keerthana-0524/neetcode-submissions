class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s))!=len(t):
            return False
        checked_char=[]
        for char in s:
            if char in checked_char:
                continue
            count1=0
            count2=0
            for c in s:
                if c==char:
                    count1+=1
            for c1 in t:
                if c1==char:
                    count2+=1
            if count1!=count2:
                return False
            checked_char.append(char)
        return True
        
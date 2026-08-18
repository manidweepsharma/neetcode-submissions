class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        str1=[0]*26
        str2=[0]*26
        for c in s:
            str1[ord(c)-ord('a')] += 1
        for c in t:
            str2[ord(c)-ord('a')] += 1
        if str1 == str2:
            return True
        else:
            return False

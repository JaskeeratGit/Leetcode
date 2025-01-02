class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharDict = {}
        tCharDict = {}
        if len(s) != len(t):
            return False
        else:
            for i,j in zip(s,t):
                if i in sCharDict:
                    sCharDict[i] += 1
                else:
                    sCharDict[i] = 1
                if j in tCharDict:
                    tCharDict[j] += 1
                else:
                    tCharDict[j] = 1
            if sCharDict == tCharDict:
                return True
            else:
                return False

                
                

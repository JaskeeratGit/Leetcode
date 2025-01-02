class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         countDict = {}
         for i in nums:
            if i in countDict:
                return True
            else:
                countDict[i] = 1
         return False
        
        

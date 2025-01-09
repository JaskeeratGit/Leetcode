class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        l2 = []
        for i in numSet:
            length = 1
            if not(i-1 in numSet):
                while i+1 in numSet:
                    length += 1
                    i+=1
                l2.append(length)

        if not l2:
            return 0
        else:
            return max(l2) 

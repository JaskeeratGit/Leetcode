class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdx = {}
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in numIdx:
                if numIdx[needed_num] < i:
                    return [numIdx[needed_num], i]
                else:
                    return [i, numIdx[needed_num]]
            numIdx[nums[i]] = i
        
        return []

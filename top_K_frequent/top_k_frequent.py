class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        freqArray = []
        for i in range(len(nums)):
            if nums[i] in freqDict:
                freqDict[nums[i]] += 1
            else:
                freqDict[nums[i]] = 1
        for key,value in freqDict.items():
            freqArray.append([value,key])
        freqArray.sort(reverse = True)
        output = []
        for pair in range(k):
            output.append(freqArray[pair][1])
        return output

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        sum1 = numbers[i] + numbers[j]
        while sum1 != target:
            if sum1<target:
                sum1 = numbers[i+1] + numbers[j]
                i += 1
            elif sum1>target:
                sum1 = numbers[i] + numbers[j-1]
                j -=1
        return[i+1,j+1]

                  

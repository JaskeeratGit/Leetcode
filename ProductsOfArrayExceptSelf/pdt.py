class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdtWithZero = 1
        pdtWithoutZero = 1
        multipleZeroes = False
        output = []
        count = 0
        for i in nums:
            if i != 0:
                pdtWithoutZero = pdtWithoutZero*i
            else:
                count += 1
            pdtWithZero = pdtWithZero*i
        for i in nums:
            if i != 0:
                output.append(pdtWithZero//i)
            elif (i == 0 and count < 2):
                output.append(pdtWithoutZero)
            else:
                output.append(pdtWithZero)
        return output
        

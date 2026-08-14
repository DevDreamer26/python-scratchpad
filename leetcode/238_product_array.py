from typing import List #Just for vsc not needed in LC, lol 🎩

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix =1 

        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

        # Brute force method
        # output = []

        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output.append(product)
        # return output
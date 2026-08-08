from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        got_it = {}

        for i in range(len(nums)):
            num = nums[i]
            need = target - num
            if need in got_it:
                return [got_it[need],i]
            else:  
                got_it[num] = i
        return []
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        absolute_max = 0
        curr_max = 0
        for n in nums:
            if n == 1:
                curr_max += 1
            else:
                curr_max = 0
            if curr_max > absolute_max:
                absolute_max = curr_max
        return absolute_max
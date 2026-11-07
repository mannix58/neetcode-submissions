class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i,n in enumerate(nums):
            right_sum = total - n - left_sum
            if right_sum == left_sum:
                return i
            left_sum += n
        return -1
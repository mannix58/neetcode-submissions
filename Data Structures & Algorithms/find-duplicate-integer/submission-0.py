class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        for n in nums:
            if n in seen:
                return n
            else:
                seen.append(n)
        return None
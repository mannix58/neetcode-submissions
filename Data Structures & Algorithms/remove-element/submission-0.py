class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for n in nums:
            if n == val:
                continue
            tmp.append(n)
        for i in range(len(nums)):
            nums[i] = tmp[i] if i < len(tmp) else "_"
        return len(tmp)
            

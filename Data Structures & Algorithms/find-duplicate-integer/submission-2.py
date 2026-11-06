class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's algo
        slow, fast = 0,0

        while True:
            slow = nums[slow] # advance by 1
            fast = nums[nums[fast]] #advance by 2 pointers
            if slow == fast: # once they intersect, break
                break
        
        slow2 = 0
        while True: 
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
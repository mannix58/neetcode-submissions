# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        head: Optional[ListNode]

        if list1 is None: return list2
        if list2 is None: return list1

        if curr1.val <= curr2.val:
            head = curr1
            tail = head
            curr1 = curr1.next
        else:
            head = curr2
            tail = head
            curr2 = curr2.next

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            else:

                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next
        if curr1 is not None:
            tail.next = curr1
        if curr2 is not None:
            tail.next = curr2
    
            
        return head
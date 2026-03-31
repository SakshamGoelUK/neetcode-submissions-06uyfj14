# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head:
            head.visited = True
            head = head.next
            if hasattr(head,'visited'):
                return True
        return False
            
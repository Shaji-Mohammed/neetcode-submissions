# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode(next=head)
        lead, trail = dummy, dummy

        for _ in range(n):
            lead = lead.next

        while lead.next:
            trail = trail.next
            lead = lead.next

        temp = trail.next
        trail.next = trail.next.next
        temp.next = None

        return dummy.next 


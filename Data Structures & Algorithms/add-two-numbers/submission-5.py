# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ln1, ln2 = len(l1), len(l2)

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 and l2:
            node = ListNode(l1.val + l2.val + carry)
            cur.next = node
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

            carry = 0
            if node.val > 9:
                node.val = node.val - 10
                carry = 1
        
        while l1:
            node = ListNode(l1.val + carry)
            cur.next = node
            l1 = l1.next
            cur = cur.next
            carry = 0
            if node.val > 9:
                node.val = node.val - 10
                carry = 1

        while l2:
            node = ListNode(l2.val + carry)
            cur.next = node
            l2 = l2.next
            cur = cur.next
            carry = 0
            if node.val > 9:
                node.val = node.val - 10
                carry = 1


        if carry:
            node = ListNode(1)
            cur.next = node
        
        return dummy.next

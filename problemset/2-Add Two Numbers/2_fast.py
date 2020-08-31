class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newNode = ListNode(0)
        carry = 0
        headd = newNode
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            val = x + y + carry
            carry = val//10
            newNode.next = ListNode(val%10)
            newNode = newNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry == 1:
            newNode.next = ListNode(carry)
        
        return headd.next
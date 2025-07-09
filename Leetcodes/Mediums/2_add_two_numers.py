# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode()
        dummy = prev

        carry = 0
        while l1 or l2:
            num1 = -1
            num2 = -1
            if l1: num1 = l1.val
            if l2: num2 = l2.val

            if num1 != -1 and num2 != -1: total = num1 + num2 + carry
            elif num1 != -1: total = num1 + carry
            else: total = num2 + carry

            carry = total // 10 #get the carry (// does integer division)
            num = total % 10 #get the num 

            nxt = ListNode(num)
            prev.next = nxt
            prev = nxt

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry != 0: #if we have a carry remainder then take care of that as well
            nxt = ListNode(carry)
            prev.next = nxt
            prev = nxt
            
        return dummy.next


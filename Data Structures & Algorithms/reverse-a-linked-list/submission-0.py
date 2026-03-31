# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
                return head

        if head.next.next is None:
                new_head = head.next
                new_head.next = head
                head.next = None
                return new_head        

        prev = head
        curr = head.next
        _next = head.next.next
        prev.next = None

        while(_next is not None):
                print(prev.val,curr.val,_next.val)
                curr.next = prev
                print(curr.val,curr.next.val)
                prev = curr
                curr = _next
                _next = curr.next 

        
        curr.next = prev

        return curr               
        
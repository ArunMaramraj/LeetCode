# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        s = head
        f = head
        
        while n!=0:
            f = f.next
            n-=1
            
        if f==None:
            return head.next
        
        while f.next!=None:
            f = f.next
            s= s.next
        
        s.next = s.next.next
        
        return dummy.next
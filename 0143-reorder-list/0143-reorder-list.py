# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
        
        
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverseList(head):        
            one = None
            two = head

            while two!= None:
                temp = two.next
                two.next=one
                one = two
                two = temp
            return one
       
        slow= head
        fast = head.next
        
        while(fast!=None and fast.next!=None):
            slow= slow.next
            fast = fast.next.next
            
        head2 = slow.next
        
        slow.next= None
        
        head2= reverseList(head2)
        head1= head
        dummy = head1
        temp1 = head1
        temp2 = head2
        
        while(head1.next!=None and head2!=None):
            temp1=head1.next
            temp2=head2.next
            head2.next=None
            head1.next=head2
            head2.next=temp1
            head1=head2.next
            head2=temp2
            
        head1.next=head2
         
        return dummy
    
    
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        pointer = head
        while(list1!=None and list2!=None ):
            if(list1.val<=list2.val):
                temp = list1
                list1= list1.next
            else:
                temp= list2
                list2=list2.next
            
            if(head==None):
                head = temp
                pointer= temp
                head.next=None
            else:
                pointer.next = temp
                pointer=pointer.next
                pointer.next = None
                
        if list1!=None:
            if pointer!=None:
                pointer.next=list1
            else:
                head=list1
            
            
        elif list2!=None:
            if pointer!=None:
                pointer.next=list2
            else:
                head=list2
            
        
        
        return head
               
                
        
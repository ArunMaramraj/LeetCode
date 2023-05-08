# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        dic = {0:dummy}

        pre = 0

        while head:
            pre += head.val
            dic[pre] = head
            head= head.next

        pre = 0
        head = dummy

        while head:
            pre = pre + head.val
            head.next = dic[pre].next
            head = head.next
        return dummy.next        


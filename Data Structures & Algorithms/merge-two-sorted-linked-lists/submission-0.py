# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        head = list1 if list1.val < list2.val else list2
        l=list1
        r=list2
        curr = head
        while l or r:
            if not l:
                curr.next = r
                return head
            if not r:
                curr.next = l
                return head
            else:
                if l.val < r.val:
                    temp = l.next
                    curr.next = l
                    curr = l
                    l = temp
                else:
                    temp = r.next
                    curr.next = r
                    curr = r
                    r = temp
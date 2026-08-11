# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """


        d=ListNode(0)
        d.next=head
        p=d

        for _ in range(left-1):
            p=p.next
        c=p.next

        for _ in range(right-left):
            t=c.next
            c.next=t.next
            t.next=p.next
            p.next=t

        return d.next

      
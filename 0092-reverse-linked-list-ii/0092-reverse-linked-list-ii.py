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

        v=[]
        c=head
        while c:
            v.append(c.val)
            c=c.next
        
        v[left-1:right]=v[left-1:right][::-1]
        
        c=head
        i=0

        while c:
            c.val=v[i]
            c=c.next
            i+=1
        return head





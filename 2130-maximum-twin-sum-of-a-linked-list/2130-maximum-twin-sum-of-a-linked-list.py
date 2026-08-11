# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        v=[]

        while head:
            v.append(head.val)
            head=head.next

        l=0
        r=len(v)-1
        m=0

        while(l<r):
            m=max(m, v[l]+v[r])
            l+=1
            r-=1
        return m
        
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        s = []
        c = head

        while c:
            while s and s[-1].val < c.val:
                s.pop()

            s.append(c)
            c = c.next

        d = ListNode(0)
        ca = d

        for i in s:
            ca.next = i
            ca = ca.next

        ca.next = None

        return d.next
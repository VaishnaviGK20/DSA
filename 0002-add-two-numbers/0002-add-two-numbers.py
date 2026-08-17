class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            s = a + b + carry

            curr.next = ListNode(s % 10)
            carry = s // 10

            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
class Solution(object): 
    def addTwoNumbers(self, l1, l2): 
        v1 = []
        v2 = []
        r = []

        while l1:
            v1.append(l1.val)
            l1 = l1.next

        while l2:
            v2.append(l2.val)
            l2 = l2.next

        carry = 0

        for i in range(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0

            s = a + b + carry
            r.append(s % 10)
            carry = s // 10

        if carry:
            r.append(carry)

        d = ListNode(0)
        c = d

        for i in r:
            c.next = ListNode(i)
            c = c.next

        return d.next
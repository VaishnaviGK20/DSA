class Solution(object): 
    def addTwoNumbers(self, l1, l2): 
        d=ListNode(0)
        c=d
        ca=0

        while l1 or l2 or ca:
            a = l1.val if l1 else 0
            b= l2.val if l2 else 0

            s=a+b+ca
            c.next=ListNode(s%10)
            ca=s//10

            c=c.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return d.next


        
 
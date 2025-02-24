# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0, head)

        groupPrev = dummy 

        if not head:
            return None
        

        while True: 
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse groups 
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                
                prev = curr
                curr = tmp 
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
    

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None
        
        N = 0  # store linkedlist length

        # get length of linkedlist
        curr = head
        while curr:  
            N +=1
            curr = curr.next

        count = 0
        curr = head
        prev = None
    
        while (N-count) >= k: # continue until right nodes are less than k

            count += k
            start = curr # keep track of starting of sub linked list before reversing
            for _ in range(k):

                nextnode = curr.next
                curr.next = prev

                prev = curr
                curr = nextnode

            if count == k:
                beginning = prev

            if count > k:
                l1.next = prev
                
            if curr:
                l1 = start
                start.next = curr
                prev = None
            
        return beginning



##### METHOD USING HELPER FUNCTION #####

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None
        
        N = 0  # store linkedlist length

        # get length of linkedlist
        curr = head
        while curr:  
            N +=1
            curr = curr.next

        count = 0
        curr = head
        prev = None
    
        while (N-count) >= k: # continue until right nodes are less than k

            count += k
            start = curr # keep track of starting of sub linked list before reversing

            # Use helper function to reverse k nodes
            prev, curr = self.reverselist(curr, k)

            if count == k:
                beginning = prev

            if count > k:
                l1.next = prev
                
            if curr:
                l1 = start
                start.next = curr
                prev = None
            
        return beginning

    def reverselist(self, curr, k):
        prev = None
        for _ in range(k):
            nextnode = curr.next
            curr.next = prev

            prev = curr
            curr = nextnode

        return prev, curr
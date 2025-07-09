# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #keep a hashmap of the nodes
        hashmap = {}

        #dont need a hash map just keep the node as a tuple in the minheap
        minheap = []
        dummy = ListNode()
        head = dummy

        #prepush each first value in minheap
        for i in range(len(lists)):
            if not lists[i]: continue
            heapq.heappush(minheap, (lists[i].val, i))
            hashmap[i] = lists[i]
        
        while minheap:
            val, i = heapq.heappop(minheap)
            node = hashmap[i]

            head.next = ListNode(val)
            head = head.next

            #if we have another node then add that
            node = node.next
            if node != None:
                hashmap[i] = node
                heapq.heappush(minheap, (node.val, i))
        
        return dummy.next


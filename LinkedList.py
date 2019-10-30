class Node():
    def __init__(self,prev=None,next=None,val=None):
        self.prev=prev
        self.next=next
        self.val=val

class LinkedList():
    def __init__(self):
        #self.length=0
        self.head=Node()
        self.tail=Node(prev=self.head)
        self.head.next=self.tail
    
    def delete(self,Node):
        cur=self.head
        while cur!=self.tail:
            if cur==Node:
                cur.prev.next=cur.next
                cur.next.prev=cur.prev
                return cur
            cur=cur.next    
        return -1
    
    #if true it returns the node
    def contains(self,v):
        cur=self.head.next
        while cur!=self.tail:
            if cur.val[1]==v:
                return cur
        return False

    #add to the right of prev_node
    def add(self,node,prev_node):
        node.next=prev_node.next
        node.prev=prev_node
        prev_node.next=node
        node.next.prev=node


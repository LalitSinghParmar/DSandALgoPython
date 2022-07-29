#Structure of single node

class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printLinkedList(self)->None:
        temp = self.head
        while temp:
            print(temp.data, end='->', sep='')
            temp = temp.next
        print('None')

    def addAtHead(self,data:int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addAtLast(self,data:int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node

    def addAtIndex(self, index:int, data:int) -> None:
        temp = self.head
        new_node = Node(data)
        cnt = 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return 
        while cnt<index-1 and temp:
            cnt += 1
            temp = temp.next
        if temp:
            new_node.next = temp.next
            temp.next = new_node

    def addAtIndex_rec(self, head:Node , index:int, data:int) -> Node:
        if head is None and index>0:
            return head
        if index == 0:
            new_node = Node(data)
            new_node.next = head
            head = new_node
            return head
        new_head = self.addAtIndex_rec(head.next, index-1, data)
        head.next = new_head
        return head

    def length_rec(self, temp:Node) -> int:
        if temp is None:
            return 0
        return 1+self.length_rec(temp.next)

    def deleteAtIndex(self,index:int) -> None:
        temp = self.head
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
        cnt = 0
        while cnt<index-1 and temp:
            temp = temp.next
            cnt += 1
        if temp:
            temp.next = temp.next.next


    def deleteAtIndex_rec(self, head:Node, index:int) ->None:
        temp = head
        if head is None and index>=0:
            return head
        if index == 0:
            head = head.next
            temp.next = None
            return head
        new_head = self.deleteAtIndex_rec(head.next, index-1)
        head.next = new_head
        return head
        



ll = LinkedList()
ll.addAtHead(1)  #1->None
ll.addAtLast(3)  #1->3->None
ll.addAtIndex(1,2) #1->2->3->None
ll.addAtIndex(0,0) #0->1->2->3->None
ll.addAtIndex(4,4) #0->1->2->3->4->None
ll.addAtIndex(10,5) #0->1->2->3->4->None
ll.printLinkedList()  #0->1->2->3->4->None

ll.head =ll.addAtIndex_rec(ll.head,0,5)  #5->0->1->2->3->4->None
ll.printLinkedList()  #5->0->1->2->3->4->None
ll.head =ll.addAtIndex_rec(ll.head,0,3) #3->5->0->1->2->3->4->None
ll.head =ll.addAtIndex_rec(ll.head,1,2) #3->2->5->0->1->2->3->4->None
ll.head =ll.addAtIndex_rec(ll.head,3,4) #3->2->5->4->0->1->2->3->4->None
ll.head =ll.addAtIndex_rec(ll.head,10,10) #3->2->5->4->0->1->2->3->4->None
ll.printLinkedList() #3->2->5->4->0->1->2->3->4->None
print(ll.length_rec(ll.head)) #9
ll.deleteAtIndex(0) #2->5->4->0->1->2->3->4->None
ll.deleteAtIndex(7) #2->5->4->0->1->2->3->None
ll.deleteAtIndex(3) #2->5->4->1->2->3->None
ll.deleteAtIndex(7) #2->5->4->1->2->3->None
ll.printLinkedList() #2->5->4->1->2->3->None
print(ll.length_rec(ll.head)) #6

ll.head =ll.deleteAtIndex_rec(ll.head, 0) #5->4->1->2->3->None
ll.head =ll.deleteAtIndex_rec(ll.head, 3) #5->4->1->3->None
ll.head =ll.deleteAtIndex_rec(ll.head, 3) #5->4->1->None
ll.head = ll.deleteAtIndex_rec(ll.head, 7) #5->4->1->None
ll.printLinkedList() #5->4->1->None
print(ll.length_rec(ll.head)) #3
print('------------------------------------------------')
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# while head:
#     print(head.data)
#     head = head.next
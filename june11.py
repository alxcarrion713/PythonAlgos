class Node:
    def_init_(self,value)
        self.value= value
        self.next= NotImplemented

class SLL:
    def_init_(self):
        self.head=None

    def addfront(self,value):

        if self.head==None:
            newnode=Node(value)
            self.head= newnode
        else:
            newnode= Node(value)
            newnode.next=self.head
            self.head=newnode
        return self

    def display(self):
        runner=self.head
        while runner!= None:
            print (runner.value)
            runner=runner.next
        print(count)

    def addback(self,value):
        newnode=Node(value)
        runner=self.head
        while runner.next != None:
            runner=runner.next
        runner.next=newnode
        return self

sll1=SLL()
sll1.addfront(5).addfront(6).addfront(8).addback(12).display()

    def moveintofront(sllinput):
        runner=self.head
        return sllinput

    def removeLastNode(head): 
    if head == None: 
        return None
    if head.next == None: 
        head = None
        return None
    second_last = head 
    while(second_last.next.next): 
        second_last = second_last.next
    second_last.next = None
    return head 
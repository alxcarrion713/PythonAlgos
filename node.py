# Sam thinks Tad might be somewhere in a very long line waiting to attend the Superman movie. Given a ListNode pointer and a val, return whether val is found in any node in the list”
# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def addfront(self, valueInput):
        #createNewNode
        newnode = Node(valueInput)
        newnode.next = self.head
        self.head = newnode
        return self

    def display(self):
        runner = self.head
        print(runner)
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    



    # def removefront(self):
    #     #your code here

sll1 = SLL()
sll1.addfront(5).addfront(8).addfront(15).display()
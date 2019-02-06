# import sys
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None 
        self.next = None
class DLists:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.size = 0

    def add_node_front(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
            return self
        self.head.prev = node
        node.next = self.head
        self.head = node
        return self
    def add_node_back(self,node):
        if self.tail == None:
            self.head = node
            self.tail = node
            return self
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return self

    def print_values(self):
        if self.head == None:
            print("This is a empty list!")
            return self
        runner = self.head
        while (runner != None):
            print("value is:", runner.val)
            runner = runner.next
        return self

    def delete_node_by_val(self,val):
        if self.head == None:
            print("This is a empty list")
            return False
        if (self.head.val == val):
            if (self.head == self.tail):  # only have one node and node.val = val
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next #need to delete first node 
            return self
        elif (self.head == self.tail):
            print("Can not find appropriate node")
            return False
        runner = self.head.next
        while ((runner.val != val) and (runner != self.tail)):
            runner = runner.next
        if (runner.val == val):
            runner.prev.next = runner.next
            runner.next.prev = runner.prev
        else:
            print("Can not find any node has this value.")
            return False
        return self
    
    def insert_at(self, val, n):
        if n == 0:
            self.add_node_front(Node(val))
            return self
        if self.head == None:
            print("This is a empty list.")
            return False
        runner = self.head
        position = 1
        while (position != n and runner != self.tail):
            runner = runner.next
            position += 1
        if ((position == n) and (runner == self.tail)):
            self.add_node_back(Node(val))
        elif((position == n) and (runner != self.tail)):
            new_node = Node(val)
            new_node.next = runner.next
            runner.next.prev = new_node
            new_node.prev = runner
            runner.next = new_node
            print("insered...")
            return self
        else:
            print("Can not find the appropriate position")
            return False
    def is_circular(self):
        if ((self.head.prev != None) or(self.tail.next != None)):
            return True
        runner = self.head.next
        while ((runner != None) and (runner!=self.tail)):
            if ((runner.next.prev != runner) or (runner.prev.next != runner)):
                return True
            runner = runner.next
        return False 
    def find_middle(self):
        runner_head = self.head
        runner_tail = self.tail
        middle_nodes = []
        while ((runner_head != runner_tail) and (runner_head.next != runner_tail)):
            runner_head = runner_head.next
            runner_tail = runner_tail.prev
        middle_nodes = [runner_head,runner_tail]
        return middle_nodes
    def reverse_dlist(self):
        new_node = Node(0)
        runner = self.head
        while runner != None :
            new_node.prev = runner.prev
            new_node.next = runner.next
            runner.prev = new_node.next
            runner.next = new_node.prev
            runner = new_node.next
        new_node = self.head
        self.head = self.tail
        self.tail = new_node
        return self


    
myDList = DLists()
# myDList.print_values()
myNode = Node(5)
myNode1 = Node(9)
myDList.add_node_back(myNode).add_node_front(Node(4)).add_node_back(Node(3)).add_node_front(myNode1).add_node_back(Node(7))
# myDList.head = myNode
# print("before delete")
# myDList.print_values()
# myDList.delete_node_by_val(4)
# print("after delete")
# myDList.print_values()
# print("before insert")
# myDList.print_values()
# myDList.insert_at(6,4)
# print("after insert")
myDList.print_values()
# print(myDList.is_circular())
# print(myDList.find_middle()[0].val)
# print(myDList.find_middle()[1].val)
myDList.reverse_dlist()
print("after revere")
myDList.print_values()



import sys

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def print_values(self):
        if self.head ==None:
            print("This is a empty list!")
            return self
        runner = self.head
        while (runner!= None):
            print("value is:",runner.val)
            runner = runner.next
        return self
    def add_to_back(self,val):
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        new_node = Node(val)
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head == None :
            return False
        # runner = self.head.next
        r_val = self.head.val
        self.head = self.head.next
        return r_val
    def remove_from_back(self):
        if self.head == None:
            return False
        
        runner = self.head.next
        prior = self.head

        while (prior.next != None and runner.next != None):
            prior = prior.next 
            runner = runner.next
        prior.next = None
        return self
    
    def remove_val(self,val):
        if self.head == None:
            print("This is a empty list")
            return False
        if (self.head.val == val):
            self.head = self.head.next
            return self 
        elif (self.head.next == None):
            print("Can not find appropriate node")
            return False

        prior = self.head
        runner =self.head.next
        while ((runner.val != val) and (runner.next != None)):
            prior = prior.next
            runner = runner.next
        if (runner.val == val):
            prior.next = runner.next
        else:
            print("Can not find any node has this value.")
            return False
        return self
    

    def insert_at(self,val,n):
        if n == 0 :
            self.add_to_front(val)
            return self
        if self.head == None:
            print("This is a empty list.")
            return False
        runner = self.head
        position = 1
        while (position != n and runner.next != None):
            runner = runner.next
            position +=1
        if (position == n):
            new_node = Node(val)
            new_node.next = runner.next
            runner.next = new_node
            print("insered...")
            return self
        else:
            print("Can not find the appropriate position")
            return False
    
        




        




# newHead = Node(3)    
# newSList = SList()
# newSList.head = newHead
# newSList.add_to_front(5)
# newSList.add_to_back(6)
# newSList.add_to_back(7)
# newSList.print_values()
# print(newSList.remove_from_front())
# print("After delete from front")
# newSList.print_values()
# newSList.remove_from_back()
# print("After delete from front")
# # newSList.print_values()
# print("Befor delete")
# newSList.print_values()
# newSList.remove_val(5)
# print("After delete")
# newSList.print_values()
# # newSList.remove_val(8)
# print("Before insert")
# newSList.print_values()
# newSList.insert_at(8,5)
# print("after insert")
# newSList.print_values()


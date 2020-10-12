from pythonisms.decorators.decorators import slow_down ,spent
import time

class Node():
    def __init__(self,value):
        """
        this is the initial method for class Node,
        it has two attributes:
        1- the value: it contents the value of node.
        2- the next: it contents the next's node.
        """
        try:
            self.value=value
            self.next=None

        except Exception as error:
            print (f"There is error in __init__ of Node, the error {error}")

class LinkedList():

    def __init__(self,collection=None):

        """
        This is the initial method of LinkedList,
        it has only one attribute, which is head.
        the head is a reference to the first node always.
        """
        try:
            self.head=None
            if collection:
                for item in reversed(collection):
                    self.insert(item) 

        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    @spent
    def insert(self,value):

        """
        This is inserting method of LinkedList,
        functionality of this method to insert a new
        node on LinkedList.
        """
        try:
            new_node=Node(value)
            if self.head == None:
                self.head=new_node
            else:
                current=self.head
                while current.next:
                    current=current.next
                current.next=new_node
            print( new_node.value)
            return( new_node.value)
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def __iter__(self):
        """
        This method to loop over all nodes of LinkedList.
        """
        def items():
            try:
                current = self.head
                while current:
                    yield current.value
                    current = current.next
            except Exception as error:
                print (f"There is error in __iter__ of LinkedList, the error {error}")
        return items()

    def __str__(self):
        """
        This method to return all nodes of LinkedList as a string.
        """
        try:
            out = ""
            for value in self:
                out += f"[ {value} ] -> "
            return out + "None"
        except Exception as error:
            print (f"There is error in __str__ of LinkedList, the error {error}")
    
    def __len__(self):
        """
        This method to return length of LinkedList
        """
        try:
            return len(list(iter(self)))
        except Exception as error:
            print (f"There is error in __len__ of LinkedList, the error {error}")

    @slow_down
    def __eq__(self, other):
        """
        This method to compare between two linked list,
        if they equal return True, if not return False. 
        """
        try:
            return list(iter(self)) == list(iter(other))
        except Exception as error:
            print (f"There is error in __eq__ of LinkedList, the error {error}")
        
    
    def __getitem__(self, index):
        """
        This method to return the value of node by  index.
        """
        try:
            if index < 0:
                index = len(self) + index

            for i, item in enumerate(self):
                if i == index:
                    return item
            raise IndexError
        except Exception as error:
            print (f"There is error in __getitem__ of LinkedList, the error {error}")


if __name__=="__main__":
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    list2= LinkedList()
    list2.insert(120)
    list2.insert(50)
    list2.insert(70)
    list2.insert(90)
    print("len =",len(list1))
    print("len =",len(list2))
    print(list1.__str__())
    print(list2.__str__())
    print("get item from linked list",list1.__getitem__(2))
    print("get item from linked list",list2.__getitem__(2))
    print("compare between two linked lists",list1.__eq__(list1))
    print("compare between two linked lists",list2.__eq__(list2))
    print("compare between two linked lists",list1.__eq__(list2))
    print("compare between two linked lists",list2.__eq__(list1))
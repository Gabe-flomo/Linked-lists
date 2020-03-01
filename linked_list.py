from box import Box

class LinkedList:
    def __init__(self,node = None):
        self.node = node
        self.length = 0 if node is None else 1

    def _len(self):
        return self.length
    
    def insert(self,data):
        '''
        Inserts a new node starting from the head.
        Once the head is initialized, newly added nodes become the new head.
        
        For Example:
            [1]=>[2]
            insert(3)
            [3]=>[1]=>[2]
        '''
        self.length += 1

        # This is the head Node
        if self.node is None:
            self.node = Box(data)
        else:
            # save the current node
            current = self.node

            # create the new node
            self.node = Box(data)

            # make the new node point to the prev
            self.node.next = current

        return self.length   

    def print_list(self):
        '''
        prints the linked list
        '''
        head = self.node
        while head:
            if head.next:
                print(f"[{head.data}]->",end="")
            elif head.next is None:
                print(f"[{head.data}]->None",end="")
            
            head = head.next
        
        print()

    def node_positions(self):
        # finds the middle index
        # if the length of the list is even there will be 2 middles
        # if the lenght of the list is odd there will be 1 middle
        middle = (self.length / 2) + 0.5 if self.length%2 is not 0 else (self.length // 2) 
        middle2 = middle + 1 if type(middle) is int else middle
        count = 1
        head = self.node
        while head:
            if count == 1:
                print(f"[{head.data}] -> Head")
            elif count == middle or count == middle2:
                print(f"[{head.data}] -> Middle")
            elif head.next is None:
                print(f"[{head.data}] -> Tail")
            else:
                print(f"[{head.data}]")
            
            count += 1
            head = head.next
        
        print()

    def delete(self):
        '''
        deletes the oldest node in the list
        '''
        head = self.node
        self.length -= 1
        while head:
            last = head.next.next

            # checks if the node 2 nodes ahead is none
            if last is None:
                # deletes the last node
                del last

                # makes the node before the deleted node the new tail
                head.next = None

            head = head.next

    def get_node(self,index):
        '''
        input an index location and the node at that index is returned
        '''
        count = 0
        head = self.node
        while head:
            
            count += 1
            if count == index:
                return head
            elif index > self.length:
                raise IndexError(f"Index is out of range for a list with size {self.length}")
            elif index < 0:
                raise ValueError(f"Index cannot be negative.")
            
            head = head.next

    def delete_node(self,index):
        '''
        enter an index location and will delete the node at that location
        '''

        # stores the node previous to the node thats being deleted
        prev_node = self.get_node(index-1)

        # stores the current node (the one being deleted)
        current_node = self.get_node(index)

        # stores the next pointer of the node being deleted
        current_node_next = current_node.next

        # sets the the previous node next pointer to the node after the node being deleted
        prev_node.next = current_node_next
        del current_node
        self.length -= 1

    def get_max(self):
        '''
        returns the largest node in the list
        '''
        max = 0
        head = self.node
        while head:
            if head.data > max:
                max = head.data
            
            head = head.next
        return max

    def move_to_head(self,node):
        pass

    def move_to_end(self,node):
        pass

    def remove_max(self):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass




ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(44)
ll.insert(8)
ll.insert(9)
ll.insert(10)
ll.insert(32)

ll.node_positions()
ll.print_list()
ll.delete()
value = ll.get_node(7)
print(value.data)
ll.print_list()
ll.delete_node(4)
ll.print_list()
print(ll.get_max())
ll.node_positions()


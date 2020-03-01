class Box:
    '''
    This class represents a single node within a linked list
    '''
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def has_next(self):
        '''
        Tells you wether or not this node is pointing to another node or not
        '''
        # if next is an object
        if self.next:
            return True
        # if next is None
        else:
            return False

    def get_next(self):
        '''
        Returns the value of the next node
        '''
        return self.next.data
    
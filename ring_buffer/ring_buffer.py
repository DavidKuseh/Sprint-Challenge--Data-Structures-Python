from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check storage to see if it's full or not
        
        # if there's space add element
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # set current to be added element
            self.current = self.storage.head
        
        # if storage is full
        # remove oldest element
        elif self.storage.length == self.capacity:
            rmv_head = self.storage.head
            self.storage.remove_from_head()
            # add new element
            self.storage.add_to_tail(item)
            # if current element is at the head, set the current to tail
            if rmv_head == self.current:
                self.current = self.storage.tail
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        # start from current item
        start = self.current
        list_buffer_contents.append(start.value)
        
        # if start.next, set nextItem to start next
        if start.next:
            nextItem = start.next
        # else set nextItem to storage head
        else:
            nextItem = self.storage.head
            
        # while nextItem is not equal to start
        while nextItem != start:
            # append nextItem to list_buffer_contents
            list_buffer_contents.append(nextItem.value)
            # if nextItem
            if nextItem.next:
                # set it to nextItem.next
                nextItem = nextItem.next
            # else set nextItem to storage head
            else:
                nextItem = self.storage.head 

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

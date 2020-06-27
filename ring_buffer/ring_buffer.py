class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.index = 0 

    # adds a given element to the buffer
    def append(self, item):
        # If the RB has no items or hasn't reached cap, add them
        if len(self.items) < self.capacity:
            self.items.append(item)

        # If the RB cap has been reached
            # Remove the least used item
            # Add the new item in it's place 
        else:
            self.items[self.index] = item
            self.index += 1

        # if the index pointer val is equal to max capacity, reset pointer to front
        if self.index == self.capacity:
            self.index = 0
        

    # returns all of the elements in the buffer in a list 
    # should not return any none values in the list even if present
    def get(self):
        return self.items 

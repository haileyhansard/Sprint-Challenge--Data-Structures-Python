class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity #the fixed max-size, which in test is 5
        self.buffer = [] #the values in the buffer array
        self.index_targeted = 0 #the index of the item that will be popped out of the array, initialized at 0 because once array is at capacity, its going to overwrite the 0 index first


    #FIFO, first in first out
    #Queue with a fixed max-size
    def append(self, item):
        #check if the length of buffer array is less than the capacity allowed (fixed max-size)
        if len(self.buffer) < self.capacity:
            #if length is smaller, can go ahead and add item to array (up to 5 items in this case)
            self.buffer.append(item)

        #if the length of buffer array is at capacity, need to overwrite the oldest item with the newest item
        elif len(self.buffer) == self.capacity:
            #and if the index is the same as capacity, 5, 
            if self.index_targeted == self.capacity:
                #then we are going to set the index 5 back to 0
                self.index_targeted = 0
            #we pop the item out at the index specified
            self.buffer.pop(self.index_targeted)
            #at the location of the index specified, insert the item 
            self.buffer.insert(self.index_targeted, item)
            #increase the index by 1 each time so that it keeps going in a loop. It won't go forever because it will reach capacity once its at 5
            self.index_targeted += 1

    def get(self):
        return self.buffer


#--- testing ---#
buffer = RingBuffer(5)

print(buffer.get())

(buffer.append('a'))
(buffer.append('b'))
(buffer.append('c'))
(buffer.append('d'))
(buffer.append('e'))
(buffer.append('f'))
(buffer.append('g'))

print(buffer.get())
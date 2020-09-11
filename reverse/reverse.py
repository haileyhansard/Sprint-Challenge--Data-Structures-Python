class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #check if head is empty, if it is, return None
        if self.head is None:
            return None
        #check if the next value is None, if it is, set the head to be node
        if node.get_next() is None:
            self.head = node
        #if there is a next,
        if node.get_next():
            #reverse the list by inputting the node's value onto the next position
            self.reverse_list(node.get_next(), node)
        #otherwise, set the next position as the previous value    
        node.set_next(prev)



#---testing---#
# test = LinkedList()
# test.add_to_head(1)
# test.add_to_head(2)
# test.add_to_head(3)
# print('original head', test.head.value)
# test.reverse_list(test.head, None)
# print('new head', test.head.value)
# print(test.head.get_next().value)

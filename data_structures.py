################################################################################
                                 LINKED LIST
################################################################################
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        #self.tail

    def find(self, val):                # FIND VALUE IN LINKED LIST
        node = self.head
        while node != None:
            if node.value == val:
                return 1
            else:
                node = node.next
        return 0

    def insert(self, val):              # INSERT VALUE IN LINKED LIST           - Change condition (this is a sorted L.List)
        if self.head == None:
            self.head = Node(val)
        elif self.head.value > val:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            while node.next != None:
                if node.next.value > val:
                    new_node = Node(val)
                    new_node.next = node.next
                    node.next = new_node
                    return
                else:
                    node = node.next
            node.next = Node(val)
        return

    def remove(self, val):              # REMOVE VALUE
        if self.head == None:
            return 0
        elif self.head.value == val:
            self.head = self.head.next
            return 1
        else:
            node = self.head
            while node.next != None:
                if node.next.value == val:
                    node.next = node.next.next
                    return 1
                else:
                    node = node.next
        return 0

    def find_index(self, val):          # FIND VALUE'S INDEX
        node = self.head
        val_index = 0
        while node != None:
            if node.value == val:
                return val_index
            else:
                node = node.next
                val_index += 1
        return -1

    def append(self, val):              # APPEND VALUE
        if self.head == None:
            self.head = Node(val)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(val)
        return

    def push(self, val):                # PREPEND VALUE
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        return

    def pop_first(self):                # POP FIRST VALUE

        if self.head == None:
            return None
        else:
            node = self.head
            self.head = self.head.next
        return node.value

    def pop_last(self):                 # POP LAST VALUE

        if self.head == None:
            return None
        elif self.head.next == None:
            node = self.head
            self.head = None
            return node.value
        else:
            node = self.head
            next_node = node.next
            while next_node.next != None:
                node = node.next
                next_node = node.next
            node.next = None
        return next_node.value

    def general_insert(self, val):      # GENERAL INSERT VALUE IN LINKED LIST

        if self.head == None:       # Check empty list
            self.head = Node(val)
        elif condition:     # Check head contion
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:               # Insert between elements
            node = self.head
            while node.next != None:
                if next_condition: # Check node condition
                    new_node = Node(val)
                    new_node.next = node.next
                    node.next = new_node
                    return
                else:
                    node = node.next
            node.next = Node(val) # Insert at end if there is no other place
        return

    def has_cycle(self):                # CHECKS IF THERE IS A CYCLE

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if fast == None or fast.next == None:
            return None

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast


#       NOTAS
#   Cuidado con el primer y último elemento al recorrer la lista (hay que tratarlos de manera diferente en general)
#   Especial cuidado con insertar elementos
#   Se pueden implementar STACKS y queues con una linked list
#   También útil para hash maps
#   Se puede tener una variable length que se incremente o decremente al insertar o eliminar elementos


################################################################################
                             DOUBLY LINKED LIST
################################################################################
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def find(self, val):                # FIND VALUE IN LINKED LIST
        node = self.head
        while node != None:
            if node.value == val:
                return 1
            else:
                node = node.next
        return 0

    def insert(self, val):              # INSERT VALUE IN LINKED LIST           - Change condition (this is a sorted L.List)
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        elif self.head.value > val:
            new_node = Node(val)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif self.tail.value < val:
            new_node = Node(val)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            node = self.head.next
            while node != None:
                if node.value > val:
                    new_node = Node(val)
                    new_node.prev = node.prev
                    new_node.next = node
                    node.prev = new_node
                    new_node.prev.next = new_node
                    return
                else:
                    node = node.next
        return

    def remove(self, val):              # REMOVE VALUE
        if self.head == None:
            return 0
        elif self.head.value == val and self.head == self.tail:
            self.head = None
            self.tail = None
            return 1
        elif self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
            return 1
        elif self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next = None
            return 1
        else:
            node = self.head
            while node != None:
                if node.value == val:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    return 1
                else:
                    node = node.next
        return 0

    def find_index(self, val):          # FIND VALUE'S INDEX
        node = self.head
        val_index = 0
        while node != None:
            if node.value == val:
                return val_index
            else:
                node = node.next
                val_index += 1
        return -1

    def append(self, val):              # APPEND VALUE
        if self.tail == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return

    def push(self, val):                # PREPEND VALUE

        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.head.prev = Node(val)
            self.head.prev.next = self.head
            self.head = self.head.prev
        return

    def pop_first(self):                # POP FIRST VALUE

        if self.head == None:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None
        return node.value

    def pop_last(self):                 # POP LAST VALUE

        if self.tail == None:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        return node.value

    def general_insert(self, val):      # GENERAL INSERT VALUE IN LINKED LIST

        if self.head == None:       # Check empty list
            self.head = Node(val)
            self.tail = self.head
        elif condition:     # Check head condition
            new_node = Node(val)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif condition:     # Check tail condition
            new_node = Node(val)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:               # Insert between elements
            node = self.head
            while node != None:
                if node.value > val:    # Check node condition
                    new_node = Node(val)
                    new_node.next = node
                    new_node.prev = node.prev
                    new_node.next.prev = new_node
                    new_node.prev.next = new_node
                    return
                else:
                    node = node.next
        return

#       NOTAS
#   Cuidado con el primer y último elemento al recorrer la lista (hay que tratarlos de manera diferente en general)
#   Especial cuidado con insertar elementos
#   Se pueden implementar stacks y QUEUES con una doubly linked list
#   Se puede tener una variable length que se incremente o decremente al insertar o eliminar elementos


################################################################################
                                   STACK
################################################################################

#       NOTAS
#   Para implementar un stack lo mejor es usar un array, appendeando elementos
#   Otra forma sería una linked list, añadiendo y eliminando elementos en head


################################################################################
                                   QUEUE
################################################################################

import queue
# Three types:
# maxsize = 0 by default imput in each class definition
q = queue.Queue() # Normal Queue
q = queue.LifoQueue()   # STACK!!
q = queue.PriorityQueue()

# Queues methods:
q.qsize()       # Returns queues size
q.empty()       # Return "True" if empty, "False" otherwise
q.full()        # Return "True" if full, "False" otherwise
q.put(element)  # Enqueue element
q.get()         # Dequeue and return de first element

#       NOTAS
#   Para implementar una queue lo mejor es utilizar la librería "queue", cuyas funciones están arriba
#   Otra forma sería una doubly linked list, añadiendo en tail y eliminando en head




################################################################################
                                   TREE
################################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        #self.parent = None

class Tree:
    def __init__(self, root = None):
        self.root = root

    def DepthFirstSearch(self, val, node = None):

        if node == None:
            if self.root == None:
                return False
            else:
                return self.DepthFirstSearch(val, self.root)
        else:
            if node.value == val:
                return True
            else:
                for child in node.children:
                    found = self.DepthFirstSearch(val, child)
                    if found == True:
                        return True
        return False

    def BreadthFirstSearch(self, val):
        if self.root == None:
            return False
        else:
            visit = [self.root]
            while visit != []:
                node = visit[0]
                del(visit[0])
                if node.value == val:
                    return True
                else:
                    for child in node.children:
                        visit.append(child)
        return False


################################################################################
                                BINARY TREE
################################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        #self.parent = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        self.traversal = []

    def DepthFirstSearch(self, val, node = None):
        if node == None:
            if self.root == None:
                return False
            else:
                return self.DepthFirstSearch(val, self.root)
        else:
            if node.value == val:
                return True
            else:
                if node.left != None:
                    found = self.DepthFirstSearch(val, node.left)
                    if found == True:
                        return True
                if node.right != None:
                    found = self.DepthFirstSearch(val, node.right)
                    if found == True:
                        return True
        return False

    def BreadthFirstSearch(self, val):
        if self.root == None:
            return False
        else:
            visit = [self.root]
            while visit != []:
                node = visit[0]
                del(visit[0])
                if node.value == val:
                    return True
                else:
                    if node.left != None:
                        visit.append(node.left)
                    if node.right != None:
                        visit.append(node.right)
        return False

    def preorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.preorder_traversal(self.root)
                return self.traversal
        else:
            self.traversal.append(node.value)
            if node.left != None:
                self.preorder_traversal(node.left)
            if node.right != None:
                self.preorder_traversal(node.right)
        return

    def inorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.inorder_traversal(self.root)
                return self.traversal
        else:
            if node.left != None:
                self.inorder_traversal(node.left)
            self.traversal.append(node.value)
            if node.right != None:
                self.inorder_traversal(node.right)
        return

    def postorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.postorder_traversal(self.root)
                return self.traversal
        else:
            if node.left != None:
                self.postorder_traversal(node.left)
            if node.right != None:
                self.postorder_traversal(node.right)
            self.traversal.append(node.value)
        return



################################################################################
                             BINARY SEARCH TREE
################################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        #self.parent = None

    # def get_next(self):
    #
    #     if self.right != None:
    #         node = self.right
    #         while node.left != None:
    #             node = node.left
    #        	return node
    #     else:
    #         node = self
    #         while node.parent != None:
    #             if node.parent.value < node.value:
    #                 node = node.parent
    #             else:
    #                 break
    #         return node.parent
    #     return None

    # def get_prev(self):
    #
    #     if self.left != None:
    #         node = self.left
    #         while node.right != None:
    #             node = node.right
    #         return node
    #     else:
    #         node = self
    #         while node.parent != None:
    #             if node.parent.value > node.value:
    #                 node = node.parent
    #             else:
    #                 break
    #         return node.parent
    #     return None

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        self.traversal = []

    def insert(self, val, node = None):

        if node == None:
            if self.root == None:
                self.root = Node(val)
            else:
                self.insert(val, self.root)
        else:
            if val < node.value:
                if node.left != None:
                    self.insert(val, node.left)
                else:
                    node.left = Node(val)
                    #node.left.parent = node
            else:
                if node.right != None:
                    self.insert(val, node.right)
                else:
                    node.right = Node(val)
                    #node.right.parent = node
        return

    def insert_list(self, list):

        for element in list:
            self.insert(element)
        return

    def find(self, val, node = None):

        if node == None:
            if self.root == None:
                return False
            else:
                return self.find(val, self.root)
        else:
            if node.value == val:
                return True
            elif val < node.value:
                if node.left == None:
                    return False
                else:
                    return self.find(val, node.left)
            else:
                if node.right == None:
                    return False
                else:
                    return self.find(val, node.right)
        return False

    def preorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.preorder_traversal(self.root)
                return self.traversal
        else:
            self.traversal.append(node.value)
            if node.left != None:
                self.preorder_traversal(node.left)
            if node.right != None:
                self.preorder_traversal(node.right)
        return

    def inorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.inorder_traversal(self.root)
                return self.traversal
        else:
            if node.left != None:
                self.inorder_traversal(node.left)
            self.traversal.append(node.value)
            if node.right != None:
                self.inorder_traversal(node.right)
        return

    def postorder_traversal(self, node = None):

        if node == None:
            if self.root == None:
                return []
            else:
                self.traversal = []
                self.postorder_traversal(self.root)
                return self.traversal
        else:
            if node.left != None:
                self.postorder_traversal(node.left)
            if node.right != None:
                self.postorder_traversal(node.right)
            self.traversal.append(node.value)
        return



################################################################################
                                   HEAP
################################################################################

class MinHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def insert(self, val):              # INSERT ELEMENT IN HEAP

        self.heapList.append(val)
        current = self.size
        parent = int((current-1)/2)
        self.size += 1

        while self.heapList[current] < self.heapList[parent]:
            self.heapList[current] = self.heapList[parent]
            self.heapList[parent] = val
            current = parent
            parent = int((current-1)/2)

        return

    def insert_list(self, hlist):       # INSERT MULTIPLE ELEMENTS
        for element in hlist:
            self.insert(element)
        return

    def peek(self):                     # RETURNS MIN VALUE

        if self.size == 0:
            return None

        return self.heapList[0]

    def pop_min(self):                  # REMOVES MIN VALUE

        if self.size == 0:
            return None
        else:
            self.size -= 1
            min = self.heapList[0]
            self.heapList[0] = self.heapList[-1]
            del(self.heapList[-1])

            current = 0
            left_child = 2 * current + 1
            right_child = 2 * current + 2

            while left_child < self.size:
                if right_child < self.size:
                    if self.heapList[left_child] < self.heapList[right_child] and self.heapList[left_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    elif self.heapList[right_child] < self.heapList[left_child] and self.heapList[right_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[right_child]
                        self.heapList[right_child] = temp
                        current = right_child
                    else:
                        return min
                else:
                    if self.heapList[left_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    else:
                        return min

                left_child = 2 * current + 1
                right_child = 2 * current + 2

        return min

    def replace(self, val):             # POP MIN AND INSERT VALUE

        if self.size == 0:
            return None
        else:
            min = self.heapList[0]
            self.heapList[0] = val

            current = 0
            left_child = 2 * current + 1
            right_child = 2 * current + 2

            while left_child < self.size:
                if right_child < self.size:
                    if self.heapList[left_child] < self.heapList[right_child] and self.heapList[left_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    elif self.heapList[right_child] < self.heapList[left_child] and self.heapList[right_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[right_child]
                        self.heapList[right_child] = temp
                        current = right_child
                    else:
                        return min
                else:
                    if self.heapList[left_child] < self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    else:
                        return min

                left_child = 2 * current + 1
                right_child = 2 * current + 2

        return min


class MaxHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def insert(self, val):              # INSERT ELEMENT IN HEAP

        self.heapList.append(val)
        current = self.size
        parent = int((current-1)/2)
        self.size += 1

        while self.heapList[current] > self.heapList[parent]:
            self.heapList[current] = self.heapList[parent]
            self.heapList[parent] = val
            current = parent
            parent = int((current-1)/2)

        return

    def insert_list(self, hlist):       # INSERT MULTIPLE ELEMENTS
        for element in hlist:
            self.insert(element)
        return

    def peek(self):                     # RETURNS MAX VALUE

        if self.size == 0:
            return None

        return self.heapList[0]

    def pop_max(self):                  # REMOVES MAX VALUE

        if self.size == 0:
            return None
        else:
            self.size -= 1
            min = self.heapList[0]
            self.heapList[0] = self.heapList[-1]
            del(self.heapList[-1])

            current = 0
            left_child = 2 * current + 1
            right_child = 2 * current + 2

            while left_child < self.size:
                if right_child < self.size:
                    if self.heapList[left_child] > self.heapList[right_child] and self.heapList[left_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    elif self.heapList[right_child] > self.heapList[left_child] and self.heapList[right_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[right_child]
                        self.heapList[right_child] = temp
                        current = right_child
                    else:
                        return min
                else:
                    if self.heapList[left_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    else:
                        return min

                left_child = 2 * current + 1
                right_child = 2 * current + 2

        return min

    def replace(self, val):             # POP MAX AND INSERT VALUE

        if self.size == 0:
            return None
        else:
            min = self.heapList[0]
            self.heapList[0] = val

            current = 0
            left_child = 2 * current + 1
            right_child = 2 * current + 2

            while left_child < self.size:
                if right_child < self.size:
                    if self.heapList[left_child] > self.heapList[right_child] and self.heapList[left_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    elif self.heapList[right_child] > self.heapList[left_child] and self.heapList[right_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[right_child]
                        self.heapList[right_child] = temp
                        current = right_child
                    else:
                        return min
                else:
                    if self.heapList[left_child] > self.heapList[current]:
                        temp = self.heapList[current]
                        self.heapList[current] = self.heapList[left_child]
                        self.heapList[left_child] = temp
                        current = left_child
                    else:
                        return min

                left_child = 2 * current + 1
                right_child = 2 * current + 2

        return min

#       NOTAS
# Estos son Binary Heaps:
#
#                 _   0   _
#		    1                 2
#         /   \            /    \
#	   3        4        5        6
#	  / \      / \      / \      / \
#	 7   8    9  10    11 12    13 14
#
# Left child    2n + 1
# Right child   2n + 2
# Parent        (n-1)/2



################################################################################
                                   GRAPH
################################################################################

# NOTAS
#   Si simplemente hace falta un undirected graph sin weighted edges entonces con tener la clase de nodo basta, incluyendo los nodos con los cuales está conectado
#   Si es un directed graph entonces habría que incluir en cada clase tan solo los nodos hacia los cuales existe un edge desde el mismo
#   Para graphs con weighted edges hay que crear una clase específica, con el valor, nodo de partida y nodo de llegada si es directed o los nodos que une en un undirected
#
#   Cuando se pretende hacer una búsqueda conviene incluir el parámetro visited en los nodos, y una función que reinicie todos eso valores a 0


################################################################################
                               SEARCH & SORT
################################################################################

def BinarySearch(array, value):         # Time Complexity: O(log(n))

    first = 0
    last = len(array)-1

    while first <= last:
        mid = (first + last)//2
        if array[mid] < value:
            first = mid + 1
        elif array[mid] > value:
            last = mid - 1
        else:
            return mid

    return -1

def BubbleSort(array):                  # Average and Worst Case: O(n^2)
                                        # Best Case: O(n) - the array is nearly or already sorted
                                        # Space Complexity: O(1)
    n = len(array)
    sorted = 0
    iteration = 0
    while sorted == 0:
        sorted = 1
        iteration = iteration + 1
        for i in range(0,n - iteration):
            if array[i] > array[i+1]:
                array[i], array[i+1] =  array[i+1], array[i]
                sorted = 0
    return array

def MergeSort(array, left = 0, right = None):   # Time Complexity: O(n log(n))  and Space Complexity: O(n)

    left < right:
    mid = (left + right) // 2
    MergeSort(array, left, mid)
    MergeSort(array, mid+1, right)

    i = 0
    j = 0
    llist = array[left:mid+1]
    rlist = array[mid+1:right+1]
    while i <= mid-left and j <= right-mid-1:

        if llist[i] < rlist[j]:
            array[left+i+j] = llist[i]
            i = i+1
        else:
            array[left+i+j] = rlist[j]
            j = j+1

    if i <= mid-left:
        array[left + i + j: right + 1] = llist[i:]
    else:
        array[left + i + j: right + 1] = rlist[j:]

    return array

def QuickSort(array, left = 0, right = None):   # Average and Best Case: O(n log(n))
                                                # Worst Case: O(n^2)
                                                # Space Complexity: O(1)
    if right == None:
        right = len(array) - 1
    if left < right:
        pivot = right
        current = left
        while current < pivot:
            if array[current] > array[pivot]:
                array[current], array[pivot-1], array[pivot] = array[pivot-1], array[pivot], array[current]
                pivot = pivot - 1
            else:
                current = current + 1
        QuickSort(array, left, pivot-1)
        QuickSort(array, pivot+1, right)

    return array


################################################################################
                                 HASH TABLE
################################################################################

class HashTable:
    def __init__(self):
        self.table = [None]*1000

    def store(self, string):

        hashvalue = calculate_hash_value(string)
        if self.table[hashvalue] == None:
            self.table[hashvalue] = [string]
        else:
            self.table[hashvalue].append(string)

        return

    def lookup(self,string):

        hashvalue = self.calculate_hash_value(string)
        if self.table[hashvalue]!=None:
            return hashvalue

        return -1

    def calculate_hash_value(self,string):
        return #HashFunction

# DICTIONARIES
#   >> dic = {key0:value0, key1:value1, key2:value2}
#       {key0:value0, key1:value1, key2:value2}
#
#   >> dic[key3] = value3
#       {key0:value0, key1:value1, key2:value2, key3:value3}
#   >> dic[key3] = value4
#       {key0:value0, key1:value1, key2:value2, key3:value4}
#
#   >> dic[key1]    >>>    value1
#   >> dic[key4]    >>>    ERROR!!!
#   >> dic.get(key1)    >>>    value1
#   >> dic.get(key4)    >>>    None
#
#   >> del(dic[key3])
#       {key0:value0, key1:value1, key2:value2}
#
#   >> dic.keys()    >>>    [key0, key1, key2]
#   >> dic.values()    >>>    [value0, value1, value2]


class Node:
  # constructor
  def __init__(self, data = None, ref=None): 
    '''
    data: holds Linked list Data
    ref: holds Reference to next linked list block
    '''
    self.data = data
    self.ref = ref

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.ref):
        current = current.ref
      current.ref = newNode
    else:
      self.head = newNode

  def insert_inbetween(self, middle_node, data):
    if middle_node is None:
      print('Node is absent')
      return
    newNode = Node(data)
    newNode.ref=middle_node.ref
    middle_node.ref=newNode


  # print method for the linked list
  def print_Linked_List(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.ref


  def remove(self, data_id):
    Head=self.head 

    if(Head is not None):
      if(Head.data==data_id):
        self.head=Head.ref
        Head=None
        return
    while(Head is None):
      if(Head.data==data_id):
        break
      prev=Head
      Head=Head.ref

    if (Head == None):
      return

    prev.ref=Head.ref
    Head=None

#Execute
LL = LinkedList()
LL.insert("Hello")
LL.insert("World")
LL.insert("Data Structures")
LL.print_Linked_List()
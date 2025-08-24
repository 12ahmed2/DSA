class Node:
  """A node in a singly linked list."""
  def __init__(self,value):
    self.value = value
    self.next= None


class LinkedList :
  """A simple singly linked list implementation."""
  def __init__(self):
    self.head= None
    self.length = 0
    self.last_member = None

  def __len__(self):
    """Return the number of elements in the list."""
    return self.length

  def add(self,value):
    """Append a new node with the given value at the end of the list."""
    if self.head is None:
      self.head = Node(value)
      self.last_member = self.head
      self.length += 1
    else :
      self.last_member.next = Node(value)
      self.length += 1
      self.last_member = self.last_member.next


  def remove(self,index):
    """Remove the node at the given index."""
    if index >= self.length or index < 0 :
      raise IndexError ("your index out of range")
    elif index == 0 :
      if self.head is None :
        raise ValueError ("the linked list is empty")
      self.head = self.head.next
      self.length -= 1
      if self.length == 0:
          self.last_member = None
    else:
      remove_member = self.head
      for _ in range(index-1):
          remove_member = remove_member.next
      remove_member.next = remove_member.next.next
      if index == self.length-1:
          self.last_member = remove_member
      self.length -= 1


  def insert_index(self,value,index):
    """
        Insert a new node with the given value at a specific index.

        Args:
            value: The data to store in the new node.
            index (int): Position at which to insert.

        Raises:
            IndexError: If index is out of range.
    """
    if index > self.length or index < 0 :
        raise IndexError ("your index out of range")

    elif index == 0 :
      if self.head is None:
        self.add(value)

      else :
        temp_head = self.head
        self.head = Node(value)
        self.length += 1
        self.head.next = temp_head

    elif index == self.length:
        return self.add(value)

    else :
        insert_member = self.head
        for _ in range(index-1):
            insert_member = insert_member.next
        new_node = Node(value)
        new_node.next = insert_member.next
        insert_member.next = new_node

        self.length += 1

  def __iter__(self):
    """Iterate through all values in the linked list."""
    printing = self.head
    while printing:
      yield printing.value
      printing = printing.next

  def __repr__(self):
    """Return a string representation of the list."""
    return f"[{','.join(repr(x) for x in self)}]"

first_linked = LinkedList()

first_linked.add("Ahmed")

first_linked.add("Mohamed")

first_linked.add("Aboelmaaty")

len(first_linked)

print(first_linked)

first_linked.insert_index("man",0)

print(first_linked)

len(first_linked)

first_linked.remove(0)

print(first_linked)

len(first_linked)

last_linked = LinkedList()

print(last_linked)


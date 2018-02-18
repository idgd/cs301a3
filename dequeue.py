class node:

	def __init__(self,item):
		if item == None:
			self.item = None
			self.next = None
		else:
			self.item = item
			self.next = node(None)

class queue:

	def __init__(self):
		self.head = node(None)
		self.count = 0

	def addFront(self,item):
		n = self.head
		while n.next.next != None:
			n = n.next
		n.next = node(item)

	def addRear(self,item):
		n = self.head
		self.head = node(item)
		self.head.next = n

	def removeFront(self):
		n = self.head
		while n.next.next != None:
			n = n.next
		n.next = node(None)

	def removeRear(self):
		self.head = self.head.next

	def isEmpty(self):
		if self.head.next == None:
			return(True)
		else:
			return(False)

	def size(self):
		return(self.count)

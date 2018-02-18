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

	def enqueue(self,item):
		n = self.head
		self.head = node(item)
		self.head.next = n
		self.count += 1

	def dequeue(self):
		n = self.head
		while n.next.item != None:
			p = n
			n = n.next
		p.next = node(None)
		self.count -= 1

	def isEmpty(self):
		if self.head.next == None:
			return(True)
		else:
			return(False)

	def size(self):
		return(self.count)

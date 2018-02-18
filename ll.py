class node:

	def __init__(self,item):
		if item == None:
			self.item = None
			self.next = None
		else:
			self.item = item
			self.next = node(None)

class ll:

	def __init__(self):
		self.head = node(None)
		self.count = 0

	def add(self,item):
		if self.head.next == None:
			n = node(None)
		else:
			n = self.head.next
		self.head = node(item)
		self.head.next = n
		self.count += 1

	def remove(self,item):
		n = self.head
		while n.next.item != item:
			n = n.next
		n.next = n.next.next
		self.count -= 1

	def search(self,item):
		n = self.head
		while n.next.item != item:
			n = n.next
		if n.next == None:
			return(False)
		else:
			return(True)

	def isEmpty(self):
		if self.head.item != None and self.head.next.item != None:
			return(False)
		else:
			return(True)

	def size(self):
		return(self.count)

	def append(self,item):
		n = self.head
		while n.next != None:
			n = n.next
		n.next = node(item)
		self.count += 1

	def index(self,item):
		n = self.head
		c = 0
		if n.item == item:
			return(0)
		while n.next.item != item:
			n = n.next
			c += 1
		return(c)

	def insert(self,pos,item):
		n = self.head
		for f in range(pos):
			n = n.next
		o = node(item)
		o.next = n.next
		n.next = o

	def pop(self):
		n = self.head
		p = None
		while n.next != None:
			p = n
			n = n.next
		p.next = node(None)
		return(n.item)

	def pop(self,item):
		n = self.head
		p = None
		while n.next != item:
			p = n
			n = n.next
		p.next = n.next
		return(n.item)
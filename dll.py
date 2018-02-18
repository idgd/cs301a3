class node:

	def __init__(self,item,last):
		if item == None:
			self.last = None
			self.item = None
			self.next = None
		else:
			self.last = last
			self.item = item
			self.next = node(None,None)

class dll:

	def __init__(self):
		self.head = node(None,None)
		self.count = 0

	def add(self,item):
		if self.head.next == None:
			n = node(None,None)
		else:
			n = self.head.next
		self.head = node(item,item)
		self.head.next = n
		self.count += 1

	def remove(self,item):
		n = self.head
		while n.next.item != item:
			n = n.next
		n.next.last = n.last
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
		n.next = node(item,n)
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
		o = node(item,n)
		o.next = n.next
		n.next = o

	def pop(self):
		n = self.head
		p = None
		while n.next != None:
			p = n
			n = n.next
		p.next = node(None,None)
		return(n.item)

	def pop(self,item):
		n = self.head
		p = None
		while n.next != item:
			p = n
			n = n.next
		p.next = n.next
		n.next.last = p
		return(n.item)

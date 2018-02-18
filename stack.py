class node:

	def __init__(self,item):
		if item == None:
			self.item = None
			self.next = None
		else:
			self.item = item
			self.next = node(None)

class stack:

	def __init__(self):
		self.head = node(None)
		self.count = 0

	def push(self,item):
		n = self.head
		while n.next.item != None:
			n = n.next
		n.next = node(item)
		self.count += 1

	def pop(self):
		n = self.head
		while n.next.item != None:
			p = n
			n = n.next
		p.next = node(None)
		self.count -= 1
		return(n)

	def peek(self):
		n = self.head
		while n.next.item != None:
			n = n.next
		return(n)

	def isEmpty(self):
		if self.head.next == None:
			return(True)
		else:
			return(False)

	def size(self):
		return(self.count)

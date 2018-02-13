class node:
	def __init__(self,item):
		if item == None:
			self.item = None
			self.next = None
		else:
			self.item = item
			self.next = node(None)

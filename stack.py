class stack:

	def __init__(self):
		self.s = []

	def push(self,item):
		self.s.append(item)

	def pop(self):
		return(self.s.pop())

	def peek(self):
		return(self.s[-1])

	def isEmpty(self):
		if not self.s:
			return(True)
		else:
			return(False)

	def size(self):
		return(len(self.s))

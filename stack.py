class stack:

	def __init__(self):
		self.s = []

	def push(self,item):
		self.s.append(item)
		# constant time

	def pop(self):
		return(self.s.pop())
		# constant time

	def peek(self):
		return(self.s[-1])
		# constant time

	def isEmpty(self):
		if not self.s:
			return(True)
		else:
			return(False)
		# constant time

	def size(self):
		return(len(self.s))
		# constant time

class queue:

	def __init__(self):
		self.q = []

	def enqueue(self,item):
		self.q.insert(0,item)

	def dequeue(self):
		self.q.pop()

	def isEmpty(self):
		if not self.q:
			return(True)
		else:
			return(False)

	def size(self):
		return(len(self.q))

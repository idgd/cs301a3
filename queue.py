class queue:

	def __init__(self):
		self.q = []

	def enqueue(self,item):
		self.q.insert(0,item)
		# linear (n) time

	def dequeue(self):
		return(self.q.pop())
		# constant time

	def isEmpty(self):
		if not self.q:
			return(True)
		else:
			return(False)
		# constant time

	def size(self):
		return(len(self.q))
		# constant time

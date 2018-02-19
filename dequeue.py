class dequeue:

	def __init__(self):
		self.dq = []

	def addFront(self,item):
		self.dq.append(item)

	def addRear(self,item):
		self.dq.insert(0,item)

	def removeFront(self):
		del self.dq[-1]

	def removeRear(self):
		del self.dq[0]

	def isEmpty(self):
		if not self.dq:
			return(True)
		else:
			return(False)

	def size(self):
		return(len(self.dq))

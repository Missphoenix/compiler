class ListandPointer:
	def __init__(self):
		self.__pointer = 0
		self.__strlist = []

	def AddNode(self, terminal):
		self.__strlist.append(terminal)

	def setPointer(self, pointer):
		self.__pointer = int(pointer)

	def IterablePointer(self):
		self.__pointer = self.__pointer + 1

	def getPointer(self):
		res = self.__pointer
		return res

	def getNode(self):
		res = str(self.__strlist[self.__pointer])
		return res

	def ResetPointer(self):
		self.__pointer = 0 

	def getLength(self):
		length = len(self.__strlist)
		return length

	def PrintList(self):
		print(self.__strlist)
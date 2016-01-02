class ListandPointer:
	def __init__(self):
		self.__pointer = 0
		self.__strlist = []

	def add_node(self, terminal):
		self.__strlist.append(terminal)

	def set_pointer(self, pointer):
		self.__pointer = int(pointer)

	def next_pointer(self):
		self.__pointer = self.__pointer + 1

	def get_node(self):
		res = str(self.__strlist[self.__pointer])
		return res

	def reset_pointer(self):
		self.__pointer = 0 

	def length(self):
		length = len(self.__strlist)
		return length

	def print_list(self):
		print(self.__strlist)
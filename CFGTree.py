from Node import rootNode

class CFGTree:
	def __init__(self , root):
		self.__root = rootNode(root)

	def set_rule(self, rule, number):
		self.__root.add_rule(rule, number)

	def get_root(self):
		root = self.__root
		return root

	def print_tree(self):
		self.__root.print_root()
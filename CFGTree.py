from Node import rootNode

class CFGTree:
	def __init__(self , root):
		self.__root = rootNode(root)

	def SetRule(self, rule, number):
		self.__root.AddRule(rule, number)

	def getRoot(self):
		root = self.__root
		return root

	def PrintTree(self):
		self.__root.PrintRoot()
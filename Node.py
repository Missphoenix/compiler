class rootNode:
	def __init__(self , root):
		self.__rootVal = root
		self.__rules = []

	def AddRule(self, rule):
		rulenode = ruleNode(rule , len(self.__rules)+1)
		self.__rules.append(rulenode)

	def PrintRoot(self):
		print("Root: %s"% (self.__rootVal), end = " ")
		for element in self.__rules:
			element.PrintRule()
		print()


class ruleNode:
	def __init__(self , rule , index):
		self.__ruleVal = rule
		self.__ruleIndex = index
		self.__simples = []
		self.__Derives = False
		self.__firsts = []
		self.__follows = []

	def AddSimple(self, simple):
		simplenode = simpleNode(simple , len(simples)+1)
		self.__simples.append(simplenode)

	def AddFirst(self, first):
		self.__firsts.append(first)

	def AddFollow(self, follow):
		self.__follows.append(follow)

	def PrintRule(self):
		print("index %d: %s"% (self.__ruleIndex, self.__ruleVal), end = " ")

class simpleNode:
	def __init__(self , simple , index):
		self.__simpleVal = simple
		self.__simpleIndex = index
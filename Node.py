class rootNode:
	def __init__(self , root):
		self.__rootVal = root
		self.__rules = []

	def AddRule(self, rule):
		rulenode = ruleNode(rule , len(self.__rules)+1)
		self.__rules.append(rulenode)

	def getRules(self):
		rules = self.__rules
		return rules

	def getRootVal(self):
		res = self.__rootVal
		return res

	def PrintRoot(self):
		print("Root: %s"% (self.__rootVal))
		for element in self.__rules:
			element.PrintRule()
		print()


class ruleNode:
	def __init__(self , rule , index):
		self.__ruleVal = rule
		self.__ruleIndex = index
		self.__simples = []
		self.__Derives = None
		self.__firsts = []
		self.__follows = []

	def AddSimple(self, simple):
		simplenode = simpleNode(simple , len(self.__simples)+1)
		self.__simples.append(simplenode)

	def AddFirst(self, first):
		self.__firsts.append(first)

	def AddFollow(self, follow):
		self.__follows.append(follow)

	def ResetSimples(self):
		self.__simples.clear()

	def setDerives(self , derives):
		self.__Derives = derives

	def getRuleVal(self):
		res = self.__ruleVal
		return res

	def getSimples(self):
		simples = self.__simples
		return simples

	def getDerives(self):
		derives = self.__Derives
		return derives

	def PrintRule(self):
		print(" Rule index %d: %s; derive λ: %s; first: %s; follow: %s"% (self.__ruleIndex, self.__ruleVal, self.__Derives, self.__firsts, self.__follows))
		for node in self.__simples:
			node.PrintSimple()
		print()

class simpleNode:
	def __init__(self , simple , index):
		self.__simpleVal = simple
		self.__simpleIndex = index

	def getSimpleVal(self):
		res = self.__simpleVal
		return res

	def PrintSimple(self):
		print("  Simple index %d: %s"% (self.__simpleIndex, self.__simpleVal), end =" ")
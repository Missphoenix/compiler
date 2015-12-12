class rootNode:
	def __init__(self , root):
		self.rootVal = root
		self.rules = []
	def AddRule(rule):
		rulenode = ruleNode(rule , len(rules)+1)
		self.rules.append(rulenode)

class ruleNode:
	def __init__(self , rule , index):
		self.ruleVal = rule
		self.ruleIndex = index
		self.simples = []
		self.Derives = false
		self.firsts = []
		self.follows = []
	def AddSimple(simple):
		simplenode = simpleNode(simple , len(simples)+1)
		self.simples.append(simplenode)
	def AddFirst(first):
		self.firsts.append(first)
	def AddFollow(follow):
		self.follows.append(follow)

class simpleNode:
	def __init__(self , simple , index):
		self.simpleVal = simple
		self.simpleIndex = index
from CFGTree import CFGTree
from Node import simpleNode

class CFGDerivesMaker:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		self.__treeList = CFGTreeList
		self.__NonTerminalList = NonTerminalList
		self.__TerminalList = TerminalList
		self.__FindRuleDerives()
		self.__PrintDerives()

		# debug part
	def __PrintDerives(self):
		for tree in self.__treeList:
			for rule in tree.getRoot().getRules():
				print(rule.getRuleVal()+"\n")
				print("Derives:  "+str(rule.getDerives())+"\n")

		# code part
	def __FindRuleDerives(self):
		for tree in self.__treeList:
			for rule in tree.getRoot().getRules():
				if rule.getDerives() == None:
					ruleAns = True
					for simple in rule.getSimples():
						if self.__traceDerives(simple.getSimpleVal()) == False:
							ruleAns = False
							break
					if ruleAns == False:
						rule.setDerives(False)
					else:
						rule.setDerives(True)

	def __traceDerives(self , derivesstr):
		if derivesstr == "λ":
			# find lambda 
			return True
		else:
			for terminal in self.__TerminalList:
				if terminal == derivesstr:
					# find terminal
					return False
			for nonterminal in self.__NonTerminalList:
				if nonterminal == derivesstr:
					for tree in self.__treeList:
						if tree.getRoot().getRootVal() == derivesstr:
							for rule in tree.getRoot().getRules():
								ruleAns = False
								if rule.getDerives() == None:
									simpleAns = True
									for simple in rule.getSimples():
										if self.__traceDerives(simple.getSimpleVal()) == False:
											simpleAns = False
											break
									if simpleAns == False:
										rule.setDerives(False)
									else:
										rule.setDerives(True)
									if simpleAns == True:
										ruleAns = True	
								elif rule.getDerives() == True:
									ruleAns = True
								else:
									print("There have a bug in rulenode derives")
							return ruleAns
		# not lambda & terminal & nonterminal Bug??
		return None


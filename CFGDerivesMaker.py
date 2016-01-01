from CFGTree import CFGTree
from Node import simpleNode

class CFGDerivesMaker:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		self.__treeList = CFGTreeList
		self.__NonTerminalList = NonTerminalList
		self.__TerminalList = TerminalList
		self.__FindRuleDerives()
		#self.__PrintDerives()

		# debug part
	def __PrintDerives(self):
		for tree in self.__treeList:
			for rule in tree.get_root().get_rules():
				print(rule.get_rule_value()+"\n")
				print("Derives:  "+str(rule.is_derive_lambda())+"\n")

		# code part
	def __FindRuleDerives(self):
		for tree in self.__treeList:
			for rule in tree.get_root().get_rules():
				if rule.is_derive_lambda() == None:
					ruleAns = True
					for simple in rule.get_simple():
						if self.__traceDerives(simple.get_simple_value()) == False:
							ruleAns = False
							break
					if ruleAns == False:
						rule.set_derive_lambda(False)
					else:
						rule.set_derive_lambda(True)

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
						if tree.get_root().get_root_value() == derivesstr:
							for rule in tree.get_root().get_rules():
								ruleAns = False
								if rule.is_derive_lambda() == None:
									simpleAns = True
									for simple in rule.get_simple():
										if self.__traceDerives(simple.get_simple_value()) == False:
											simpleAns = False
											break
									if simpleAns == False:
										rule.set_derive_lambda(False)
									else:
										rule.set_derive_lambda(True)
									if simpleAns == True:
										ruleAns = True	
								elif rule.is_derive_lambda() == True:
									ruleAns = True
								else:
									print("There have a bug in rulenode derives")
							return ruleAns
		# not lambda & terminal & nonterminal Bug??
		return None


from __future__ import print_function
from CFGTree import CFGTree
from Node import ruleNode

class CFGScanner:
	def __init__(self, file_name):
		self.__rule = []
		self.__nonterminal = []
		self.__rule_tree = []
		self.__ReadCFG(file_name)
		self.__CutNonTerminal()
		self.__BuildRuleTree()

	def __ReadCFG(self, file_name):
		cfg_file = open(file_name, 'r')
		while True:
			line = cfg_file.readline().strip()
			if not line:
				break
			else:
				self.__rule.append(line.replace("lamda","λ"))
		cfg_file.close()

	def __CutNonTerminal(self):
		for content in self.__rule:
			rule = content.split(" ")
			if rule[1] != "|":
				self.__nonterminal.append(rule[1])

	def __BuildRuleTree(self):
		root = ""
		tree = None
		for content in self.__rule:
			content_split = content.split(" ")
			right_rule = self.__GetRightpart(content)
			if content_split[1] !=  "|":
				if root != "":
					self.__rule_tree.append(tree)
				root = content_split[1]
				tree = CFGTree(root)
				tree.SetRule(right_rule)
			else:
				tree.SetRule(right_rule)
		self.__rule_tree.append(tree)
			

	def __GetRightpart(self, rule):
		rule = rule.replace("|", ">")
		pos = rule.find(">")
		rrule = rule[pos+2:len(rule)]
		return rrule
	
	#get variable part

	def GetNonTerminal(self):
		res = self.__nonterminal
		return res

	#debug part

	def PrintCFG(self):
		print("CFG: ")
		for content in self.__rule:
			print("rule %s"% content)

	def PrintNonTerminal(self):
		print("Nonterminal: ")
		print(self.__nonterminal)

	def PrintRuleTree(self):
		for element in self.__rule_tree:
			element.PrintTree()


test = CFGScanner("CFG1")
test.PrintCFG()
test.PrintNonTerminal()
test.PrintRuleTree()


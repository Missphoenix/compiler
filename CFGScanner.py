from __future__ import print_function

class CFGScanner:
	def __init__(self, file_name):
		self.__rule = []
		self.__nonterminal = []
		self.__ReadCFG(file_name)
		self.__CutNonTerminal()

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

	def __GetRightpart(self, rule):
		rule = rule.replace("|", ">")
		pos = rule.find(">")
		rrule = rule[pos:len(rule)]
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


test = CFGScanner("CFG")
test.PrintCFG()
test.PrintNonTerminal()


from CFGTree import CFGTree
from Node import simpleNode

class CFGProcessor:
	def __init__(self , CFGtreeList , NonterminalList):
		self.__treelist = CFGtreeList
		self.__nonterminallist = NonterminalList
		self.__terminallist = []
		self.__memory = _Memory()
		self.__SimpleSpecific()
		

	def __SimpleSpecific(self):
		for tree in self.__treelist:
			for rule in tree.getRoot().getRules():
				simplelist = []
				for simple in rule.getSimples():
					if self.__CheckLambda(simple.getSimpleVal()) == False:
						if self.__CheckTerminalAll(simple.getSimpleVal()) == False:
							nodelist = self.__CheckTerminal(simple.getSimpleVal() , self.__memory)
							simplelist.extend(nodelist)
							self.__memory.resetData()
						else:
							simplelist.append(simple.getSimpleVal())
					else:
						simplelist.append("λ")
				rule.ResetSimples()
				for simple in simplelist:
					rule.AddSimple(simple)
			tree.PrintTree()

	def __CheckTerminalAll(self , simplestr):
		return self.__CheckNonTerminal(simplestr)

	def __CheckTerminal(self , simplestr , memory):
		nodelist = []
		terminal , oldstr , index = memory.getData()
		if len(simplestr)-1 >= index:
			if terminal is None:
				nowstr = simplestr[index]
				if self.__CheckNonTerminal(nowstr) == True:
					memory.ChangeData(False , nowstr , index+1)
				else:
					memory.ChangeData(True , nowstr , index+1)
				nodelist = nodelist + self.__CheckTerminal(simplestr , memory)
			elif terminal is False:
				nowstr = simplestr[index]
				nowstr = oldstr + nowstr
				if self.__CheckNonTerminal(nowstr) == True:
					memory.ChangeData(False , nowstr , index+1)
				else:
					memory.ChangeData(None , None , index)
					nodelist.append(oldstr)
				nodelist = nodelist + self.__CheckTerminal(simplestr , memory)
			elif terminal is True:
				nowstr = simplestr[index]
				if self.__CheckNonTerminal(nowstr) == True:
					memory.ChangeData(None , None , index)
					nodelist.append(oldstr)
				else:
					nowstr = oldstr + nowstr
					memory.ChangeData(True , nowstr , index+1)
				nodelist = nodelist + self.__CheckTerminal(simplestr , memory)
			else:
				print("Error Check variable in memory")
		else:
			if terminal is False:
				nodelist.append(oldstr)
			elif terminal is True:
				nodelist.append(oldstr)
			else:
				print("Error Check variable in memory")
		return nodelist

	def __CheckNonTerminal(self , checkstr):
		for nonterminal in self.__nonterminallist:
			index = 0 
			for char in checkstr:  
				if len(nonterminal)-1 >= index: 
					if char == nonterminal[index]:
						index = index + 1
					else:
						break
			if len(checkstr)-1 < index:
				return True
		return False

	def __CheckLambda(self , simplestr):
		if simplestr == 'λ':
			return True
		else:
			return False

class _Memory:
	def __init__(self):
		self.__IsTerminal = None
		self.__Str = None
		self.__index = 0

	def ChangeData(self , newterminal , newstr , newindex):
		self.__IsTerminal = newterminal
		self.__Str = newstr
		self.__index = newindex

	def resetData(self):
		self.__IsTerminal = None
		self.__Str = None 
		self.__index = 0

	def getData(self):
		return self.__IsTerminal , self.__Str , self.__index
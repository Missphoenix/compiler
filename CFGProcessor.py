from CFGTree import CFGTree
from Node import simpleNode

class CFGProcessor:
	def __init__(self, CFG_tree_list, non_terminal_list):
		self.__treelist = CFG_tree_list
		self.__nonterminallist = non_terminal_list
		self.__terminallist = []
		self.__memory = _Memory()
		self.__simple_specific()
		self.__build_terminal_list()
		#print(self.get_terminal_list())

	def get_terminal_list(self):
		terminallist = self.__terminallist
		return terminallist

	def __simple_specific(self):
		for tree in self.__treelist:
			for rule in tree.get_root().get_rules():
				simplelist = []
				for simple in rule.get_simple():
					if self.__is_lambda(simple.get_simple_value()) == False:
						if self.__check_terminal_all(simple.get_simple_value()) == False:
							nodelist = self.__check_terminal(simple.get_simple_value() , self.__memory)
							simplelist.extend(nodelist)
							self.__memory.reset_data()
						else:
							simplelist.append(simple.get_simple_value())
					else:
						simplelist.append("λ")
				rule.reset_simples()
				for simple in simplelist:
					rule.add_simple(simple)
			#tree.print_tree()


	def __build_terminal_list(self):
		EndExist = False
		for tree in self.__treelist:
			for rule in tree.get_root().get_rules():
				for simple in rule.get_simple():
					simplestr = simple.get_simple_value()
					if simplestr != "λ":
						if not simplestr[0].isupper():
							if simplestr == "$":
								EndExist = True
							else:
								if simplestr not in self.__terminallist:
									self.__terminallist.append(simplestr)
		if EndExist == True:
			self.__terminallist.append("$")


	def __check_terminal_all(self, simplestr):
		return self.__check_non_terminal(simplestr)

	def __check_terminal(self, simplestr, memory):
		nodelist = []
		terminal , oldstr , index = memory.get_data()
		if len(simplestr)-1 >= index:
			if terminal is None:
				nowstr = simplestr[index]
				if self.__check_non_terminal(nowstr) == True:
					memory.change_data(False , nowstr , index+1)
				else:
					memory.change_data(True , nowstr , index+1)
				nodelist = nodelist + self.__check_terminal(simplestr , memory)
			elif terminal is False:
				nowstr = simplestr[index]
				nowstr = oldstr + nowstr
				if self.__check_non_terminal(nowstr) == True:
					memory.change_data(False , nowstr , index+1)
				else:
					memory.change_data(None , None , index)
					nodelist.append(oldstr)
				nodelist = nodelist + self.__check_terminal(simplestr , memory)
			elif terminal is True:
				nowstr = simplestr[index]
				if self.__check_non_terminal(nowstr) == True:
					memory.change_data(None , None , index)
					nodelist.append(oldstr)
				else:
					nowstr = oldstr + nowstr
					memory.change_data(True , nowstr , index+1)
				nodelist = nodelist + self.__check_terminal(simplestr , memory)
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

	def __check_non_terminal(self, checkstr):
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

	def __is_lambda(self , simplestr):
		if simplestr == "λ":
			return True
		else:
			return False

class _Memory:
	def __init__(self):
		self.__is_termial = None
		self.__string = None
		self.__index = 0

	def change_data(self, newterminal, newstr, newindex):
		self.__is_termial = newterminal
		self.__string = newstr
		self.__index = newindex

	def reset_data(self):
		self.__is_termial = None
		self.__string = None 
		self.__index = 0

	def get_data(self):
		return self.__is_termial, self.__string, self.__index
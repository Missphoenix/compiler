from CFGTree import CFGTree
from Node import simpleNode

class CFGFirstsMaker:
	def __init__(self, CFGTreeList):
		self.__treelist = CFGTreeList
		self.__BuildFirsts()

	def __BuildFirsts(self):
		for tree in self.__treelist:
			for rule in tree.get_root().get_rules():
				simple_list = [simple.get_simple_value() for simple in rule.get_simple()]
				rule.set_firsts(self.__FindFirsts(simple_list))

	def __FindFirsts(self, simple_list):
		waiting_list = simple_list
		first_list = []

		if len(waiting_list) == 0:
			return first_list
		elif self.__isTerminal(waiting_list[0]):
			if self.__isLambda(waiting_list[0]):
				waiting_list.remove(waiting_list[0])
				for element in self.__FindFirsts(waiting_list):
					if element in first_list:
						continue
					else:
						first_list.append(element)
			elif not waiting_list[0] in first_list:
				first_list.append(waiting_list[0])
		else:
			for tree in self.__treelist:
				if tree.get_root().get_root_value() == waiting_list[0]:
					for rule in tree.get_root().get_rules():
						derives_list = [simple.get_simple_value() for simple in rule.get_simple()]
						derives_list.extend(waiting_list[1:len(waiting_list)])
						for element in self.__FindFirsts(derives_list):
							if element in first_list:
								continue
							else:
								first_list.append(element)
		return first_list

	def __isLambda(self, str):
		if str == "λ":
			return True
		else:
			return False

	def __isTerminal(self, str):
		if str[0].isupper():
			return False
		else:
			return True
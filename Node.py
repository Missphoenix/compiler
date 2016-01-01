class rootNode:
	def __init__(self , root):
		self.__rootVal = root
		self.__rules = []

	def add_rule(self, rule, number):
		rulenode = ruleNode(rule , len(self.__rules)+1, number)
		self.__rules.append(rulenode)

	def get_rules(self):
		rules = self.__rules
		return rules

	def get_root_value(self):
		res = self.__rootVal
		return res

	def print_root(self):
		print("Root: %s"% (self.__rootVal))
		for element in self.__rules:
			element.print_rule()
		print()


class ruleNode:
	def __init__(self , rule , index, number):
		self.__ruleVal = rule
		self.__ruleIndex = index
		self.__ruleNumber = int(number)
		self.__simples = []
		self.__Derives = None
		self.__firsts = []
		self.__follows = []
		self.__ans = []

	def add_simple(self, simple):
		simplenode = simpleNode(simple , len(self.__simples)+1)
		self.__simples.append(simplenode)

	def add_follow(self, follow):
		self.__follows.append(follow)

	def reset_simples(self):
		self.__simples.clear()

	def set_derive_lambda(self , derives):
		self.__Derives = derives

	def set_firsts(self, firsts):
		self.__firsts = firsts

	def set_answer(self, list):
		self.__ans = list

	def get_rule_value(self):
		res = self.__ruleVal
		return res

	def get_simple(self):
		simples = self.__simples
		return simples

	def is_derive_lambda(self):
		derives = self.__Derives
		return derives

	def get_first(self):
		firsts = self.__firsts
		return firsts

	def get_follow(self):
		follows = self.__follows
		return follows

	def get_rule_number(self):
		ruleNumber = self.__ruleNumber
		return ruleNumber

	def get_answer(self):
		ans = self.__ans
		return ans

	def print_rule(self):
		print(" Rule number %d: %s; derive λ: %s; first: %s; follow: %s; ans: %s;"% (self.__ruleNumber, self.__ruleVal, self.__Derives, self.__firsts, self.__follows, self.__ans))
		for node in self.__simples:
			node.print_simple()
		print()

class simpleNode:
	def __init__(self , simple , index):
		self.__simpleVal = simple
		self.__simpleIndex = index

	def get_simple_value(self):
		res = self.__simpleVal
		return res

	def print_simple(self):
		print("  Simple index %d: %s"% (self.__simpleIndex, self.__simpleVal), end =" ")
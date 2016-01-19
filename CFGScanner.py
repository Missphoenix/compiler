from __future__ import print_function
from CFGTree import CFGTree
from Node import ruleNode

class CFGScanner:
	def __init__(self, file_name):
		self.__rule = []
		self.__nonterminal = []
		self.__rule_tree = []
		self.__read_CFG(file_name)
		self.__cut_non_terminal()
		self.__build_rule_tree()
		self.__build_tree_simple()

	def __read_CFG(self, file_name):
		cfg_file = open(file_name, 'r')
		while True:
			line = cfg_file.readline().strip()
			if not line:
				break
			else:
				self.__rule.append(line.replace("lamda","λ"))
		cfg_file.close()

	def __cut_non_terminal(self):
		for content in self.__rule:
			rule = content.split(" ")
			if rule[1] != "|":
				self.__nonterminal.append(rule[1])

	def __build_rule_tree(self):
		root = ""
		tree = None
		for content in self.__rule:
			content_split = content.split(" ")
			right_rule = self.__get_right_part(content)
			if content_split[1] !=  "|":
				if root != "":
					self.__rule_tree.append(tree)
				root = content_split[1]
				tree = CFGTree(root)
				tree.set_rule(right_rule, content_split[0])
			else:
				tree.set_rule(right_rule, content_split[0])
		self.__rule_tree.append(tree)

	def __build_tree_simple(self):
		for tree in self.__rule_tree:
			if self.__is_nonterminal_char():
				for rule in tree.get_root().get_rules():
					rule_list = [char for char in rule.get_rule_value()]
					for simple in rule_list:
						rule.add_simple(simple)
			else:
				for rule in tree.get_root().get_rules():
					rule_list = rule.get_rule_value().split(" ")
					for simple in rule_list:
						rule.add_simple(simple)

	def __get_right_part(self, rule):
		rule = rule.replace("|", ">")
		pos = rule.find(">")
		rrule = rule[pos+2:len(rule)]
		return rrule

	def __is_nonterminal_char(self):
		for non_ter in self.__nonterminal:
			if len(non_ter) != 1:
				return False
		return True
	
	#get variable part

	def get_non_terminal(self):
		res = self.__nonterminal
		return res

	def get_rule_tree(self):
		res = self.__rule_tree
		return res

	#debug part

	def print_CFG(self):
		print("CFG: ")
		for content in self.__rule:
			print("rule %s"% content)

	def print_non_terminal(self):
		print("Nonterminal: ")
		print(self.__nonterminal)

	def print_rule_tree(self):
		for element in self.__rule_tree:
			element.print_tree()
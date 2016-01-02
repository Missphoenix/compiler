from CFGTree import CFGTree
from Node import simpleNode

class CFGFollowMaker:
	def __init__(self, CFG_tree_list):
		self.__tree_list = CFG_tree_list
		self.__find_rule_follow()

	def __find_rule_follow(self):
		for tree in self.__tree_list:
			for rule in tree.get_root().get_rules():
				if rule.is_derive_lambda() == True:
					self.__find_rule_start(tree.get_root().get_root_value(), rule)

	def __find_rule_start(self, root, rule):
		find_follow = _FollowMemory()
		find_follow.set_rule_node(rule)
		find_follow.set_root(root)
		for tree in self.__tree_list:
			# find all node append root
			for rule in tree.get_root().get_rules():
				find_flag = False
				find_list = _FollowList()
				strlist = []
				for simple in rule.get_simple():
					if find_flag == False:
						if simple.get_simple_value() == root:
							find_flag = True
							find_list.set_rule_root(tree.get_root().get_root_value())
					else:
						if self.__is_lambda(simple.get_simple_value()) == False:
							strlist.append(simple.get_simple_value())
				if find_flag == True:
					find_list.add_check_string(strlist)
					find_follow.add_follow_list(find_list)
		self.__follow_decision(find_follow)
					
	def __follow_decision(self, follow_memory):
		follow_lists = follow_memory.get_follow_lists()

		for followlist in follow_lists:
			self.__check_follow(followlist, follow_memory)
			for follow in followlist.get_find_follows():
				follow_memory.add_find_follow(follow)
		for follow in follow_memory.get_find_follows():
			follow_memory.get_rule_node().add_follow(follow)
	
	def __check_follow(self, follow_list, follow_memory):
		last_list = follow_list.get_check_strings()
		new_list = []
		for last_follow in last_list:
			if len(last_follow) == 0:
				if follow_memory.get_root() != follow_list.get_rule_root():
					# to see it's recall
					for tree in self.__tree_list:
						new_function_list = _FollowList()
						find_new_function = False
						for rule in tree.get_root().get_rules():
							find_flag = False
							strlist = []
							for simple in rule.get_simple():
								if find_flag == False:
									if simple.get_simple_value() == follow_list.get_rule_root():
										find_flag = True
										find_new_function = True
										new_function_list.set_rule_root(tree.get_root().get_root_value())
								else:
									if self.__is_lambda(simple.get_simple_value()) == False:
										strlist.append(simple.get_simple_value())
							if find_flag == True:
								if len(strlist) > 0:
									new_function_list.add_check_string(strlist)
						if find_new_function == True:
							follow_memory.add_follow_list(new_function_list)
							find_new_function = False
			else:
				first_follow_string = last_follow[0]
				if self.__is_terminal(first_follow_string) == True:
					follow_list.add_find_follow(first_follow_string)
				else:
					recursive_flag = False
					if first_follow_string == follow_memory.get_root():
						recursive_flag = True
					for tree in self.__tree_list:
						if first_follow_string == tree.get_root().get_root_value():
							for rule in tree.get_root().get_rules():
								newstr = []
								for simple in rule.get_simple():
									if self.__is_lambda(simple.get_simple_value()) == False:
										newstr.append(simple.get_simple_value())
								newstr = self.__copy_follow_string(newstr, last_follow)
								if recursive_flag != True or len(newstr) > 0:
									new_list.append(newstr)
		if len(new_list) > 0:
			# to see it's done yet
			follow_list.change_check_strings(new_list)	
			self.__check_follow(follow_list, follow_memory)

	def __copy_follow_string(self, newstr, oldstr):
		copystr = oldstr
		firstIgnore = False
		for copy in copystr:
			if firstIgnore == False:
				firstIgnore = True
			else:
				newstr.append(copy)
		return newstr

	def __is_lambda(self, str):
		if str == "λ":
			return True
		else:
			return False

	def __is_terminal(self, str):
		if str[0].isupper():
			return False
		else:
			return True

class _FollowMemory:
	def __init__(self):
		self.__rule_nodes = None
		self.__follow_root = None
		self.__follow_lists = []
		self.__find_follows = []

	def set_rule_node(self, rulenode):
		self.__rule_nodes = rulenode

	def set_root(self, root):
		self.__follow_root = root

	def add_follow_list(self, followlist):
		self.__follow_lists.append(followlist)

	def add_find_follow(self, element):
		if element not in self.__find_follows:
			self.__find_follows.append(element)

	def get_rule_node(self):
		res = self.__rule_nodes
		return res

	def get_root(self):
		res1 = self.__follow_root
		return res1

	def get_follow_lists(self):
		res = self.__follow_lists
		return res

	def get_find_follows(self):
		res = self.__find_follows
		return res
						
class _FollowList:
	def __init__(self):
		self.__rule_root = None
		self.__check_strings = []
		self.__find_follows = []

	def set_rule_root(self, root):
		self.__rule_root = root

	def add_check_string(self, checkstr):
		self.__check_strings.append(checkstr)

	def add_find_follow(self, followstr):
		self.__find_follows.append(followstr)

	def change_check_strings(self, check_strings):
		self.__check_strings = check_strings

	def get_rule_root(self):
		res = self.__rule_root
		return res

	def get_check_strings(self):
		res = self.__check_strings
		return res

	def get_find_follows(self):
		res = self.__find_follows
		return res
		


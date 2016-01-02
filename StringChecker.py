class StringChecker:
	def __init__(self, user_str, tree_list, ter_list, nonter_list, table):
		self.__user_str = user_str
		self.__tree_list = tree_list
		self.__ter_list = ter_list
		self.__nonter_list = nonter_list
		self.__prediect_table = table
		self.__parse_stack = []
		self.__successful = True
		self.__accept_checker()

	def __accept_checker(self):
		self.__parse_stack.append(self.__nonter_list[0])
		while self.__successful == True and len(self.__parse_stack) > 0:
			if self.__parse_stack[len(self.__parse_stack)-1] in self.__nonter_list:
				self.__append_rule_to_parse_stack(self.__parse_stack[len(self.__parse_stack)-1] , self.__user_str.get_node() )
			if self.__parse_stack[len(self.__parse_stack)-1] in self.__ter_list:
				self.__check_string()
		if self.__successful == True:
			print("Accept")

	def __check_string(self):
		if self.__parse_stack[len(self.__parse_stack)-1] == self.__user_str.get_node():
			self.__parse_stack.pop(len(self.__parse_stack)-1)
			self.__user_str.next_pointer()
		else:
			print("Error")
			self.__successful = False

	def __append_rule_to_parse_stack(self, parsechar, userchar):
		predict_rule = self.__prediect_table[parsechar][userchar]
		predict_list = []
		if predict_rule == -1:
			# if no rule in predict table
			print("Error")
			self.__successful = False
			return
		else:
			rule = self.__find_rule(predict_rule)
			for simple in rule.get_simple():
				if self.__is_lambda(simple.get_simple_value()) == False:
					predict_list.append(simple.get_simple_value())
			predict_list.reverse()
			self.__parse_stack.pop(len(self.__parse_stack)-1)
			self.__parse_stack = self.__parse_stack + predict_list
			print("Apply:" , end=" ")
			print(predict_rule)

	def __find_rule(self, rule_num):
		found = False
		return_rule = None
		for tree in self.__tree_list:
			if found == False:
				for rule in tree.get_root().get_rules():
					if rule.get_rule_number() == rule_num:
						return_rule = rule
						found = True
						break
		return return_rule

	def __is_lambda(self, str):
		if str == "λ":
			return True
		else:
			return False
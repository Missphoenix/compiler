from CFGTree import CFGTree
from Node import simpleNode

class CFGDerivesMaker:
	def __init__(self , CFG_tree_list , non_terminal_list , terminal_list):
		self.__tree_list = CFG_tree_list
		self.__non_terminal_list = non_terminal_list
		self.__terminal_list = terminal_list
		self.__set_rules_derives_lambda()
		#self.__print_derives()

	# debug part
	def __print_derives(self):
		for tree in self.__tree_list:
			for rule in tree.get_root().get_rules():
				print(rule.get_rule_value()+"\n")
				print("Derives:  "+str(rule.is_derive_lambda())+"\n")

	# code part
	def __set_rules_derives_lambda(self):
		for tree in self.__tree_list:
			for rule in tree.get_root().get_rules():
				if rule.is_derive_lambda() == None:
					derives_lambda = True
					for simple in rule.get_simple():
						if self.__trace_derives(simple.get_simple_value()) == False:
							derives_lambda = False
							break
					rule.set_derive_lambda(derives_lambda)

	def __trace_derives(self , derivesstr):
		if derivesstr == "λ":
			# find lambda 
			return True
		else:
			for terminal in self.__terminal_list:
				if terminal == derivesstr:
					# find terminal
					return False
			for nonterminal in self.__non_terminal_list:
				if nonterminal == derivesstr:
					for tree in self.__tree_list:
						if tree.get_root().get_root_value() == derivesstr:
							# find the rule start from derives string
							for rule in tree.get_root().get_rules():
								ruleAns = False
								if rule.is_derive_lambda() == None:
									# rule doesn't set derive lambda
									# find it and set it
									simpleAns = True
									for simple in rule.get_simple():
										if self.__trace_derives(simple.get_simple_value()) == False:
											simpleAns = False
											break
									rule.set_derive_lambda(simpleAns)
									if simpleAns == True:
										ruleAns = True	
								elif rule.is_derive_lambda() == True:
									ruleAns = True
								else:
									print("There have a bug in rulenode derives")
							return ruleAns
		# not lambda & terminal & nonterminal Bug??
		return None


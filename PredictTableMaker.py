from CFGTree import CFGTree
from Node import simpleNode

class PredictTableMaker:
	def __init__(self, CFGTree, NonTerminalList, TerminalList):
		self.__treelist = CFGTree
		self.__nonterminallist = NonTerminalList.copy()
		self.__terminallist = TerminalList.copy()
		self.__predicttable = {}
		self.__answer_productor()
		self.__table_establish()
		#self.print_table()

	def __table_initialize(self):
		for nonterminal in self.__nonterminallist:
			innertable = {}
			for terminal in self.__terminallist:
				innertable[terminal] = -1
			self.__predicttable[nonterminal] = innertable

	def __table_establish(self):
		self.__table_initialize()
		for tree in self.__treelist:
			root = tree.get_root().get_root_value()
			for rule in tree.get_root().get_rules():
				rule_number = rule.get_rule_number()
				for ans in rule.get_answer():
					self.__predicttable[root][ans] = rule_number

	def __answer_productor(self):
		for tree in self.__treelist:
			for rule in tree.get_root().get_rules():
				answers = rule.get_first().copy()
				for element in rule.get_follow():
					if not element in answers:
						answers.append(element)
				rule.set_answer(answers)

	def get_predict_table(self):
		res = self.__predicttable
		return res

	def print_table(self):
		print("Predict Table:")
		for nonterminal in self.__nonterminallist:
			print("{%s: "% nonterminal, end = " ")
			for terminal in self.__terminallist:
				print("[%s: %d]"%(terminal, self.__predicttable[nonterminal][terminal]), end = " ")
			print("}")
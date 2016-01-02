from CFGTree import CFGTree
from CFGProcessor import *
from CFGScanner import *
from CFGPredictor import *
from InputTokens import InputTokens
from StringChecker import *

class System:
	def __init__(self):
		self.__filepath = ""
		self.__scanner = None
		self.__processor = None
		self.__predictor = None
		self.__input = None
		self.__checker = None
		self.__set_check = False
	
	def show(self):
		article = "======================================\nWelcome to Top-down parser\nHere is your option:\n\t1.Store CFG file\n\t2.Put string\n\t3.Print tree\n\t4.Print predict table\n\t5.Quit\n======================================"
		print(article)

	def check(self):
		choice = input("Your Choice: ")
		if choice == '1':
			# init the CFG scanner
			self.__filepath = input("Your file path: ")
			self.__scanner = CFGScanner(self.__filepath)
			
			# test processor
			treelist = self.__scanner.get_rule_tree()
			nonterlist = self.__scanner.get_non_terminal()
			self.__processor = CFGProcessor(treelist , nonterlist)
			terlist = self.__processor.get_terminal_list()
			self.__predictor = CFGPredictor(treelist , nonterlist , terlist)
			
			# end
			self.__set_check = True
			return choice , True
		elif choice == '2':
			# init the CFG processor
			if self.__set_check == False:
				print("You didn't set the CFG")
				return choice , False
			userstr = input("Your String: ")
			terlist = self.__processor.get_terminal_list()
			self.__input = InputTokens(userstr, terlist)
			if not self.__input.tokens_check():
				return choice, False
			self.__input.get_token_list().reset_pointer()
			self.__checker = StringChecker(self.__input.get_token_list() , self.__scanner.get_rule_tree() , self.__processor.get_terminal_list() , self.__scanner.get_non_terminal() , self.__predictor.get_predict_table())
			return choice , True
		elif choice == '3':
			# print tree
			treelist = self.__scanner.get_rule_tree()
			for tree in treelist:
				tree.print_tree()
			return choice , True
		elif choice == '4':
			# print table
			self.__predictor.print_table()
			return choice , True
		elif choice == '5':
			# quit
			return choice , True
		else:
			print("We don't have this option")
			return choice , False
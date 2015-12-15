from CFGTree import CFGTree
from CFGProcessor import *
from CFGScanner import *
from CFGPredictor import *
from InputTokens import InputTokens

class System:
	def __init__(self):
		self.__filepath = ""
		self.__scanner = None
		self.__processor = None
		self.__predictor = None
		self.__input = None

	
	def show(self):
		article = "======================================\nWelcome to Top-down parser\nHere is your option:\n\t1.Store CFG file\n\t2.Put String\n\t3.Quit\n======================================"
		print(article)

	def Check(self):
		choice = input("Your Choice: ")
		if choice == '1':
			# init the CFG scanner
			self.__filepath = input("Your file path: ")
			self.__scanner = CFGScanner(self.__filepath)
			
			# test processor
			treelist = self.__scanner.GetRuleTree()
			nonterlist = self.__scanner.GetNonTerminal()
			self.__processor = CFGProcessor(treelist , nonterlist)
			terlist = self.__processor.getTerminalList()
			self.__predictor = CFGPredictor(treelist , nonterlist , terlist)
			for tree in treelist:
				tree.PrintTree()
			self.__predictor.PrintTable()
			# end
			return choice , True
		elif choice == '2':
			# init the CFG processor
			userstr = input("Your String: ")
			terlist = self.__processor.getTerminalList()
			self.__input = InputTokens(userstr, terlist)
			if not self.__input.TokensCheck():
				print("There is an invalid tokens in input string")
				return choice, False
			self.__input.PrintTokens()
			return choice , True
		elif choice == '3':
			# quit
			return choice , True
		else:
			print("We don't have this shit")
			return choice , False
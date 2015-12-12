from CFGTree import CFGTree
from CFGProcessor import *
from CFGScanner import *

class System:

	def show(self):
		article = "======================================\nWelcome to Top-down parser\nHere is your option:\n\t1.Store CFG file\n\t2.Put String\n\t3.Quit\n======================================"
		print(article)

	def Check(self):
		choice = input("Your Choice: ")
		if choice == '1':
			# init the CFG scanner
			filepath = input("Your file path: ")
			scanner = CFGScanner(filepath)
			
			# test processor
			treelist = scanner.GetRuleTree()
			nonterlist = scanner.GetNonTerminal()
			processor = CFGProcessor(treelist , nonterlist)
			# end
			return choice , True
		elif choice == '2':
			# init the CFG processor
			userstr = input("Your String: ")
			print(userstr)
			return choice , True
		elif choice == '3':
			# quit
			return choice , True
		else:
			print("We don't have this shit")
			return choice , False
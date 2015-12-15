from CFGDerivesMaker import *
from CFGFirstsMaker import CFGFirstsMaker
from CFGFollowMaker import CFGFollowMaker
from PredictTableMaker import PredictTableMaker

class CFGPredictor:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		derivesMaker = CFGDerivesMaker(CFGTreeList , NonTerminalList , TerminalList)
		firstsMaker = CFGFirstsMaker(CFGTreeList)
		followMaker = CFGFollowMaker(CFGTreeList)
		self.__tableMaker = PredictTableMaker(CFGTreeList, NonTerminalList, TerminalList)

	def PrintTable(self):
		self.__tableMaker.PrintTable()
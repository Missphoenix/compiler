from CFGDerivesMaker import *
from CFGFirstsMaker import CFGFirstsMaker
from CFGFollowMaker import CFGFollowMaker
from PredictTableMaker import PredictTableMaker

class CFGPredictor:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		self.__derivesMaker = CFGDerivesMaker(CFGTreeList , NonTerminalList , TerminalList)
		self.__firstsMaker = CFGFirstsMaker(CFGTreeList)
		self.__followMaker = CFGFollowMaker(CFGTreeList)
		self.__tableMaker = PredictTableMaker(CFGTreeList, NonTerminalList, TerminalList)

	def PrintTable(self):
		self.__tableMaker.PrintTable()

	def getPredictTable(self):
		res = self.__tableMaker.getPredictTable()
		return res
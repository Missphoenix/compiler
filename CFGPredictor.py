from CFGDerivesMaker import *
from CFGFirstsMaker import CFGFirstsMaker
from PredictTableMaker import PredictTableMaker

class CFGPredictor:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		derivesMaker = CFGDerivesMaker(CFGTreeList , NonTerminalList , TerminalList)
		firstsMaker = CFGFirstsMaker(CFGTreeList)
		tableMaker = PredictTableMaker(CFGTreeList, NonTerminalList, TerminalList)
from CFGDerivesMaker import *
from CFGFirstsMaker import CFGFirstsMaker

class CFGPredictor:
	def __init__(self , CFGTreeList , NonTerminalList , TerminalList):
		derivesMaker = CFGDerivesMaker(CFGTreeList , NonTerminalList , TerminalList)
		firstsMaker = CFGFirstsMaker(CFGTreeList)
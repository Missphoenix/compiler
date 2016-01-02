from CFGDerivesMaker import *
from CFGFirstsMaker import CFGFirstsMaker
from CFGFollowMaker import CFGFollowMaker
from PredictTableMaker import PredictTableMaker

class CFGPredictor:
	def __init__(self, CFG_tree_list, non_terminal_list, terminal_list):
		self.__derive_maker = CFGDerivesMaker(CFG_tree_list , non_terminal_list , terminal_list)
		self.__first_maker = CFGFirstsMaker(CFG_tree_list)
		self.__follow_maker = CFGFollowMaker(CFG_tree_list)
		self.__table_maker = PredictTableMaker(CFG_tree_list, non_terminal_list, terminal_list)

	def print_table(self):
		self.__table_maker.print_table()

	def get_predict_table(self):
		res = self.__table_maker.get_predict_table()
		return res
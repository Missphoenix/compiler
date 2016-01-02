from ListandPointer import ListandPointer

class InputTokens:
	def __init__(self, InputStr, TerminalList):
		self.__input = InputStr.strip()
		self.__tokens = ListandPointer()
		self.__terminallist = TerminalList.copy()
		self.__cut_tokens()

	def __cut_tokens(self):
		if not self.__have_space():
			for char in self.__input:
				self.__tokens.add_node(char)
		else:
			for token in self.__input.split(" "):
				self.__tokens.add_node(token)

	def tokens_check(self):
		error_flag = False
		for index in range(self.__tokens.length()):
			self.__tokens.set_pointer(index)
			if not self.__tokens.get_node() in self.__terminallist:
				print("Token %d: \"%s\" is not in TerminalList"% (index+1, self.__tokens.get_node()))
				error_flag = True
		return not error_flag

	def print_tokens(self):
		self.__tokens.print_list()

	def get_token_list(self):
		res = self.__tokens
		return res

	def __have_space(self):
		for char in self.__input:
			if char.isspace():
				return True
		return False
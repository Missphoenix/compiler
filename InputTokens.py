from ListandPointer import ListandPointer

class InputTokens:
	def __init__(self, InputStr, TerminalList):
		self.__input = InputStr.strip()
		self.__tokens = ListandPointer()
		self.__terminallist = TerminalList.copy()
		self.__CutTokens()

	def __CutTokens(self):
		if not self.__HaveSpace():
			for char in self.__input:
				self.__tokens.AddNode(char)
		else:
			for token in self.__input.split(" "):
				self.__tokens.AddNode(token)

	def TokensCheck(self):
		error_flag = False
		for index in range(self.__tokens.getLength()):
			self.__tokens.setPointer(index)
			if not self.__tokens.getNode() in self.__terminallist:
				print("Token %d: \"%s\" is not in TerminalList"% (index+1, self.__tokens.getNode()))
				error_flag = True
		return not error_flag

	def PrintTokens(self):
		self.__tokens.PrintList()

	def getTokenList(self):
		res = self.__tokens
		return res

	def __HaveSpace(self):
		for char in self.__input:
			if char.isspace():
				return True
		return False
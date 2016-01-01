class StringChecker:
	def __init__(self , userstr , treelist , terlist , nonterlist , table):
		self.__userstr = userstr
		self.__treelist = treelist
		self.__terlist = terlist
		self.__nonterlist = nonterlist
		self.__prediectTable = table
		self.__ParseStack = []
		self.__Successful = True
		self.__CheckAccept()

	def __CheckAccept(self):
		self.__ParseStack.append(self.__nonterlist[0])
		while self.__Successful == True and len(self.__ParseStack) > 0:
			if self.__ParseStack[len(self.__ParseStack)-1] in self.__nonterlist:
				self.__AppendStringToParseStack(self.__ParseStack[len(self.__ParseStack)-1] , self.__userstr.getNode() )
			if self.__ParseStack[len(self.__ParseStack)-1] in self.__terlist:
				self.__CheckString()
		if self.__Successful == True:
			print("Accept")

		
	def __CheckString(self):
		if self.__ParseStack[len(self.__ParseStack)-1] == self.__userstr.getNode():
			self.__ParseStack.pop(len(self.__ParseStack)-1)
			self.__userstr.IterablePointer()
		else:
			print("Error")
			self.__Successful = False

	def __AppendStringToParseStack(self , parsechar , userchar):
		predictAnswer = self.__prediectTable[parsechar][userchar]
		predictlist = []
		Found = False
		for tree in self.__treelist:
			if Found == False:
				for rule in tree.get_root().get_rules():
					if rule.get_rule_number() == predictAnswer:
						for simple in rule.get_simple():
							if self.__isLambda(simple.get_simple_value()) == False:
								predictlist.append(simple.get_simple_value())
						Found = True
						break
		predictlist.reverse()
		self.__ParseStack.pop(len(self.__ParseStack)-1)
		self.__ParseStack = self.__ParseStack + predictlist
		print("Apply:" , end=" ")
		print(predictAnswer)

	def __isLambda(self, str):
		if str == "λ":
			return True
		else:
			return False
from CFGTree import CFGTree
from Node import simpleNode

class CFGFollowMaker:
	def __init__(self , CFGTreeList):
		self.__treeList = CFGTreeList
		self.__FindRuleFollow()

	def __FindRuleFollow(self):
		for tree in self.__treeList:
			for rule in tree.get_root().get_rules():
				if rule.is_derive_lambda() == True:
					self.__FindRuleStart(tree.get_root().get_root_value() , rule)


	def __FindRuleStart(self , followRoot , RuleNode):
		FindFollow = _FollowMemory()
		FindFollow.setRuleNode(RuleNode)
		FindFollow.setRoot(followRoot)
		for tree in self.__treeList:
			for rule in tree.get_root().get_rules():
				FindRuleStart = False
				FindList = _FollowList()
				strlist = []
				for simple in rule.get_simple():
					if FindRuleStart == False:
						if simple.get_simple_value() == followRoot:
							FindRuleStart = True
							FindList.setRuleRoot(tree.get_root().get_root_value())
					else:
						if self.__isLambda(simple.get_simple_value()) == False:
							strlist.append(simple.get_simple_value())
				if FindRuleStart == True:
					FindList.AddCheckStr(strlist)
					FindFollow.AddFollowList(FindList)
		self.__FollowDecision(FindFollow)
					
	def __FollowDecision(self , FollowMemory):
		follow_lists = FollowMemory.getFollowLists()

		for followlist in follow_lists:
			self.__CheckFollow(followlist , FollowMemory)
			for follow in followlist.getFindFollows():
				FollowMemory.AddFindFollow(follow)
		for follow in FollowMemory.getFindFollows():
			FollowMemory.getRuleNode().add_follow(follow)
	
	def __CheckFollow(self , FollowList , FollowMemory):
		lastList = FollowList.getCheckStrs()
		newList = []
		for lastFollow in lastList:
			#print(lastFollow , end = ", ")
			if len(lastFollow) == 0:
				if FollowMemory.get_root() != FollowList.getRuleRoot():
					# to see it's recall
					for tree in self.__treeList:
						NewFunctionList = _FollowList()
						FindNewFunction = False
						for rule in tree.get_root().get_rules():
							FindRuleStart = False
							strlist = []
							for simple in rule.get_simple():
								if FindRuleStart == False:
									if simple.get_simple_value() == FollowList.getRuleRoot():
										FindRuleStart = True
										FindNewFunction = True
										NewFunctionList.setRuleRoot(tree.get_root().get_root_value())
								else:
									if self.__isLambda(simple.get_simple_value()) == False:
										strlist.append(simple.get_simple_value())
							if FindRuleStart == True:
								if len(strlist) > 0:
									NewFunctionList.AddCheckStr(strlist)
						if FindNewFunction == True:
							FollowMemory.AddFollowList(NewFunctionList)
							FindNewFunction = False
			else:
				firstfollowstr = lastFollow[0]
				if self.__isTerminal(firstfollowstr) == True:
					FollowList.AddFindFollow(firstfollowstr)
				else:
					Recursive = False
					if firstfollowstr == FollowMemory.get_root():
						Recursive = True
					for tree in self.__treeList:
						if firstfollowstr == tree.get_root().get_root_value():
							for rule in tree.get_root().get_rules():
								newstr = []
								for simple in rule.get_simple():
									if self.__isLambda(simple.get_simple_value()) == False:
										newstr.append(simple.get_simple_value())
								newstr = self.__copyFollowstr(newstr , lastFollow)
								if Recursive != True or len(newstr) > 0:
									newList.append(newstr)
		if len(newList) > 0:
			# to see it's done yet
			FollowList.ChnageCheckStrs(newList)	
			self.__CheckFollow(FollowList , FollowMemory)

	def __copyFollowstr(self , newstr , oldstr):
		copystr = oldstr
		firstIgnore = False
		for copy in copystr:
			if firstIgnore == False:
				firstIgnore = True
			else:
				newstr.append(copy)
		return newstr


	def __isLambda(self, str):
		if str == "λ":
			return True
		else:
			return False

	def __isTerminal(self, str):
		if str[0].isupper():
			return False
		else:
			return True

class _FollowMemory:
	def __init__(self):
		self.__RuleNode = None
		self.__FollowRoot = None
		self.__FollowLists = []
		self.__FindFollows = []

	def setRuleNode(self , rulenode):
		self.__RuleNode = rulenode

	def setRoot(self , root):
		self.__FollowRoot = root

	def AddFollowList(self , followlist):
		self.__FollowLists.append(followlist)

	def AddFindFollow(self , element):
		if element not in self.__FindFollows:
			self.__FindFollows.append(element)

	def getRuleNode(self):
		res = self.__RuleNode
		return res

	def get_root(self):
		res1 = self.__FollowRoot
		return res1

	def getFollowLists(self):
		res = self.__FollowLists
		return res

	def getFindFollows(self):
		res = self.__FindFollows
		return res
						
class _FollowList:
	def __init__(self):
		self.__RuleRoot = None
		self.__CheckStrs = []
		self.__FindFollows = []


	def setRuleRoot(self , root):
		self.__RuleRoot = root

	def AddCheckStr(self , checkstr):
		self.__CheckStrs.append(checkstr)

	def AddFindFollow(self , followstr):
		self.__FindFollows.append(followstr)

	def ChnageCheckStrs(self , CheckStrs):
		self.__CheckStrs = CheckStrs

	def getRuleRoot(self):
		res = self.__RuleRoot
		return res

	def getCheckStrs(self):
		res = self.__CheckStrs
		return res

	def getFindFollows(self):
		res = self.__FindFollows
		return res
		


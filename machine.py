class LexicalAnalyzer:
	def __init__(self, string):
		self.string = string + ' '
		self.cc = ''
		self.state = 0
		self.tokenLexic = []

	def __decideState(self):
		if (self.state is 0):
			nc = {
				"p" : 11,
				"q" : 11,
				"r" : 11,
				"s" : 11,
				"n" : 21,
				"a" : 31,
				"o" : 41,
				"x" : 51,
				"i" : 68,
				"t" : 71,
				"(" : 91,
				")" : 101,
			}
			try:
				self.state =  nc[self.cc]
				return True
			except KeyError:
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 11) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(1)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 21) :
			if (self.cc is "o"):
				self.state = 22
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 22) :
			if (self.cc is "t"):
				self.state = 23
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 23) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(2)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 31) :
			if (self.cc is "n"):
				self.state = 32
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 32) :
			if (self.cc is "d"):
				self.state = 33
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 33) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(3)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 41) :
			if (self.cc is "r"):
				self.state = 42
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 42) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(4)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 51) :
			if (self.cc is "o"):
				self.state = 52
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 52) :
			if (self.cc is "r"):
				self.state = 53
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 53) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(5)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 68) :
			if (self.cc is "f"):
				self.state = 69
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 61) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(6)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 61) :
			if (self.cc is "f"):
				self.state = 81
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 81) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(8)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 71) :
			if (self.cc is "h"):
				self.state = 72
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 73) :
			if (self.cc is "e"):
				self.state = 74
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 74) :
			if (self.cc is "n"):
				self.state = 75
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 75) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(7)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 91) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(9)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 101) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(10)
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False

	def generateTokenLexic(self):
		n = len(self.string)
		i = 0
		self.state = 0
		self.cc = self.string[i]
		cont = self.__decideState()
		while cont :
			i = i + 1
			if (i < n):
				self.cc = self.string[i]
				cont = self.__decideState()
			else :
				cont = False

		return self.tokenLexic
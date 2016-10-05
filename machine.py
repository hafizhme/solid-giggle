class LexicalAnalyzer:
	def __init__(self, string):
		self.str = string
		self.state = 0

	def decideState(self):
		if (self.state > 0) and (self.state <= 10):
			if (self.cc is " "):
				self.state =  0
		elif (self.state is 0):
			nc = {
				"p" : 1,
				"q" : 1,
				"r" : 1,
				"s" : 1,
				"n" : 21,
				"a" : 31,
				"o" : 41,
				"x" : 51,
				"i" : 68,
				"t" : 71,
				"(" : 9,
				")" : 10,
			}
			try:
				self.state =  nc[self.cc]
			except KeyError:
				self.state =  99
		elif (self.state is 21):
			if (self.cc is "o"):
				self.state =  22
			else:
				self.state =  99
		elif (self.state is 22):
			if (self.cc is "t"):
				self.state =  2
			else:
				self.state =  99
		elif (self.state is 31):
			if (self.cc is "n"):
				self.state =  32
			else:
				self.state =  99
		elif (self.state is 32):
			if (self.cc is "d"):
				self.state =  3
			else:
				self.state =  99
		elif (self.state is 41):
			if (self.cc is "r"):
				self.state =  4
			else:
				self.state =  99
		elif (self.state is 51):
			if (self.cc is "o"):
				self.state =  52
			else:
				self.state =  99
		elif (self.state is 52):
			if (self.cc is "r"):
				self.state =  5
			else:
				self.state =  99
		elif (self.state is 68):
			if (self.cc is "f"):
				self.state =  69
			else:
				self.state =  99
		elif (self.state is 69):
			if (self.cc is "f"):
				self.state =  8
			elif (self.cc is " "):
				self.state =  6
			else:
				self.state =  99
		elif (self.state is 71):
			if (self.cc is "h"):
				self.state =  72
			else:
				self.state =  99

		elif (self.state is 72):
			if (self.cc is "e"):
				self.state =  73
			else:
				self.state =  99
		elif (self.state is 73):
			if (self.cc is "n"):
				self.state =  7
			else:
				self.state =  99

	def generateTokenLexic(self):
		self.state = 0
		tokenLexic = []
		for self.cc in self.str:
			print(self.cc)
			self.decideState()
			print(self.state)
			if (0 < self.state) and (self.state <= 10):
				tokenLexic.append(self.state)
			elif (self.state is 99):
				tokenLexic.append("ERROR")
				break
		return tokenLexic
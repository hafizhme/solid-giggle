from dataType import Stack

class LexicalAnalyzer:
	def __init__(self, string):
		self.string = string + ' '
		self.cc = ''
		self.state = 0
		self.stack = Stack()
		self.tokenLexic = []

	def __decideState(self):
		if (self.state is 0):
			nc = {
				"p" : 1,
				"q" : 1,
				"r" : 1,
				"s" : 1,
				"n" : 3,
				"a" : 7,
				"o" : 11,
				"x" : 14,
				"i" : 18,
				"t" : 21,
				"(" : 28,
				")" : 30,
				" " : 0
			}
			try:
				self.state =  nc[self.cc]
				return True
			except KeyError:
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 1) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(1) # q2
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 3) :
			if (self.cc is "o"):
				self.state = 4
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 4) :
			if (self.cc is "t"):
				self.state = 5
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 5) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(2) # q6
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 7) :
			if (self.cc is "n"):
				self.state = 8
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 8) :
			if (self.cc is "d"):
				self.state = 9
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 9) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(3) # q10
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 11) :
			if (self.cc is "r"):
				self.state = 12
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 12) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(4) # q13
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 14) :
			if (self.cc is "o"):
				self.state = 15
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 15) :
			if (self.cc is "r"):
				self.state = 16
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 16) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(5) # q17
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 18) :
			if (self.cc is "f"):
				self.state = 19
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 19) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(6) # q20
				return True
			elif (self.cc is "f"):
				self.state = 26
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 21) :
			if (self.cc is "h"):
				self.state = 22
				return True
			else:
				self.tokenLexic.append("ERROR")
		elif (self.state is 22) :
			if (self.cc is "e"):
				self.state = 23
				return True
			else:
				self.tokenLexic.append("ERROR")
		elif (self.state is 23) :
			if (self.cc is "n"):
				self.state = 24
				return True
			else:
				self.tokenLexic.append("ERROR")
		elif (self.state is 24) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(7) # q25
				return True
			else:
				self.tokenLexic.append("ERROR")
		elif (self.state is 26) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(8) #q27
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 28) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(9) #29
				return True
			else :
				self.tokenLexic.append("ERROR")
				return False
		elif (self.state is 30) :
			if (self.cc is " "):
				self.state = 0
				self.tokenLexic.append(10) #q31
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
	
	def parser(self):
		n = len(self.tokenLexic)
		i = 0
		self.cc = self.tokenLexic[i]
		if self.cc is 'ERROR':
				return False
		self.stack.push(self.cc)
		i += 1

		while i < n:
			self.cc = self.tokenLexic[i]

			if self.cc is 'ERROR':
				return False
			
			if self.stack.peek() is 1:
				if self.cc is 2 or self.cc is 3 or self.cc is 4 or self.cc is 5 or self.cc is 7 or self.cc is 8 or self.cc is 10:
					self.stack.pop()
				self.stack.push(self.cc)
			elif self.stack.peek() is 2 or self.stack.peek() is 3 or self.stack.peek() is 4 or self.stack.peek() is 5 or self.stack.peek() is 6 or self.stack.peek() is 7 or self.stack.peek() is 8 or self.stack.peek() is 9:
				if self.cc is 1 or self.cc is 9:
					self.stack.pop()
				self.stack.push(self.cc)
			elif self.stack.peek() is 10:
				if self.cc is 3 or self.cc is 4 or self.cc is 5 or self.cc is 7 or self.cc is 8 or self.cc is 10:
					self.stack.pop()
				self.stack.push(self.cc)

			print(self.stack.size())
			i += 1

		if self.stack.peek() is 10 or self.stack.peek() is 1:
			self.stack.pop()
			return self.stack.isEmpty()
		return False

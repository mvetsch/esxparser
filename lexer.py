#!/bin/python

class Token(object):
	def __init__(self):
		self.str = 'unspecified token'

	def __repr__(self):
		return str(self.str)

class AssignmentToken(Token):
	def __init__(self):
		self.str = '=' 

class CommaToken(Token):
	def __init__(self):
		self.str = ',' 

class OpenCurlyBracketToken(Token):
	def __init__(self):
		self.str = '{' 

class CloseCurlyBracketToken(Token):
	def __init__(self):
		self.str = '}' 

class OpenBracketToken(Token):
	def __init__(self):
		self.str = '(' 

class CloseBracketToken(Token):
	def __init__(self):
		self.str = ')' 

class OpenTagBracketToken(Token):
	def __init__(self):
		self.str = '<' 

class CloseTagBracketToken(Token):
	def __init__(self):
		self.str = '>' 

class OpenArrayBracketToken(Token):
	def __init__(self):
		self.str = '[' 

class CloseArrayBracketToken(Token):
	def __init__(self):
		self.str = ']'

class IdentifierToken(Token):
	def __init__(self, id):
		self.str = id

class StringToken(Token):
	def __init__(self, value):
		self.str = value

class EOFToken(Token):
	def __init__(self):
		self.str = "EOF" 


class esxlexer(object):
	def __init__(self, inputString):
		self.text = inputString
		self.index = 0

	def printAll(self):
		print self.text

	def getToken(self):
		if not self.index < len(self.text):
			return EOFToken()

		char = self.text[self.index]
		self.index += 1

		if char.isspace():
			return self.getToken()

		if char == '=':
			return AssignmentToken()
		
		if char == ',':
			return CommaToken()
		
		if char == '{': 
			return OpenCurlyBracketToken()

		if char == '}':
			return CloseCurlyBracketToken()

		if char == '(':
			return OpenBracketToken()

		if char == ')' : 
			return CloseBracketToken()

		if char == '<':
			return OpenTagBracketToken()

		if char == '>': 
			return CloseTagBracketToken()	
		
		if char == '[':
			return OpenArrayBracketToken()
		
		if char == ']':
			return CloseArrayBracketToken()

		if char == '"':
			# value
			val = ''
			char = self.text[self.index]
			self.index += 1 
			while char != '"':
				val += char 
				char = self.text[self.index]
				self.index += 1
			
			return StringToken(val)

		if char == '\'':
			# value 
			val = ''
			char = self.text[self.index]
			self.index += 1
			while char != '\'':
				val += char
				char = self.text[self.index]
				self.index += 1
			
			return StringToken(val)

		if char.isalpha() or char.isdigit() or char == '-' :
			# identifier
			ident = char
			char = self.text[self.index]
			self.index +=1
			while char.isalpha() or char == '.' or char.isdigit():
				ident += char
				char = self.text[self.index]
				self.index += 1
			
			self.index -= 1
			return IdentifierToken(ident)


		return Token()

	

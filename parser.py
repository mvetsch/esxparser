#!/bin/python



""" 
grammar:
	S -> datasets eof
	datasets -> dataset datasets
	datasets -> epsilon
	dataset -> ( ident ) content
	content -> [ q ] 
	content ->  { data } 
	q -> q , q
	q -> content
	data-> assignment data
	data-> epsilon
	assignment -> ident = value, 
	value -> string
	value -> ident
	value -> dataset
	value -> < ident > 

""" 

from lexer import *

class esxparser(object):
	def __init__(self, lexer):
		self.lexer = lexer
		self.nxtToken = self.lexer.getToken()

	def isType(self, token, tokentype):
		if not isinstance(token, tokentype):
			raise Exception("parse error , Expected another Token than -> " + str(token))
		

	def token(self):
		self.actToken = self.nxtToken
		self.nxtToken = self.lexer.getToken()	
		return self.actToken
				
	def nextToken(self):
		return self.nxtToken
	
	def S(self):
		r = self.datasets()
		self.isType(self.token(), EOFToken)
		return r 

	def datasets(self):
		resultList = []
 
		resultList.append(self.dataset())
	
		if isinstance(self.nxtToken, OpenBracketToken):
			resultList.extend(self.datasets())

		return resultList

	def dataset(self):
		result = {}
		self.isType(self.token(), OpenBracketToken)
		t = self.token()	
		self.isType(t, IdentifierToken)
		result['__name'] = str(t)
		self.isType(self.token(), CloseBracketToken)

		self.content(result)
		return result
		
	def content(self, result): 
	
		t = self.nextToken()
		if isinstance(t, IdentifierToken):
			if 'null' == str(t):
				self.token()
				return 

		if isinstance(t, OpenArrayBracketToken) :
			self.token()
			result['array'] = self.q()
			self.isType(self.token(), CloseArrayBracketToken)
			return
		
		if isinstance(t, OpenBracketToken):
			result['dataset'] = self.dataset()
			return


		self.isType(t, OpenCurlyBracketToken)
		self.token() 
	
		self.data(result)
		
		self.isType(self.token(), CloseCurlyBracketToken)

		return result

	def q(self):
		result = [] 
		index = 0
	
		while not isinstance (self.nextToken(), CloseArrayBracketToken):
			result.append({ })
			self.content(result[index]) 
			
			if isinstance(self.nextToken(), CommaToken):
				index += 1
				t = self.token()

		return result
					
	def data(self, result):
		
		ide = self.token()
		self.isType(ide, IdentifierToken)
		self.isType(self.token(), AssignmentToken)
		
		result[str(ide)] = self.value()

		self.isType(self.token(), CommaToken)

		if isinstance(self.nextToken(), IdentifierToken):
			self.data(result)

	def value(self): 
			
		t = self.nextToken()

		if isinstance(t, StringToken):
			return str(self.token())

		if isinstance(t, IdentifierToken):
			return self.token()

		if isinstance(t, OpenTagBracketToken):
			self.token()
			ident = self.token()
			self.isType(ident, IdentifierToken)
			self.isType(self.token(), CloseTagBracketToken)
			return '< ' + str(ident) + ' >' ;
		
		return self.dataset()
		
	

def printr(arr, level=0): 
	for k, v in arr.iteritems():
		#print v.__class__.__name__  str(len(v))
		if isinstance(v, list):
			print tab(level) + str(k) + ' : ' 
			for i in range(0, len(v)):
				print tab(level) + str(i) + ' = ' 	
				self.printr(v[i], level+1)
		elif isinstance(v, dict):
			print tab(level) + str(k) + " : " 	
			self.printr(v, level+1)
		else: 
			print tab(level) + str(k) + " : " + str(v)

def tab(n):
	val =''
	for a in range(0,n):
		val+= '\t'
	return val


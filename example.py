#!/bin/python

from lexer import esxlexer
from parser import esxparser


inputfile = open('input', 'r')
input = inputfile.read()

l = esxlexer(input)
p = esxparser(l)

resultarray = p.S()
print resultarray['name']
print resultarray['files']['vmPathName']


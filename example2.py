#!/bin/python

from lexer import esxlexer
from parser import esxparser
from parser import *

inputfile = open('input2', 'r')
input = inputfile.read()

l = esxlexer(input)
p = esxparser(l)

resultarray = p.S()

printr(resultarray)

print resultarray[0]['url']
print resultarray[0]['vmfs']['name']
print resultarray[1]['array'][0]['dataset']['key']

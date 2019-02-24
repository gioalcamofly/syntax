#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import nltk
from nltk import load_parser

cp = load_parser('gramatica_base.fcfg', trace=2)


infile = open('textos.txt')
# Mostramos por pantalla lo que leemos desde el fichero
for line in infile:
    print(line)
    tokens=line.split()
    trees = cp.parse(tokens)
    for tree in trees: print(tree)
infile.close()

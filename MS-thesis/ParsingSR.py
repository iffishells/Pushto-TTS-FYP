import nltk
from nltk.tree import Tree
from nltk.parse.generate import generate
from nltk.tree import *
import os
from nltk.tokenize import word_tokenize
import os
import xml.etree.ElementTree as etree


path = (r'C:\Users\Mustafa\Desktop\Thesis\updated\dict')
for filename in os.listdir(path):
    xmlD = etree.parse(R"C:\Users\Mustafa\Desktop\Thesis\updated\dict\\" + filename)
    root = xmlD.getroot()
    for child in root:
        nodetext = child.find('word').text
        if(nodetext == -1):
            test=child.findtext("./int/gram")
            test=test.replace("[", "")
            test=test.replace("]", "")
            test=test.replace("-", " ")
            test=test.replace("=", " ")
            q = word_tokenize(test)
        
##grammar1 = nltk.CFG.fromstring("""
##S -> NP VP
##NP -> N | H N | H N N | P P | N N | AP
##VP -> V | V H | H V | Ad V | N H V | N H H V
##AP -> H N | NN N
##PP -> N H | H N | H N H
##N -> path
##""")

grammar1 = nltk.CFG.fromstring("""
 اسس -> اَس  | ح اَس | ح اَس اَس | اَس اَس | اسف
 س -> فس اسس
 اسس -> اَس  | ح اَس | ح اَس اَس | اَس اَس
 فس -> ف | ح ف | ف ح | ص ف | اَس ح ف | اَس ح ح ف
 اسف" -> عډد اَس"
 پپ ->  اَس ح | ح اَس | ح اَس ح
 
 اسس -> اَس  | ح اَس | ح اَس اَس | اَس اَس

AP -> H N | NN N
N -> path
""")

sr_parser = nltk.ShiftReduceParser(grammar1)
sen = input("Enter your sentence: ")
sent = sen.split()
for tree in sr_parser.parse(sent):
    print(tree)




######################################################################3

##
##grammar1 = nltk.CFG.fromstring("""
##  S -> NP VP
##  VP -> V NP | V NP PP | ADJ V | ADJ NP V 
##  PP -> P NP
##  V -> "saw" | "ate" | "walked" | "شو"
##  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | N
##  Det -> "a" | "an" | "the" | "my"
##  N -> "man" | "dog" | "cat" | "telescope" | "park" | "apple" | "يوسف"
##  P -> "in" | "on" | "by" | "with"
##  ADJ -> "غلے" | "is"
##  """)
##
###sr_parser = nltk.RecursiveDescentParser(grammar1)
##sr_parser = nltk.ShiftReduceParser(grammar1)
##sen = input("Enter your sentence: ")
##sent = sen.split()
##for tree in sr_parser.parse(sent):
##    print(tree)



#sr_parse = nltk.ShiftReduceParser(grammar1, trace=2)
#"John saw Bob"
#the dog saw a man on the park
# يوسف غلے شو
# a man ate an apple 


########################################################################


import nltk
import re
import string
from nltk.tokenize import word_tokenize
import os
import xml.etree.ElementTree as etree



sen = open('Corpus2 Frequently Used.txt',encoding="utf8").read()
print("\n")
u = word_tokenize(sen)
##print(u)
##print("\n")

for i in word_tokenize(sen):
        print(i)
print("###########################")


path = "/dict"
for filename in os.listdir(path):    
    xmlD = etree.parse(R"C:\Users\Mustafa\Desktop\Thesis\updated\dict\\" + filename)
    root = xmlD.getroot()
    count = 0
    for a in word_tokenize(sen):
        for child in root:
            nodetext = child.find('word').text
            #if(nodetext.find(a) != -1):
            if(nodetext == a):
                print(a)  
                count += 1
                print(count)



# summary : 
this code just checking the and count the word existing 
in the curret dictt xml files









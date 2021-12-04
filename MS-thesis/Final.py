import nltk
import re
import string
from nltk.tokenize import word_tokenize
import os
import xml.etree.ElementTree as etree

##sen = open('ao-kana.txt',encoding="utf8").read()
##print("\n")
##u = word_tokenize(sen)
###print(u)
####print("\n")
##
##for i in word_tokenize(sen):
##        print(i)
##print("###########################")
##
##
##path = (r'C:\Users\Mustafa\Desktop\Thesis\Dataset\New folder')
##for filename in os.listdir(path):    
##        xmlD = etree.parse(filename)
##        root = xmlD.getroot()
##
##        count = 0
##        
##        if filename.endswith(".xml"):
##            print("XXX")
##        else:
##            for a in word_tokenize(sen):
##                for child in root:
##                    nodetext = child.find('word').text
##                    if(nodetext.find(a) != -1):
##                        print(a)  
##                        count += 1
##                        #print(count)
##
######        Average = count/969
######        print(Average)



sen = open('Corpus2 Frequently Used.txt',encoding="utf8").read()
print("\n")
u = word_tokenize(sen)
##print(u)
##print("\n")

for i in word_tokenize(sen):
        print(i)
print("###########################")


path = (r'C:\Users\Mustafa\Desktop\Thesis\updated\dict\\')
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












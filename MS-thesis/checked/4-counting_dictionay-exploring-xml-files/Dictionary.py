import os, sys
import xml.etree.ElementTree as etree

base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)



##xmlD = etree.parse("3.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("\n")
##
##
##
##
##
##xmlD = etree.parse("4.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("\n")
##
##
##
##
##
##
##
##
##
##
##
##xmlD = etree.parse("5.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("\n")
##
##
##
##
##
##
##
##
##
##xmlD = etree.parse("6.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("/n")
##
##
##
##
##
##
##xmlD = etree.parse("7.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("/n")
##
##
##
##
##
##
##
##
##
##xmlD = etree.parse("1581-1744-1608.xml")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("/n")
##
##
##
##


##
##xmlD = etree.parse("1575-1593-1588")
##root = xmlD.getroot()
##
##for child in root:
##    for children in child:
##        print(children.text)
##    print("\n")
##
##for pron in root.iter('pron'):
##    print(pron.tag, pron.text, pron.attrib)
##
##for gram in root.iter('gram'):
##    print(gram.tag, gram.text, gram.attrib)
##
##for poem in root.iter('poem'):
##    print(poem.tag, poem.text, poem.attrib)
##    print("/n")
##






##xmlD = etree.parse("1575-1593-1588")
##root = xmlD.getroot()


path = '/home/iffishells/Pictures/Pushto-TTS-FYP/MS-thesis/dict'
for filename in os.listdir(path):
    tree = etree.parse("/home/iffishells/Pictures/Pushto-TTS-FYP/MS-thesis/dict/" + filename)
    root = tree.getroot()
    
    for child in root:
        for children in child:
            print(children.text)
            #print("\n")
    #print("\n")
    for gram in root.iter('gram'):
        print(gram.tag, gram.text, gram.attrib)
        print("\n")        








##
##sen = open('ao-kana.txt',encoding="utf8").read()
##print("\n")
##
##path = (r'C:\Users\Mustafa\Desktop\Thesis\Dataset\New folder')
##
##for i in word_tokenize(sen):
##     if(path != -1):
##          for filename in os.listdir(path):
##               xmlD = etree.parse(filename)
##               root = xmlD.getroot()
##               count = 0
##               for child in root:
##                    nodetext = child.find('word').text
##               if(nodetext.find(i) != -1):
##                    print(i)  
##                    count += 1
##                    print(count)
##               
######        Average = count/969
######        print(Average)





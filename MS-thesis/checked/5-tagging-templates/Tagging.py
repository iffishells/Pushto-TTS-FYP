
################################################################
import nltk
from nltk.tokenize import word_tokenize
import os
import xml.etree.ElementTree as etree

##sen = input("Enter Your sentence - ")
##print(sen)
##print("\n")
##print(word_tokenize(sen))
##print("\n")
###s = word_tokenize(sen)[0]
##roman = etree.parse('1583-32-1707')
##
##root = roman.getroot()
##
##for a in word_tokenize(sen):
##    for child in root:
##        nodetext = child.find('word').text
##        #if(nodetext.find(a) != -1):
##        if(nodetext == a):
##            print("WORD", '\n',a,'\n')
##            test=child.findtext("./int/gram")
##            q = word_tokenize(test)
##            for t in q:
##                if(t == "اس"):
##                    print("Noun")
##                elif(t == "مذ"):
##                    print("Masculine")
##                elif(t == "ج"):
##                    print("Plural")
##                elif(t == "مو"):
##                    print("Femenine")





############################################################################



#########

sen = 'نه زه به سبا ته وخته پا نه څېږممذ'
print(sen)
print("\n")
print(word_tokenize(sen))
print("\n")

path = "/home/iffishells/Pictures/Pushto-TTS-FYP/MS-thesis/dict/"


for a in word_tokenize(sen):
    #print(a)
    for filename in os.listdir(path):
        #print(a+" in "+filename)
        #os.chdir(r'C:\Users\Mustafa\Desktop\Thesis\Dataset\Newfolder')
        #print(r"C:\Users\Mustafa\Desktop\Thesis\Dataset\Newfolder\dict\\" + filename) 
        xmlD = etree.parse("/home/iffishells/Pictures/Pushto-TTS-FYP/MS-thesis/dict/" + filename)
        root = xmlD.getroot()
        for child in root:
            nodetext = child.find('word').text
            #if(nodetext.find(a) != -1):
            if(nodetext == a):
                test=child.findtext("./int/gram")
                test=test.replace("[", "")
                test=test.replace("]", "")
                test=test.replace("-", " ")
                test=test.replace("=", " ")
                test=test.replace("(", " ")
                test=test.replace(")", " ")
                q = word_tokenize(test)
##                count = 0
                for t in q:
                    print("inside looop")
                    print(a,'\t','\t',t)
                    if(t == "اَس"):
                        print("Noun")
                    elif(t == "مذ"):
                        print("Masculine")
                    elif(t == "ج"):
                        print("Plural")
                    elif(t == "مؤ"):
                        print("Femenine")
                    elif(t == "ص"):
                        print("Adjective")
                    elif(t == "فاعل"):
                        print("Adverb")
                    elif(t == "فعل"):
                        print("Verb")
                    elif(t == "حا"):
                        print("Present")
                    elif(t == "ما"): 
                        print("Past")
                    elif(t == "وا"):
                        print("Singular")
##                    count += 1


######################################################################                    
#تته :-  ( ت + تَه ) [  پ ، اس ، مؤ ، وا، ج: تتې ] کم نوره ، کم روښانه هغه ډيوه يا بتۍ چې رڼا ئې کمه کړے شوې وي ـ
#for child in root:
 #   nodetext = child.find('word').text
  #  for a in word_tokenize(sen):
   #     if(nodetext.find(a) != -1):
    #        print("XXX", nodetext)
      #      print("Word", nodetext)
      #      #test=child.findall("./int/gram")
       #     test=child.findtext("./int/gram")
       #     #print(test)
        #    q = word_tokenize(test)
            #print(q)
            
        #for t in q:
        #    if(t == "اس"):
        #        print("Noun")
        #    elif(t == "مذ"):
        #        print("Masculine")
        #    elif(t == "ج"):
        #        print("Plural")
        #    elif(t == "مو"):
        #        print("Femenine")

            



##list_Pas =["مذ","اس","ج","مو"]
##list_Eng =["Noun", "Singular", "Plural","Femenine"]
##
###for l in list_Pas:
##if(list_Pas[0] == "مذ"):
##    print("Noun")
            
















            
##            if(t.text == "[اس-مذ]"):
##                print("Noun Masculine")
##            elif(t.text == "[عف تر-اس-مذ]"):
##                print("Noun")
##            elif(t.text == "[عپ تر+اس+ج]"):
##                print("Noun")
##            
##            elif(t.text == "[عفر تر-اس-مذ]"):
##                print("Noun Masculine")
##            elif(t.text == "[عپ تر+اس+ج]"):
##                print("Noun Plural")
##            elif(t.text == "[عف تر-صف]"):
##                print("Noun Plural")
##            elif(t.text == "[ع ف-تر-اس-مذ]"):
##                print("Noun Masculine")
##            elif(t.text == ""):
##                print("Noun Plural")
##            elif(t.text == "[اس-مذ-ج— ړے]"):
##                print("Noun Masculine-Plural")
##            elif(t.text == "[اس-مذ-ج:لي]"):
##                print("Noun-Plural")
##            elif(t.text == "[پ تر-اس-مذ]"):
##                print("Noun-Plural")
##            elif(t.text == "[عپ تر-اس-مو-ج:پهې]"):
##                print("Noun-Feminine-Plural")
##            elif(t.text == "[پ تر-اس-مؤ-ج:رې]"):
##                print("Noun-Feminine-Plural")


        
##        list_one =["مذ","اس","ج","مو"]
##        for t in test:
##            if(t.text == "مذ"):
##                print("Masculine")
##            elif(t.text == "اس"):
##                print("Noun")
##            elif(t.text == "ج"):
##                print("abc")




####xmldoc = etree.parse('roman.xml')
####itemlist = xmldoc.getElementsByTagName('word')
####print(len(itemlist))
####print(itemlist[0].attributes['name'].value)
####for s in itemlist:
####    print(s.attributes['name'].value)



###########################################################

##root = etree.parse("roman.xml")
##search = root.findall(".//word/.[@value='waya']")
##print(search)
##
##search[0].attrib
##search[0].tag

###########################################################



####sen = input("Enter Your sentence - ")
####print(sen)
####print("\n")
####print(word_tokenize(sen)[0])
##
##node=etree.fromstring('<a><word>Aslam</word><gram>[Noun]</gram><meaning>talking</meaning></a>')
##
##s = node.findtext('word')
##print(s)
##
##s1= node.findtext('gram')
##print(s1)


#############################################################





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Dec 22 13:20:50 2021

@author: iftikhar

"""
import pandas as pd
import re
import importlib
from importlib import reload

from linguistic_dictionay import Pashto_dictionary
import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize

 

def combining_dicts(filepath_1, filepath_2):
    '''
        Combining_dict is combining the two files for the searching of the
        part of speech tagging

        parameters :
            file_path_1 : file path
            file_path_2 : file path
    '''
    # finding from file 1
    file2 = pd.read_csv(filepath_2,encoding = "utf-8")

    word = list(file2.WORD)

    POS = list(file2.POS)  # part of speech

    if len(word) == len(POS):
        pos_dictionary_2 = {}

        for index in range(len(word)):
            pos_dictionary_2[word[index]] = POS[index].strip()

    # reading from file 2

    file1 = pd.read_excel(filepath_1,encoding = "utf-8")

    words = list(file1.token)
    adjective = list(file1.Adjective)

    if len(words) == len(adjective):
        pos_dictionary_1 = {}
        for index in range(len(words)):
            pos_dictionary_1[words[index]] = adjective[index].strip()

    for index in range(len(words)):
        word.append(words[index])
        POS.append(adjective[index])

    print("lenght of word : {} end lenght of POS :{} ".format(len(word), len(POS)))

    return word, POS


def Normalization(text ,encoding = "utf8"):
    
    '''
        Nommalization function do the normalize the text for removing 
        the special character and non language word and conver the 
        digit into the pashto text
        
        parameter :
                text :  take the pasto text
    '''

    # remove the English character fromt the text

    text = re.sub('[a-zA-Z]', "", text)
    #print("Removed English text : ", text)

    # remove the special character form text

    text = re.sub('[!@#$%^&*(){}-]', "", text)

    print("Removed the special character : ", text)
    
    # repalce the digit in the pasto text
    
        # if counting digits exist in the string
    counting_dic = ['1','2','3','4','5','6','7','8','9','0']
    for digit in counting_dic:
        text = text.replace(digit, Pashto_dictionary(2) )
    
    
    
    return text
    

def tokenization(normalized_text):
    
    # strip the extra space on given normalized text 
    normalized_text= normalized_text.strip()
    #normalized_text = normalized_text.split(' ')
    
    tokens = word_tokenize(normalized_text)
    return tokens




def grammar_to_tag(arg):
    '''
        grammar_to_tag() is also the helping functionn of the linguistic part of
        the program
        
        parameter : it takes one parameter which arge of the full spell of 
        part of speech and it will return the short form of the respective POS
        
        return : it will return None if pos is not contain in the database
                otherwise return the short form
    '''
    switcher={
            "Noun": "N",
            "Verb": "V",
            "Adverb": "ADV",
            "Adjective": "ADJ",
            "Numerical": "NUM",
            "ProNoun" : "PRN",
            "Abbreviation": "N",
            "Interjection" : "INT",
            "Particle" : "RP",
            "Preposition" : "PrP",
            "Postposition" : "PoP",
            "Suffix" : "SUF",
            "Prefix" : "PRF",
            "Conjunction" : "CO"
            }
    return switcher.get(arg,"none")






if __name__ == '__main__':
    print("orginal text : ", "جمال د ګټے خو وو نه، لوږے تندے پرے تېرېدے اتاشه ")
    sent = "جمال  #$%^&د ګټے* خو وو نه felm 1 23mfemp، لوږے تندے پرے تېرېدے اتاشه ABCfn nie pjfeinfep onofe"
    #print(sent.replace("1", "123"))
    #print("Damage Sentance : ", sent)

    tokenization(Normalization(sent))

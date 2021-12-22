#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 07:46:23 2021

@author: ifti
"""

import pandas as pd
import nltk
def POS_tag_From_Database(token):
    ''' POS_tag_From_Database take single parameter which is token in pashto
    and return the respective part of speech tag from the database
    if len(words)==len(adjective) is not equal will return None
    return None if word not present in database
    '''
    
    file_path = "Datasets/Pastho-dictionary(pos).xlsx"
    dictt = pd.read_excel(file_path)

    words = list(dictt.token)
    adjective = dictt.Adjective

    if len(words)==len(adjective):
        pos_dictionary = {}
        for index in range(len(words)):
            pos_dictionary[words[index]] = adjective[index].strip()
    else:
        print("words and respective tag not equal in database path :{}".format(file_path))
        return None

    if token in pos_dictionary:
        return (token , pos_dictionary[token])
    else:
        ## apply some rules on those words whose are present in the database
        pass
    
    
def combining_dicts(self,filepath_1,filepath_2):
    file2 = pd.read_csv(filepath_2)
    word = list(file2.WORD)
    POS = list(file2.POS)
    if len(word)==len(POS):
        pos_dictionary_2 = {}

        for index in range(len(word)):
            pos_dictionary_2[word[index]] = POS[index].strip()
            
        
        
    # file 1
    file1 = pd.read_excel(filepath_1)

    words = list(file1.token)
    adjective = list(file1.Adjective)
    if len(words)==len(adjective):
        pos_dictionary_1 = {}
        for index in range(len(words)):
            pos_dictionary_1[words[index]] = adjective[index].strip()
            
    for index in range(len(words)):
        word.append(words[index])
        POS.append(adjective[index])
    
    
    print("lenght of word : {} end lenght of POS :{} ".format(len(word),len(POS)))
    
    return word ,POS

#now get two list of the words and respective POS
def make_dataframe(self,list_of_word ,list_of_POS):
    
    dict_dataframe = {
        "words" : list_of_word,
        "POS" : list_of_POS
    }
    
    data = pd.DataFrame(dict_dataframe ,index = False ,header=False)
    
    data.to_csv("Pashto_pos_dict.csv",header=True ,index=False)
def Tagging(self,sent,database):
    print("Given sentance : ",sent)
    
    tokenized = nltk.word_tokenize(sent) # just for sake of the moment making token at the space level.
    
    pos_dictionary = {}
    
    words_list = list(database["words"])
    pos_list = list(database["POS"])
    
    for index,word in enumerate(words_list):
        pos_dictionary[word] = pos_list[index]
        
        
#         print("POS Dictionary : ",pos_dictionary)
    print("Tokenized Sentance : ",tokenized)
    

    
    for index,word in enumerate(tokenized):
        print("Index : {} and word : {}".format(index ,word))
        
        if word in pos_dictionary:
            print("found")
            print(pos_dictionary[word])
        else:
            print("Not found : ",word)
        






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 07:31:22 2021

@author: iftikhar
"""

from preprocessing import Normalization
from preprocessing import tokenization
from tagging import Pos_tagging
from IPATranscription import IPA

import importlib
from importlib import reload
from syllables_linguistic import IPA_of_token
from syllables_linguistic import make_syllables

def main_handler(sentance ):
    '''
        main_handler() function is the main function to deal with
        every other moudle and also user input and his choices
        
        parameter :
            it takes only one parameter which is sentance from the user
            and return the speech
        
    '''
    # first normaliza the text of given text

    normalizaed_text = Normalization(sentance)
    print("Normalized Text : ",normalizaed_text)

        
    # tokinzation
    tokenized = tokenization(normalizaed_text)
    print("tokens : ",tokenized)
    

    # now its time to tag the token from part of speeech
    
    
 #   case 0 :
#        Those words contain in the database
#=============================================================================
    for token in range(0,len(tokenized)):
        print("------------",tokenized[token],"-----")
        if Pos_tagging(tokenized[token]) is not None:
            
            print(tokenized[token],Pos_tagging(tokenized[token]))
            
            # for those words that not contain in the database
        else:
            
            # Rule  for new words
                # need improvements for the numerical values in pashto
            if  Pos_tagging(tokenized[token + 1]) in ["Verb" , "Punctuation","Auxiliary verb","Copula verb"]:
                
                print(tokenized[token],"Verb")
            else:
                print(tokenized[token],"Noun")
    
#=============================================================================
    
    # for the syllables
    sentance_syllables = ""
    for token in tokenized:
        print("present token ",token)
        print("IPA of token ",IPA_of_token(token))
        sentance_syllables += make_syllables(IPA_of_token(token)) + "-"
        print(" syllables form : ",make_syllables(IPA_of_token(token)))
    
    print(sentance_syllables)
if __name__ == "__main__":
    #sent = "جمال  #$%^&د ګټے* خو وو نه felm 1 23mfemp، لوږے تندے پرے تېرېدے اتاشه ABCfn nie pjfeinfep onofe"
    doc = open("Datasets/test_corpus.txt", mode="r", encoding="utf-8").read()
    #print(type(doc))
    main_handler(doc)

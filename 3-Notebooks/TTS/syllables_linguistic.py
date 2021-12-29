#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:32:31 2021

@author: ifti
"""
from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipastring import IPAString

    
        

from IPATranscription import IPA
import importlib
from importlib import reload


def IPA_of_token(token):
    '''
        IPA_of_token() is a linguistic function to find the IPA of Pasto letter
        
        parameter : it take a token which actaully a single pashto word
        
        return : it will return the IPA of given pashto word from the lexicon
    '''
    
    # iterate over the each token
    #print("token : {}".format(token))
    ipa = []
    temp =""
    for char in token:
        #print("char : {} , {} ".format(char ,IPA(char)))
        temp = str(IPA(char)).replace("[", "")
        temp = temp.replace("]", "")
        temp = temp.replace(",", "")
        
        if temp =="ʔ":
            print("dump")
            f = open("Datasets/not_available_ipa.txt","+w" ,encoding='utf-8')
            f.write(char)
            f.close()
            
            
        
       # print(temp,len(temp))
        # if more then IPA then we will use first for the time being
        ipa.append(temp)
        #print(ipa)
    return ipa
        
def is_valid_syllable(cv):
    '''
        is_valid_syllable() is helper function of linguistic part
        
        parameter : it will syllables
        
        return : it will return the string to tell you it is valid syllable or not.
    '''
    if cv in ["V","VC","CV","CVC","CCV","CVCC","CCVC","CCCV","CCCVC"]:
        return "Valid syllables"
    else:
        return "Not Valid syllables"


def make_syllables(IPA_list):
    '''
        make_syllables() is the function of linguistic part of the program and
        it will make the syllable of the given IPA
        
        
        paramter : it takes the list of ipa of the token ,
        
        return : it  will return the syllables of the ipa
        
    '''

#=============================================================================
    #reverse_list = reversed(IPA_list)
    ipa_str = ""
    cv_Form =  ""
    
    for char_ipa in range(0,len(IPA_list)):
        #print("ipa :",char_ipa)
        
        if IPA_list[char_ipa] =="None":
            continue
        
        if IPA_list[char_ipa] in  ['əi','ə','u','ɑ','ā','ai','a','i','o','u','e','əi','A','E','I','U','O' ]:
            cv_Form+="V"
            ipa_str += IPA_list[char_ipa]
        
        else:
            #print(char_ipa)
            cv_Form+="C"
            ipa_str += IPA_list[char_ipa] + " "
            
    print(cv_Form)        
    print(is_valid_syllable(cv_Form))
    return ipa_str

# =============================================================================

if __name__ == "__main__":
    print()
    print(make_syllables(IPA_of_token("اړنګمن")))
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
        

def make_syllables(IPA_list):
    ''' Not decided yet'''

    #reverse_list = reversed(IPA_list)
    ipa_str = ""
    
    
    for char_ipa in IPA_list:
        #print("ipa :",char_ipa)
        
        if char_ipa =="None":
            continue
        
        if char_ipa in  ['ā','ai','a','i','o','u','e','əi','A','E','I','U','O' ]:
            
            ipa_str += char_ipa
        
        else:
            print(char_ipa)
            ipa_str += char_ipa + " "
            
            
    #print(ipa_str)
    return ipa_str


if __name__ == "__main__":
    print(IPA_of_token("عقل"))
    print(make_syllables( ['ā', 'q', 'l']))
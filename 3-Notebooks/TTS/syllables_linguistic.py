#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:32:31 2021

@author: ifti
"""
from IPATranscription import IPA
def syllables(token):
    
    # iterate over the each token
    print("token : {}".format(token))
    ipa = []
    temp =""
    for char in token:
        print("char : {} , {} ".format(char ,IPA(char)))
        temp = str(IPA(char)).replace("[", "")
        temp = temp.replace("]", "")
        temp = temp.replace(",", "")
        
        if temp =="ʔ":
            print("dump")
            f = open("Datasets/not_available_ipa.txt","+w" ,encoding='utf-8')
            f.write(char)
            f.close()
            
            
        
        print(temp,len(temp))
        # if more then IPA then we will use first for the time being
        ipa.append(temp)
        print(ipa)
    return ipa
        
        



if __name__ == "__main__":
    syllables("عقل")
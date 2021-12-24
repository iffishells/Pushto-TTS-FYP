#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 05:40:36 2021

@author: ifti
"""
from linguistic_dictionay import Part_of_speech_dictionay

def Pos_tagging(token=None):
    # case 0 
        # if token is none
    
    if token is None:
        print("Error : Token is None")
        return 0
    
    # case 1:
        # if token exist in the database
    # part of speech database
    
    if Part_of_speech_dictionay(token) is not None:
        return Part_of_speech_dictionay(token)
    else:
        return None























if __name__ == "__main__":
    Pos_tagging("ABCD")
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 07:31:22 2021

@author: iftikhar
"""

from preprocessing import Normalization

def user_text(sentance ):
    
    # first normaliza the text of given text

    normalizaed_text = Normalization(sentance)
    print("Normalized Text : ",normalizaed_text)

        
    # tokinzation
    
    




























if __name__ == "__main__":
    sent = "جمال  #$%^&د ګټے* خو وو نه felm 1 23mfemp، لوږے تندے پرے تېرېدے اتاشه ABCfn nie pjfeinfep onofe"

    user_text(sent)

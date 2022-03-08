#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:02:06 2021

@author: ifti
"""
import pandas as pd
def  Pashto_dictionary(num , encoding = "utf-8") :
    '''
        Pashto_dictionary() is the functin to convert the counting digit into
        the Pashto text form. Pashto_dictionary() covering the only 1 to 9 digit
        
        parameter : it takes two parameter one of his by default and other one
        paramter from the user which is number
        
        return : it will return the string of the pasto digit.
    '''
    
    pasto_counting_dict = {
       1: "يو"
         ,
         2: "دؤه",
         3:"    درے",
         4:"څلور",
         5:"    پنځه",
         6:"شپږ",
         7:"أوؤه",
         8:"    أته",
         9:"نهه",
         
       0 : "صفر"
        
        
        }
    if num is None:
        return pasto_counting_dict
    else:
        return pasto_counting_dict[num]
    
    
def Part_of_speech_dictionay(token):
    '''
        Part_of_speech_dictionary() wil return the part of speech of given token
        
        paramters:
            it takes only one parameter which token
            
        return
            if token contain in the database then it will return the toke
            otherwise return the None
    '''
    pos = pd.read_csv("Datasets/final_pos_datasets.csv" , encoding = "utf-8")    
    
    words_list = list(pos.words)
    pos_list = list(pos.POS)
    
    # making dictionary for the part of speech database
    # its bad idea to dump on the data on Ram but its oky
   
    pos_dic = {}
    if len(words_list) == len(pos_list):
        
        for word_index in range(0,len(words_list)):
            word = words_list[word_index].strip()
            pos = pos_list[word_index].strip()
            pos_dic[word] = pos 
    else:
        print("Error :words list len and pos list len is not Equal")

    #print(pos_dic)

    if token in pos_dic:
        return pos_dic[token]
    else:
        return None

if __name__ == "__main__":
    #print(Pashto_dictionary(0))
    
    print(Part_of_speech_dictionay("وړجن"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
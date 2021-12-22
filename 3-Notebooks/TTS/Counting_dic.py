#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:02:06 2021

@author: ifti
"""

def  Pashto_dictionary(num , encoding = "utf8") :
    
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
    

if __name__ == "__main__":
    print(Pashto_dictionary(0))
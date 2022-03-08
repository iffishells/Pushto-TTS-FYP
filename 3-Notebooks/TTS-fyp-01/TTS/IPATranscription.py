#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 11:06:32 2021

@author: ifti
"""



#import lib
import pandas as pd
import requests
from bs4 import BeautifulSoup

import importlib
from importlib import reload

def scrapping_IPA():
    '''
        scrapping_IPA() is a function to scrap the IPA from the web site 
        of https://polyglotclub.com/wiki/Language/Central-pashto/Pronunciation/Alphabet-and-Pronunciation
        
        parameter :
                no parameter
                
        return
            it will create the csv file on current path
    '''
    
    
    

    try:

        URL = "https://polyglotclub.com/wiki/Language/Central-pashto/Pronunciation/Alphabet-and-Pronunciation"
        r = requests.get(URL)
    except:
        print("Error : link is Down")

    soup = BeautifulSoup(r.content, 'html5lib') 
    # If this line causes an error, run 'pip install html5lib' or install html5lib
    # print(soup)

    tables = soup.find(class_="wikitable")

    column_name = []
    Final = []
    Medial = []
    Initial = []
    Isolated= []
    IPA = []
    
    for group in tables.find_all('tbody'):
        for row in group.find_all('tr'):
            if row.find_all('td'):
                # print("---------",row.find_all('td'))
                # for ipa col
                try : # may be some of them is not availables yet
                    ipa = row.find_all('td')[0]
                    IPA.append(ipa.get_text().strip())
                except:
                    IPA.append("Not yet")

                try :
                    # for final columns
                    final = row.find_all('td')[1]
                    Final.append(final.get_text().strip())
                except:
                    Final.append("Not yet")


                try:
                    # for Middle columns
                    medial = row.find_all('td')[2]
                    Medial.append(medial.get_text().strip())

                except:
                    Medial.append("Not yet")

                try:
                    # for Initail columns
                    initail = row.find_all('td')[3]
                    Initial.append(initail.get_text().strip())

                except:
                    Initial.append("Not yet")

                try: 
                    # for Isolated columns
                    isolated = row.find_all('td')[4]
                    Isolated.append(isolated.get_text().strip())
                except:
                    Isolated.append("Not yet")




    ipa_dictionay = {}
    ipa_dictionay["IPA"] = IPA
    ipa_dictionay["Final"] = Final
    ipa_dictionay["Medial"] = Medial
    ipa_dictionay["Initial"] = Initial
    ipa_dictionay["Isolated"] = Isolated
    # print((Isolated,IPA))
    
    


    # ipa_dictionay
    df = pd.DataFrame.from_dict(ipa_dictionay)
    df.to_csv("IPA_pashto.csv",index=False,encoding='utf-8')
    
    
    

def IPA(char ,Final_=False ,Medial_=False, Initial_=False,Isolated_=False):
    '''
        IPA() is a function to return the IPA of pashto char 
        
        parameter: 
            it have five paramters 
            first paramter is char which is actually char character
            
            final , medial and initial and Isolated respective taking the 
            bool value according to the sending the information
    '''
        # getting from file
    import pandas as pd
    df = pd.read_csv("Datasets/IPA_pashto.csv",encoding="utf-8")

    Final = list(df["Final"])
    Medial = list(df["Medial"])
    Initial = list(df["Initial"])
    Isolated= list(df["Isolated"])
    IPA = list(df["IPA"])



    IPA_dic = {}
    
    for index in range(0,len(IPA)):
        IPA_dic[Isolated[index]] = IPA[index]
        IPA_dic[Initial[index]] = IPA[index]
        IPA_dic[Medial[index]] = IPA[index]
        IPA_dic[Final[index]] = IPA[index]


    #print(IPA_dic)
    if char in IPA_dic:
        return IPA_dic[char]
    else:
        f = open("Datasets/not_available_ipa.txt","+w")
        f.write(char)
        f.close()
        print("{} Not present :".format(char))
        return 
        


# =============================================================================
#     Isolate_dic ={}
#     Initial_dic =  {}
#     Medial_dic = {}
#     Final_dic = {}
# 
#     if len(Isolated)==len(IPA):
#         for index in range(0,len(Isolated)):
#             Isolate_dic[Isolated[index].strip()] = IPA[index]
#             Initial_dic[Initial[index].strip()] = IPA[index]
#             Medial_dic[Medial[index].strip()] = IPA[index]
#             Final_dic[Final[index].strip()] = IPA[index]
# 
#     else:
#         print("Error : Isolated and Ipa len change")
#     
#     try:
#         if Isolated_==True:
#             return Isolate_dic[char]
#         if Initial_ == True:
#             return Initial_[char]
#         if Medial_== True:
#             return Medial_dic[char]
#         if Final_ == True:
#             return Final_dic[char]
# 
#     except:
#         print("IPA of {} is not available ".format(char))
#         return False
#     
# =============================================================================
    
if __name__ == "__main__":
    pass
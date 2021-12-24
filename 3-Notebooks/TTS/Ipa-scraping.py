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
                IPA.append(None)
            
            try :
                # for final columns
                final = row.find_all('td')[1]
                Final.append(final.get_text().strip())
            except:
                Final.append(None)
            
            
            try:
                # for Middle columns
                medial = row.find_all('td')[2]
                Medial.append(medial.get_text().strip())
            
            except:
                Medial.append(None)
            
            try:
                # for Initail columns
                initail = row.find_all('td')[3]
                Initial.append(initail.get_text().strip())
            
            except:
                Initial.append(None)
            
            try: 
                # for Isolated columns
                isolated = row.find_all('td')[4]
                Isolated.append(isolated.get_text().strip())
            except:
                Isolated.append(None)
            
                
                
                
ipa_dictionay = {}
ipa_dictionay["IPA"] = IPA
ipa_dictionay["Final"] = Final
ipa_dictionay["Medial"] = Medial
ipa_dictionay["Initial"] = Initial
ipa_dictionay["Isolated"] = Isolated


# ipa_dictionay
df = pd.DataFrame.from_dict(ipa_dictionay)
df.to_csv("IPA_pashto.csv",index=False)
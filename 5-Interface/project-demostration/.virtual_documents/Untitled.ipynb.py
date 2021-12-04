import os

import pandas as pd
import numpy as np


folder = 'Datasets'

folder_list = []
for name in os.listdir(folder):
    if os.path.isdir(os.path.join(folder,name)):
        folder_list.append(name)

speech_db = {}
for name in folder_list:
#     print(name)
    speech_db[name] = []

for name in folder_list:
    path_list = []
    for count in range(1,10):
        path = "/home/iffishells/Videos/Pushto-TTS-FYP/5-Interface/project-demostration/Datasets/"+name+"/"+name+"-"+str(count)+".wav" 
        speech_db[name].append(path)
    




get_ipython().getoutput("ls "Datasets/44-lagand"")



for name in folder_list:
    name = str(name)
    print(type(name))
    path = str("Datasets/"+name) 
    print(path)
    get_ipython().getoutput("ls path")
    break





df


get_ipython().getoutput("ls "Datasets/1-us"")


path = "Datasets/1-us"
get_ipython().getoutput("cd Datasets")
get_ipython().getoutput("pwd")





speech_db




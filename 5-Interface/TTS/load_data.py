import  pandas as pd
import numpy as np
import os 
def loadingdata():
    '''
    loadingdata() till no taking no arguments 
    return :  it will retur the dictionary of the key as word and value as the audio path of the of that words
    '''
    print("loading data Called")
    filepath  = "/home/iffishells/Pictures/Pushto-TTS-FYP/5-Interface/TTS/static/Pashto_Speech_Corpus"
    
    list_of_files = os.listdir(filepath)
    list_of_files = sorted(list_of_files)
    database_data = {}
    for inside in list_of_files:
        # print("inside : ",inside)
        # print(filepath+"/"+inside)
        
        
        audio_files_path = os.listdir(filepath+"/"+inside)
        
        for audio in audio_files_path:
            # print(filepath+"/"+inside+"/"+audio)
            
            # print(audio)
            if audio.endswith(".wav"):
                database_data[inside] = "static/Pashto_Speech_Corpus/"+inside+"/"+audio 
        
    
    # print(database_data)
    return database_data


# if __name__ == '__main__':
    
#     loadingdata()
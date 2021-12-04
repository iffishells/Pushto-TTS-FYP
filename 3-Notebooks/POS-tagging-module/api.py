from googletrans import Translator # google api


def english_to_pashsto(eng_sent):
    translator = Translator()
    
    pashto_sent = translator.translate(eng_sent ,dest = 'ps')
    print(pashto_sent)
    return pashto_sent
# except:
    #     print("Error :Eng to pashto module is not working")
    #     return 0
     
     
if __name__ == '__main__':
    english_to_pashsto("what is your name ?")
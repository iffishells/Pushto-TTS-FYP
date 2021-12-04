from api import english_to_pashsto
from nltk.tokenize import word_tokenize



if __name__ == '__main__':
    print("Hello world")
    # print(english_to_pashsto("what is your name"))
    
    
    sent = "مهربانی وکړه بیاي ووايه . يوسف غلے شو . دیړ وخت وشو نہ خکاری"
    print("Full sentance : ",sent)
    sent = word_tokenize(sent)
    print(sent)
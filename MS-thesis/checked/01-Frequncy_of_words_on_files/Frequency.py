import nltk
import re
import string
from nltk.tokenize import word_tokenize

#Program will display a welcome message to the user
#print("Welcome! This program will analyze your file to provide a word count, 
# the top 30 words and remove the following stopwords.")

s = open('Final Corpus3.txt',encoding="utf8").read()  # Open the input file

# Program will count the characters in text file
num_chars = len(s)

# Program will count the lines in the text file
num_lines = s.count('\n')

# Program will call split with no arguments
words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w],w) for w in d]
lst.sort()
lst.reverse()

# Program will print the results
print('Your input file has characters = '+str(num_chars))
print('Your input file has lines = '+str(num_lines))
print('Your input file has the following words = '+str(num_words))

print('\n The 30 most frequent words are /n')

i = 1
for count, word in lst[:200]:
    print('%2s. %4s %s' %(i,count,word))
    i+= 1


print("Thank You! Goodbye.")

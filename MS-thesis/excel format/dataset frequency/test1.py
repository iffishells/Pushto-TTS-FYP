from collections import Counter
import re
 
def openfile(test):
    fh = open(test, "r+")
    str = fh.read()
    fh.close()
    return str
 
def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str
 
def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt
 
def main(test, topwords):
    txt = openfile("test.txt")
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print(key,value)
 
main('speech.txt', 500)

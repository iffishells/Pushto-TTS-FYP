import nltk
from nltk import PCFG
from nltk import Nonterminal
from nltk import tokenize
from nltk.parse import pchart
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | NP PP [0.25] | 'John' [0.1] | 'I' [0.15]
    Det -> 'the' [0.8] | 'my' [0.2]
    N -> 'man' [0.5] | 'telescope' [0.5]
    VP -> VP PP [0.1] | V NP [0.7] | V [0.2]
    V -> 'ate' [0.35] | 'saw' [0.65]
    PP -> P NP [1.0]
    P -> 'with' [0.61] | 'under' [0.39]
""")

prods = grammar.productions()

for i in prods:
    print(i.prob())


# This works but does not transfer probabilities (Chart)
sr_parser = nltk.parse.chart.ChartParser(grammar)
sen = "I under John saw the telescope" 
sent = word_tokenize(sen)

for tree in sr_parser.parse(sent):    
    new_prods = tree.productions()
    for i in new_prods:
        print(i)
    #break

# This works (viterbi)
my_viterbi_parser = nltk.ViterbiParser(grammar)
test=my_viterbi_parser.parse(sent)
max=0
for i in test:
    if (i.prob() > max):
        max=i.prob()
        max_tree=i

print(max)
print(max_tree)

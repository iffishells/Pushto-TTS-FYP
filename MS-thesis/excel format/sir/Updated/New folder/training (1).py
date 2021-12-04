#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import nltk
import re
import pandas
from termcolor import colored

dic = pandas.read_csv("dictionary.csv")
doc = pandas.read_csv("corpus2.csv", quotechar='"', delimiter=',')
doc.columns=['ORIGINAL','TAGGED']

def number_to_pos(arg):
    switcher={
            1: "Noun",
            2: "Verb",
            3: "Adverb",
            4: "Adjective",
            5: "Numerical",
            6: "ProNoun",
            7: "Abbreviation",
            8: "Interjection",
            9: "Particle",
            10: "Preposition",
            11: "Postposition",
            12: "Suffix",
            13: "Prefix",
            14: "Conjunction"
            }
    return switcher.get(arg,"none")

def grammar_to_tag(arg):
    switcher={
            "Noun": "N",
            "Verb": "V",
            "Adverb": "ADV",
            "Adjective": "ADJ",
            "Numerical": "NUM",
            "ProNoun" : "PRN",
            "Abbreviation": "N",
            "Interjection" : "INT",
            "Particle" : "RP",
            "Preposition" : "PRP",
            "Postposition" : "POP",
            "Suffix" : "SUF",
            "Prefix" : "PRF",
            "Conjunction" : "CO"
            }
    return switcher.get(arg,"none")

def get_prob_dist(arg):
    cfd_tagwords = nltk.ConditionalFreqDist(arg)
    cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)
    return cpd_tagwords

def get_prob_dist_tags(arg):
    cfd_tags     = nltk.ConditionalFreqDist(nltk.bigrams(arg))
    cpd_tags     = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)
    return cpd_tags

# ? zero or more
# + one ore more
patterns= """S:{<NP><VP>}
             NP:{<ADJP><NP>}
             NP:{<PRP>?<N>+}
             NP:{<PRN>}
             NP:{<NP><CO><NP>}
             PP:{<PP><PP>}
             PP:{<PRP><PP>}
             PP:{<PRP><NP>}
             PP:{<NP><POP>}
             ADJP:{<ADJ>+<NP>}
             ADJP:{<ADJ><ADJ>}
             ADVP:{<ADV><NP>}
             ADVP:{<PRP><ADV><RP>}
             VP:{<NP><VP>}
             VP:{<NP><PP>+<VP>}
             VP:{<ADVP><VP>}
             VP:{<V>}
             VP:{<RP><V>}
             VP:{<RP><V><RP>}
             VP:{<POP><V>}
             VP:{<V><RP>}
             """
chunker = nltk.RegexpParser(patterns)

sentence_tuple=[]
output_full_productions=[]
sentence_string=""

S = nltk.Nonterminal('S')
NP = nltk.Nonterminal('NP')
N = nltk.Nonterminal('N')
VP = nltk.Nonterminal('VP')
ADJP = nltk.Nonterminal('ADJP')
PRP = nltk.Nonterminal('PRP')
PRN = nltk.Nonterminal('PRN')
CO = nltk.Nonterminal('CO')
PP = nltk.Nonterminal('PP')
POP = nltk.Nonterminal('POP')
ADJ = nltk.Nonterminal('ADJ')
ADV = nltk.Nonterminal('ADV')
RP = nltk.Nonterminal('RP')
ADVP = nltk.Nonterminal('ADVP')

for index, line_csv in doc.iterrows():
    line = line_csv[0]              # Actual Sentence
    pos  = line_csv[1]              # Part of Speech tagged Sentence
    if isinstance(pos, str):        # Skip (continue) if POS Sentence already given
                                    # Start scoring
        print(colored(pos,'red'))
        sentence_tuple_temp = []
        sentence_tuple.append(("START", "START"))
        tagsback=[nltk.tag.str2tuple(t) for t in pos.split()]
        for t in tagsback:
            sentence_tuple.append((t[1],t[0]))
            sentence_tuple_temp.append((t[0],t[1]))
        sentence_tuple.append(("END", "END"))
        print(sentence_tuple_temp)

        cpd_tagwords = get_prob_dist(sentence_tuple)

        #print("The probability of an Noun (N) being 'جمال' is",
        #       cpd_tagwords["N"].prob("جمال"))

        brown_tags = [tag for (tag, word) in sentence_tuple]
        cpd_tags     = get_prob_dist_tags(brown_tags)
        #print(cpd_tags["PRP"].prob("N"))

        output = chunker.parse(sentence_tuple_temp)
        #output_tree = nltk.Tree.fromstring(output)
        #output.chomsky_normal_form()
        print(output)
        #output.draw()
        nltk.draw.TreeView(output)._cframe.print_to_file('output'+str(index)+'.eps')

        for f in output.productions():
            output_full_productions.append(f)

        print(output.productions())

        continue

    line = re.sub("\,", "", line)   # remove commas
    line = re.sub("\،", "", line)   # remove commas
    line = re.sub("\‘", "", line)   # remove weird symbol
    line = re.sub("\’", "", line)   # remove weird symbol
    line = re.sub("\۔", "", line)   # remove weird symbol

    # Check if multiple sentences on the same line
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', line)
    for sentence in sentences:      # For each sentence on the line (normally 1)
        if len(sentence) > 0:
            print(colored(sentence,'red'))
        words = nltk.tokenize.word_tokenize(sentence)   # Word Tokenize
        words_in_sentence = []
        full_version = 0
        for w in words:
            pos = dic["WORD"] == w
            if len(dic[pos]) == 1:
                w1 = dic["WORD"][pos].to_string(header=False,index=False)
                w2 = dic["POS"][pos].to_string(header=False,index=False)
                w3 = grammar_to_tag(w2)
                #print("%15s\t(%s) %s"% (w1, w3, w2))
                words_in_sentence.append([w1.strip(), w2.strip(), w3.strip()])
            if len(dic[pos]) > 1:
                w1 = dic["WORD"][pos].to_string(header=False,index=False)
                w2 = dic["POS"][pos].to_string(header=False,index=False)
                temp=[]
                count = 1
                for (f, b) in zip(w1.split(), w2.split()):
                    w3 = grammar_to_tag(b)
                    print("%2s:%15s\t(%s) %s"% (count, f, w3, b))
                    temp.append([f, b, w3])
                    count += 1
                print("%2s:%15s\t%s"% (count, "نور", "other"))
                inp = int(input("Which POS for ("+colored(w,'red')+") is correct?"))
                if inp == count:
                    full_version=1
                else:
                    words_in_sentence.append([temp[inp-1][0].strip(),
                        temp[inp-1][1].strip(), temp[inp-1][2].strip()])
            if (len(dic[pos]) == 0 or full_version == 1):
                full_version = 0
                inp = int(input("POS for ("+colored(w,'red')+") in ("+sentence+")\n"+"""
                    1\tNoun
                    2\tVerb
                    3\tAdverb
                    4\tAdjective
                    5\tNumerical
                    6\tProNoun
                    7\tAbbreviation
                    8\tInterjection
                    9\tParticle
                    10\tPreposition
                    11\tPostposition
                    12\tSuffix
                    13\tPrefix
                    14\tConjunction\n"""))
                dic = dic.append({"POS": number_to_pos(inp), "WORD": w}, ignore_index=True)
                pos = dic["WORD"] == w
                w1 = dic["WORD"][pos].to_string(header=False,index=False)
                w2 = dic["POS"][pos].to_string(header=False,index=False)
                w3 = grammar_to_tag(w2)
                print(w1.split()[0].strip(), "\t", w2.split()[0].strip(), "\t",
                        w3.strip())
                dic.to_csv("dictionary.csv", encoding='utf-8', index=False, quoting=1)
                words_in_sentence.append([w1, w2, w3])

        for w in words_in_sentence:
            print("%15s\t%s (%s)"% (colored(w[0],'blue'), colored(w[1],'blue'), colored(w[2],'blue')))
            sentence_tuple.append((w[0],w[1]))
            sentence_string += f"{w[0]}/{w[2]} "
        doc.loc[index,"TAGGED"] = sentence_string
        sentence_string=""
        doc.to_csv("corpus2.csv", encoding='utf-8', index=False, quoting=1)

print(sentence_tuple)
tag_fd = nltk.FreqDist(tag for (word, tag) in sentence_tuple)
print(tag_fd.most_common())
print(tag_fd.tabulate())

patterns= """NP:{<Preposition>?<Noun>+}
             VP:{<Verb>+}
             S:{<NP><VP>}"""
chunker = nltk.RegexpParser(patterns)
output = chunker.parse(sentence_tuple)
print(output)

print(output_full_productions)
print(nltk.induce_pcfg(S, output_full_productions))

import re
from collections import Counter
#import matplotlib.pyplot as plt
#import networkx as nx


words = re.findall('\w+', open('T.txt', "r", encoding='utf-8').read())
a= Counter(zip(words,words[0:]))
print(a)
print("\n")
##G = nx.from_numpy_matrix(a)
##nx.draw(G)
##plt.show()

print(Counter(zip(words,words[1:])))
print("\n")

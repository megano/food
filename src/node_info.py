from nltk.corpus import stopwords
import networkx as nx
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

SG = nx.read_edgelist('../data/soup_database_edges.tsv', comments='#',  delimiter=',', encoding='utf-8')
# draw the network of soups and ingredients
# nx.draw(SG)
# plt.show()
# plt.savefig("network_of_soups_and_ingredients.png")

# Create salad network
SaladG = nx.read_edgelist('../data/salad_recipe_and_ingredients.tsv', comments='#',  delimiter=',', encoding='utf-8')

#print salad network info
print 'SaladG # edges:', SaladG.number_of_edges()
print 'SaladG # nodes:', SaladG.number_of_nodes()

# Salad - Generate a sorted list of connected components, largest first.
cc_salad = sorted(nx.connected_components(SaladG), key = len, reverse=True)
print "cc_salad", len(cc_salad)
print cc_salad[0]

# Generate connected components as subgraphs.
# How many connected components are there?
graphs_salad = list(nx.connected_component_subgraphs(SaladG))
print graphs_salad

salad_I = nx.read_edgelist('../data/salad_salad_edges_small_.tsv', comments='#',  delimiter='\t', encoding='utf-8')
# draw the network of salad relatedness
nx.draw(salad_I)
plt.show()
plt.savefig("network_of_salad_ingredient_connections.png")

## Jaccard similarity
#  algorithm of the jaccard similarity is the length of the intersection divide the the length of the union.
G = nx.complete_graph(5)
preds = nx.jaccard_coefficient(G, [nodepair1, nodepair1])
for u, v, p in preds:
    '(%d, %d) -> %.8f' % (u, v, p)

# # Soup network info
# print 'SoupG # edges:', SG.number_of_edges()
# print 'SoupG # nodes:', SG.number_of_nodes()

# Soup - Generate a sorted list of connected components, largest first.
# cc = sorted(nx.connected_components(SG), key = len, reverse=True)
# print len(cc)
# print cc[0]

# Generate connected components as subgraphs.
# How many connected components are there?
graphs_soup = list(nx.connected_component_subgraphs(SG))
print graphs_soup




I = nx.read_edgelist('../data/ingredient_edges.tsv', comments='#',  delimiter='\t', encoding='utf-8')
# draw the network of soup relatedness
# nx.draw(I)
# plt.show()
# plt.savefig("network_of_soups_relatedness.png")

print '# edges:', I.number_of_edges()  # edges: 7409
print '# nodes:', I.number_of_nodes()  # nodes: 521

# edges: 1922
# nodes: 710

# Find the most important nodes (using centrality)
mimportant_ingredients = Counter(nx.degree_centrality(I)).most_common(20)
print 'most important ingredients are ', mimportant_ingredients
# Original list: salt, onions, garli, carrots, pepper, olive oil, water, celery, chicken broth, garlic cloves.

# # Refined list
# [(u'onion', 0.6957403651115619), (u'garlic', 0.5801217038539553), (u'olive oil', 0.46247464503042596), (u'carrot', 0.43407707910750504), (u'celery', 0.41379310344827586), (u'chicken broth', 0.38742393509127787), (u'water', 0.34279918864097364), (u'butter', 0.3286004056795132), (u'thyme', 0.3002028397565923), (u'bay leaves', 0.27586206896551724), (u'flour', 0.2657200811359026), (u'chicken stock', 0.24949290060851925), (u'vegetable broth', 0.23326572008113589), (u'parsley', 0.2231237322515213), (u'cilantro', 0.20081135902636915), (u'tomatoe', 0.18864097363083165), (u'ginger', 0.16227180527383367), (u'oregano', 0.1460446247464503), (u'beef broth', 0.14401622718052737), (u'sour cream', 0.13793103448275862)]

# plt.hist(mimportant_ingredients,
#          color='#887E43',
#          label='ingredients')
#
# plt.title('Most Important Ingredients')
# plt.xlabel('Ingredient')
# plt.ylabel('Percent of Recipies')
# plt.legend(loc='upper right')
# plt.show()



degree_dict = I.degree()
print "degree_dict", degree_dict
# degree_series = pd.Series(degree_dict)
# degree_series.describe()
# plt.show()
# plt.clf()

'''
What are the most connected nodes?
- top 10 most connected nodes
- what are the largest subgraphs?
- do these make sense? what adjustments might be needed?
'''

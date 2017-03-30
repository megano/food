'''
This script creates edge files for the graphs of salad-ingredient and salad-salad with shared ingredients.

Created files:
    * data/salad_ingredient_edges_small.tsv
    * data/salad_salad_edges_small_.tsv

Needs this file to run:
    * data/salad_recipe_and_ingredients.csv (ingredient, salad edges)
'''

from itertools import combinations
from load_salad_database_data import load_salad_database_data


def make_edge_file(filename, d):
    '''
    filename: name of file to write to
    d: dictionary of edge data

    Write edge list to the file.
    '''
    f = open(filename, 'w')
    edges = set()
    for key, values in d.iteritems():
        for edge in combinations(values, 2):
            edges.add(tuple(sorted(edge)))
    for one, two in edges:
        f.write("%s\t%s\n" % (one, two))
    f.close()


if __name__ == '__main__':
    ingredients, salads = load_salad_database_data('../data/salad_recipe_and_ingredients.tsv')
    make_edge_file('../data/salad_ingredient_edges_small.tsv', ingredients)
    make_edge_file('../data/salad_salad_edges_small_.tsv', salads)

'''
This script creates edge files for the ingredient only graph and soup only graph.

Created files:
    * data/ingredient_edges.tsv
    * data/soup_edges.tsv

Needs this file to run:
    * data/soup_database_edges.csv (ingredient, soup edges)
'''

from itertools import combinations
from load_soup_database_data import load_soup_database_data


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
    ingredients, soups = load_soup_database_data('../data/soup_database_edges.tsv')
    make_edge_file('../data/ingredient_edges.tsv', ingredients)
    make_edge_file('../data/soup_edges.tsv', recipes)

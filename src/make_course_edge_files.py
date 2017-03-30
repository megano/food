'''
This script creates edge files for the graphs of salad-ingredient and salad-salad with shared ingredients.

Created files:
    *course*_ingredient_edges.tsv
    *course*_recipe_edges.tsv

Needs this file to run:
    *course*_recipe_and_ingredients.csv
    Has recipe name repeated for each occurance of ingredient in recipe.
'''

from itertools import combinations
from load_names_ingredients_for_course import recipe_and_ingredient_pair_dict

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
    # repeat for each course
    ingredients, recipes = load_names_ingredients_for_course('../data/*course*_recipe_and_ingredients.tsv')
    make_edge_file('../data/*course*_ingredient_edges.tsv', ingredients)
    make_edge_file('../data/*course*_recipe_edges.tsv', recipes)

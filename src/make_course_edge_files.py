'''
The code below creates edge files for the graphs of salad-ingredient and salad-salad with shared ingredients.

Created files:
    coursetype_ingredient_edges.tsv
    coursetype_recipe_edges.tsv

Needs this file to run:
    coursetype_recipe_and_ingredients.csv
    Has recipe name repeated for each occurance of ingredient in recipe.
'''

from itertools import combinations
import load_names_ingredients_for_course as lnifc

def make_edge_file(filename, d, coursetype):
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
    coursetype = 'Desserts'
    ingredients, recipes = lnifc('../data/'+ coursetype + '_recipe_and_ingredients.tsv')
    make_edge_file('../data/' + coursetype + '_ingredient_edges.tsv', ingredients)
    make_edge_file('../data/'+ coursetype +'_'+ coursetype +'_edges.tsv', recipes)

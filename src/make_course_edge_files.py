from itertools import combinations
import load_names_ingredients_for_course as lnifc

from collections import defaultdict

def recipe_and_ingredient_pair_dict(filename):
    '''
    filename: name of file with course names and ingredients.
    Read data, create two dictionaries of adjacency lists:
    pairs of ingredients that co-occur, and pairs of recipe names that share ingredients.
    '''
    f = open(filename)
    ingredients = defaultdict(set)
    recipes = defaultdict(set)
    for line in f:
        recipe, ingredient = line.strip().split(',')
        recipes[recipe].add(ingredient)
        ingredients[ingredient].add(recipe)
    f.close()
    return ingredients, recipes

'''
The code below creates edge files for the graphs of relationships
ingredient-ingredient, and course-course with shared ingredients.

Created files:
    ../data/coursetype_ingredient_edges.tsv
    ../data/coursetype_recipe_edges.tsv

Needs this file to run:
    coursetype_recipe_and_ingredients.csv
    Has recipe name repeated for each occurance of ingredient in recipe.
'''

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
    filename = '../data/'+ coursetype + '_recipe_and_ingredients.tsv'
    ingredients, recipes = recipe_and_ingredient_pair_dict(filename)
    make_edge_file('../data/' + coursetype + '_ingredient_edges.tsv', ingredients)
    make_edge_file('../data/'+ coursetype +'_'+ coursetype +'_edges.tsv', recipes)

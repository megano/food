from collections import defaultdict

filename = 'yumdata.csv'

def load_yumdata_data(filename):
    '''
    filename: name of yummly edge data file

    Read in the data and create two dictionaries of adjacency lists, one for
    the ingredients and one for the recipes.
    '''
    f = open(filename)
    ingredients = defaultdict(set)
    recipes = defaultdict(set)
    for line in f:
        ingredients, recipe = line.strip().split('\t')
        ingredients[ingredients].add(recipe)
        recipes[recipe].add(ingredients)
    f.close()
    return ingredients, recipes

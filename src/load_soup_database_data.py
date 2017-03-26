from collections import defaultdict

def load_soup_database_data(filename):
    '''
    filename: name of soup edge data file

    Read in the data and create two dictionaries of adjacency lists,
    one for ingredients and one for recipes.
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

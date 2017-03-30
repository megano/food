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

# salad_database --> recipe_and_ingredient_pair_dict_for_course

## # df[coursetype].loc[:,[["id", "name", "ingredient"]] = df[coursetype][["id", "name", "ingredient"]].values

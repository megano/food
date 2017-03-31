import pandas as pd
import numpy as np
import string
import re
from collections import Counter

def read_csv(filename, col_names):
    '''
    Takes file name, list of column header names, and a course type.
    Creates a master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    return df_all_courses

def make_course_dfs(df, compare_courses):
    '''
    Input - Takes a dataframe, string of courses to create dataframes for.
    Ex: compare courses = ['Desserts', 'Breakfast and Brunch'].
    Dataframe can have multiple course types.
    Output - For each course in compare_courses it creates a data frame with only
    recipes matching specified course type. And an ingredient file for that course.
    '''
    d = {}
    for choice in compare_courses:
        # d[choice] is 'Desserts' on first pass.
        '''
        loops through choices in compare_courses list.
        '''
        #print "choice in compare_courses is", choice
        # print type(choice)
        # print "now creating dataframe for ", choice
        d[choice] = df[df['course'] == choice]
        d[choice].drop({'id', 'course'}, axis=1, inplace=True)
        # clean up values in ingredients column
        # remove all whitespace at the start and end, lowercase, strip out non-alpha characters with regex # replace('-', ' ')
        d[choice].ingredient = d[choice].ingredient.str.strip().str.lower().map(lambda x: re.sub(r'\W+', ' ', x))
        # print d[choice].ingredient  # verify oreo cookies entry has no trademark
        d[choice].name = d[choice].name.str.strip().str.lower().map(lambda x: re.sub(r'\W+', ' ', x))
        # print d[choice].name
        # return d[choice]
        # df[choice].loc[:,[['id', 'name', 'ingredient']] = df[choice][['id', 'name', 'ingredient']].values

        ## Print number of unique ingredients, recipe names for that course type.
        print d[choice].ingredient.nunique(), "unique ingredients in recipes for " + choice

        # 3767  unique ingredients in recipes for Breakfast and Brunch
        print d[choice].name.nunique(), "unique recipe names for " + choice
        # 14963  unique recipe names for Breakfast and Brunch
    return d

def make_counters(course_df_dict, countnum=20):
    '''
    In: dictionary of dataframes. key: coursename, value: course_df with only recipe name and ingredient columns.
    Out: Set of X common ingredients between courses.

    It takes a course dataframe
    Counts # times an ingredient occurs within all recipes in that course.
    Returns ingredient and # times it occurs within recipies in that course, with most frequently occuring ingredients first.
    Creates a list of the top X occuring ingredients.

    # Desserts c_most = [('salt', 22931), ('sugar', 20860), ('butter', 19475), ('vanilla extract', 17831), ('eggs', 17366), ('all purpose flour', 12705), ('unsalted butter', 11823), ('baking powder', 11816), ('baking soda', 10475), ('granulated sugar', 10020)]
    # Desserts c_least [('liver', 1), ('crispbreads', 1), ('cinnamon ice cream', 1), ('simply organic ground cloves', 1), ('unreal candy', 1), ('vanilla pastry cream', 1), ('nestle toll house delightfulls peanut butter filled morsels', 1), ('king syrup', 1), ('white chocolate liqueur', 1), ('date paste', 1)]

    Compares top X ingredients of course a to course b.
    Returns list of ingredients that occur in both course a and course b.
    '''
    # my_counters = {}
    most_common_ing_set_list = {}
    ## Create counter for the course. Prints most and least common ingredients.
    for course_df in course_df_dict:
        print "course_df_dict course_df is ", course_df

        c = Counter(course_df.ingredient)
        c_most_common = c.most_common(countnum)  # X most common ingredients in course
        most_common_ing_set = {x for x,_ in c.most_common(countnum)}  # converts result to ingredient list, no counts

        most_common_ing_set_list[course_df](most_common_ing_set) # adds top X ingredients to dictionary.

        ## Create csv of ingredient set
        # ing_set.to_csv('top_20_ingredients_of_'+ course_df +'.txt')

        ## Print summary
        # print "counter of "+ course_df + "recipe phrases", c
        # print "c_most_common", c_most_common
        # print course_df + " c_least", c.most_common()[:-10-1:-1]  # least common ingredients

        # my_counters[course_df](c_most_common)


    # print "my_counters are", my_counters
    return most_common_ing_set_list # my_counters


### MAKE RECOMMENDATIONS
# remove stopwords

 ## 5 recipes each for 2 courses with at least 1 common ingredient.
 # Ex: Return salad and soup recipes containing tomatoes.

# def common_ingredients(my_counters):
#     '''
#     In: The list of courses and ingredient counts from make_counters.
#     Out: Ingredients common in courses.
#     '''
#     # Check recipes for at least 1 ingredients in common.
#     recipes_match = d[choice][d[choice].ingredient.isin([ingredient1, ingredient2])]
#     print "recipes_match", recipes_match.head()
#     print len(recipes_match)

def rec_recipes(df_course, compare_courses, my_ing_lists):
    '''
    In: list of ingredients that occur in both course a and course b.
    Out: Recipe recommendations that have at least 1
    matching ingredient from X most common in both courses.
    '''
    common_ing = []


    # [common_ing.append(ing_a in ing_b) for ing in ing_lst_2]


    # ## Ex: What are course X recipes with at least 1 of 3 of most common ingredients?
    # row_mask = soups_df_all.ingredient.isin(match_lst).all(1)
    # recipes_match = coursetype_df[coursetype_df[row_mask]]
    # print "recipes with at least 1 common ingredient with match list", recipes_match.head()
    # print len(recipes_match)

## How to choose between results of matching recipes.
# look at total number of ingredients needed to make recommended recipes. Maybe ratio of shared ing vs total ing.
# if results don't have variety, try creating that. Pick at random or sort by max number of common ingredients.




# def make_network():
#     do_ri_pair()  # makes edge files
#     do_network()  # makes visualization


if __name__ == '__main__':
    course_chosen = 'Desserts'
    course_chosen2 = 'Breakfast and Brunch'
    compare_courses = ['Desserts', 'Breakfast and Brunch']
    col_headers = ['id', 'name', 'course', 'ingredient']
    filename = '../data/ttest_api2_42_1_155501.csv'
    df = read_csv(filename, col_names = col_headers)
    course_df_dict = make_course_dfs(df = df, compare_courses = compare_courses)
    my_counters, my_ing_lists = make_counters(course_df_dict = course_df_dict)
    rec_recipes(df_course = course_df_dict, compare_courses = compare_courses, my_ing_lists = my_ing_lists)
    # course_info(course_chosen = course_chosen, df=df_course)


    # course_options = ['Main Dishes', 'Desserts', 'Side Dishes', 'Lunch and Snacks', 'Appetizers', 'Salads', 'Breads', 'Breakfast and Brunch', 'Soups', 'Beverages', 'Condiments and Sauces', 'Cocktails']

    # soup_mc_ing_10_mod = ['chicken',
    #  'onions',
    #  'broth',
    #  'oil',
    #  'olive',
    #  'garli',
    #  'carrots',
    #  'tomatoes',
    #  'celery',
    #  'onion',
    #  'stock',
    #  'butter',
    #  'cheese',
    #  'cream']
    #  salad_mc_ing_10_mod = ['oil',
    #   'olive',
    #   'vinegar',
    #   'lemon',
    #   'onion',
    #   'cheese',
    #   'garlic',
    #   'mayonnaise',
    #   'tomatoes',
    #   'mustard']

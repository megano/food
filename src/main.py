import pandas as pd
import numpy as np
import string
import re
from collections import Counter
# from load_names_ingredients_for_course import recipe_and_ingredient_pair_dict as do_ri_pair

'''
The code below takes a raw csv of recipe data.
It gives recommendations and info on the relationships
of ingredients within and across courses.

Supported Courses
Main Dishes, Desserts, Side Dishes, Lunch and Snacks,
Appetizers, Salads, Breads, Breakfast and Brunch,
Soups, Beverages, Condiments and Sauces, Cocktails

========================================================================================
=== EXAMPLE OUTPUT FOR DESSERTS AND BREAKFAST AND BRUNCH COURSES  ======================

shared_ing are set(['butter', 'baking powder', 'vanilla extract', 'large eggs', 'flour',
 'eggs', 'sugar', 'water', 'vanilla', 'all purpose flour', 'unsalted butter',
 'brown sugar', 'baking soda', 'salt', 'milk', 'cinnamon'])

                                            name       ingredient
167  5 ingredient breakfast stuffed acorn squash             eggs
170  5 ingredient breakfast stuffed acorn squash             salt
216                      farmer s market granola  unsalted butter
217                      farmer s market granola      brown sugar
379                     avocado eggs in a basket       large eggs
55633
204728
                            name   ingredient
9   cookies and cream snack cake        flour
10  cookies and cream snack cake        sugar
12  cookies and cream snack cake  baking soda
13  cookies and cream snack cake         salt
17  cookies and cream snack cake       butter

['5 ingredient breakfast stuffed acorn squash'
 'cookies and cream snack cake']
========================================================================================
Created files:
    '../data/'+ course_type + '_recipe_and_ingredients.tsv'
    '../data/'+ course_type + '_top_ingredients.tsv'
    Uncomment the lines to generate files

Needs recipe csv file to run:
    '../data/all_recipes_unfiltered.csv'
    Has recipe name repeated for each occurance of ingredient in recipe.
'''

def read_recipe_csv(filename, col_names):
    '''
    In: CSV file name, list of column header names.
    Out: A master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    ### drop duplicate rows
    return df_all_courses

def make_course_df(df_all_courses, course_type):
    '''
    In: Master dataframe of all course types, string of a course type to create a dataframe for.
    Ex: 'Breakfast and Brunch'.
    Out: course_df_raw: A data frame with only recipes matching specified course type.
    '''
    df = df_all_courses
    choice = course_type
    choice_df = df[df['course'] == choice]
    # Select rows matching only that course type
    choice_df.drop({'id', 'course'}, axis=1, inplace=True)
    # print "df minus id and course columns", choice_df.head()
    print "@@@ number unique recipies in data @@@", df_all_courses.id.nunique()
    course_df_raw = choice_df
    return course_df_raw

def clean_course_df(course_df_raw, course_type):
    '''
    In: Course type and course dataframe with raw values: uppercase letters, punctuation, etc.
    Out: course_df: A course dataframe with cleaned values in ingredients column.
    '''
    choice_df = course_df_raw
    # print choice_df.ingredient.head()
    # remove all whitespace at start and end, lowercase, strip out non-alpha characters with regex # replace('-', ' ')
    choice_df.ingredient = choice_df.ingredient.str.strip().str.lower().map(lambda x: re.sub(r'\W+', ' ', x))
    # print choice_df.ingredient  # verify oreo cookies entry has no trademark
    choice_df.name = choice_df.name.str.strip().str.lower().map(lambda x: re.sub(r'\W+', ' ', x))
    # print choice_df

    course_df = choice_df
    return course_df

def make_course_ingredient_lists(num_top_ing, course_df): #, cooking_stopwords):
    '''
    In: A data frame with only recipes matching specified course type. Max number of ingredients for top ingredient list.
    Cooking stopwords removes those words from ingredients.
    Out: course_all_ing: List of all unique ingredient phrases for that course.
    course_top_ing: List of X most frequently occuring ingredient phrases for that course.

    Counts # times an ingredient occurs within all recipes in that course.
    Returns ingredient, # times it occurs within recipies in that course. Most frequently occuring ingredients first.

    Course type examples: ['Desserts', 'Breakfast and Brunch']
    '''
    countnum = num_top_ing
    # print "make_course_ingredient_lists course df", course_df.head()
    c = Counter(course_df.ingredient)
    c_most_common = c.most_common(countnum)  # X most common ingredients in course
    # print "c_most_common", c_most_common  # ordered
    most_common_ing_set = {x for x,_ in c.most_common(countnum)}  # gives ingredient list, no counts, not ordered
    # print "most_common_ing_set", most_common_ing_set
    course_all_ing = c # this is the counter, results are ordered
    course_top_ing = most_common_ing_set
    # print "course_all_ing counter", course_all_ing
    # print "course top list is", course_top_ing
    return course_top_ing, course_all_ing

def compare_course_ingredients(course_top_ing_a, course_top_ing_b):
    '''
    In: Two course ingredient sets to compare.
    Out: shared_ing: List of common ingredients in those two courses.
    '''
    shared_ing = course_top_ing_a.intersection(course_top_ing_b)

    print "@@@ First course to compare's top ingredients are @@@", course_top_ing_a
    print "@@@ Second course to compare's top ingredients are  @@@", course_top_ing_b
    return shared_ing


def rec_recipes_with_shared_ingredients(shared_ing, course_df_a, course_df_b, num_recipe_names):
    '''
    In: List of shared ingredients, dataframes of course types, number of recipe names to recommend.
    Out: rec_recipes: Returns X recipe recommendations
    that have at least 1 ingredient in the overlap list of the
    # of most common ingredients in both course a and b.

    Finds the row in the course_df that has that ingredient.
    Looks at the recipe name value for that row.
    Makes a list of recipe names.
    '''
    print "@@@ rec_recipes shared_ing @@@", shared_ing
    print course_df_a.ingredient.head()
    print course_df_b.ingredient.head()

    # Finds the row in the course_df that has that ingredient.
    r_course_a = course_df_a[course_df_a.ingredient.isin(shared_ing)]
    print "@@@ r_course_a is @@@", r_course_a.head()
    # print len(r_course_a)
    r_course_b = course_df_b[course_df_b.ingredient.isin(shared_ing)]
    # print len(r_course_b)
    print "@@@ r_course_b is @@@", r_course_b.head()

    # Get X recipe names from each course that match ingredient overlap list
    a = list(set(r_course_a.name.values))[0:num_recipe_names]
    b = list(set(r_course_b.name.values))[0:num_recipe_names]
    print "@@@ unique a recipes are @@@", a
    print "@@@ unique b recipes are @@@", b

    ## Can get a different kind of rec with masking.
    # ## Ex: What are recipes with at least 1 of 3 of most common ingredients?
    # row_mask = soups_df_all.ingredient.isin(match_lst).all(1)
    # recipes_match = coursetype_df[coursetype_df[row_mask]]
    # print "recipes with at least 1 common ingredient with match list", recipes_match.head()
    # print len(recipes_match)

    # rec_recipes = []
    # rec_recipes = np.concatenate((a, b))
    # print rec_recipes
    # return rec_recipes


def do_it_all(course_type):
    '''
    In: Calls all functions needed to make course top ingredient list.
    Out: Course top ingredients, cleaned course dataframe.
    '''
    col_names = ['id', 'name', 'course', 'ingredient']
    # filename = '../data/all_recipes_unfiltered.csv'
    # Smaller file for debugging
    filename = '../data/ttest_api2_42_1_155501.csv'
    num_top_ing = 50
    df_all_courses = read_recipe_csv(filename, col_names)
    course_df_raw = make_course_df(df_all_courses, course_type)
    course_df = clean_course_df(course_df_raw, course_type)

    # ing_filename = '../data/'+ course_type + '_ingredients.tsv'
    # course_df.ingredient.values.tofile(ing_filename,sep=',')
    course_top_ing, course_all_ing = make_course_ingredient_lists(num_top_ing, course_df)
    return course_top_ing, course_df

if __name__ == '__main__':
    course_type = 'Soups'
    course_type2 = 'Cocktails'
    num_recipe_names = 10
    course_top_ing_a, course_df_a = do_it_all(course_type=course_type)
    course_top_ing_b, course_df_b = do_it_all(course_type = course_type2)
    shared_ing = compare_course_ingredients(course_top_ing_a, course_top_ing_b)
    rec_recipes = rec_recipes_with_shared_ingredients(shared_ing, course_df_a, course_df_b, num_recipe_names)

    '''
    Supported Courses
    Main Dishes, Desserts, Side Dishes, Lunch and Snacks,
    Appetizers, Salads, Breads, Breakfast and Brunch,
    Soups, Beverages, Condiments and Sauces, Cocktails
    '''

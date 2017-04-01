import pandas as pd
import numpy as np
import string
import re
from collections import Counter
from load_names_ingredients_for_course import recipe_and_ingredient_pair_dict as do_ri_pair
from make_network import do_it_all as do_network


def read_csv(filename, col_names):
    '''
    In: CSV file name, list of column header names.
    Out: A master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    ### drop duplicate rows
    # print df_all_courses.head()
    return df_all_courses

def make_course_df(df_all_courses, course_type):
    '''
    In: Master dataframe of all course types, string of a course type to create a dataframe for.
    Ex: 'Breakfast and Brunch'.
    Out: course_df_raw: A data frame with only recipes matching specified course type.
    '''
    return # course_df_raw

def clean_course_df(course_df_raw):
    '''
    In: A course dataframe with raw values: uppercase letters, punctuation, etc.
    Out: course_df: A course dataframe with cleaned values.
    '''

    return # course_df

def make_course_ingredient_lists(course_df, num_top_ing, cooking_stopwords):
    '''
    In: A data frame with only recipes matching specified course type. Max number of ingredients for top ingredient list.
    Cooking stopwords list of words to remove from ingredients.
    Out: course_all_ing: List of all unique ingredient phrases for that course.
    course_top_ing: List of X most frequently occuring ingredient phrases for that course.

    Note: Cooking stopwords are removed from ingredient lists.

    Counts # times an ingredient occurs within all recipes in that course.
    Returns ingredient, # times it occurs within recipies in that course. Most frequently occuring ingredients first.

    Course type examples: ['Desserts', 'Breakfast and Brunch']
    '''
    return # course_all_ing, course_top_ing

def compare_course_ingredients(course_top_ing_a, course_top_ing_b, num_shared):
    '''
    In: Two course ingredient sets to compare. Number of shared ingredients to check for.
    Out: shared_ing: List of common ingredients in those two courses.
    '''
    return # shared_ing

def rec_recipes_with_shared_ingredients(shared_ing, course_df_a, course_df_b):
    '''
    In: List of shared ingredients, dataframes of course types.
    Out: rec_recipes: Returns a few recipe recommendations that have at least 1
    matching ingredient from X most common in both course a and b.

    Finds the row in the course_df that has that ingredient.
    Looks at the recipe name value for that row.
    Makes a list of recipe names.
    '''
    return # rec_recipes

def print_rec_recipes(rec_recipes):
    '''
    In:
    Out:
    OUTPUT EXAMPLE:
    There are 46550 soup and salad recipes sharing at least 1 ingredient in the match list.
    Here are 6 of them: Butternut Squash Soup, The Best Minestrone Soup, ....

    # ## Ex: What are course X recipes with at least 1 of 3 of most common ingredients?
    # row_mask = soups_df_all.ingredient.isin(match_lst).all(1)
    # recipes_match = coursetype_df[coursetype_df[row_mask]]
    # print "recipes with at least 1 common ingredient with match list", recipes_match.head()
    # print len(recipes_match)
    '''

# def rec_groceries():
#     '''
#     In: Recipe names.
#     Out: grocery_list = List of ingredients in that recipe.
#     '''
#     # Butternut Squash Soup:  [onions, tomatoes, ...], The Best Minestrone Soup [onions, cilantro, ...]

# def compare_course_summary():
#     '''
#     In:
#     Out:
#     Prints summary of course comparison.
#     '''

#
# def make_course_ingredient_file(course_ing):
#     '''
#     In: A course ingredient list
#     Out: ingredient: A text file of ingredients for that course.
#     '''

if __name__ == '__main__':
    col_names = ['id', 'name', 'course', 'ingredient']
    filename = '../data/ttest_api2_42_1_155501.csv'
    df_all_courses = read_csv(filename, col_names)
    course_type = 'Desserts'
    course_type2 = 'Breakfast and Brunch'
    num_top_ing = 20
    # compare_courses = ['Desserts', 'Breakfast and Brunch']
    course_df_raw = make_course_df(df_all_courses, course_type)
    course_df = clean_course_df(course_df_raw)
    # course_all_ing, course_top_ing = make_course_ingredient_lists(course_df, num_top_ing) #, cooking_stopwords)
    # shared_ing = compare_course_ingredients(course_top_ing_a, course_top_ing_b, num_shared)
    # rec_recipes = rec_recipes_with_shared_ingredients(shared_ing, course_df_a, course_df_b)
    # print_rec_recipes(rec_recipes)

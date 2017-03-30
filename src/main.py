import pandas as pd
import numpy as np
import string
import re
from collections import Counter
from load_names_ingredients_for_course import recipe_and_ingredient_pair_dict as do_ri_pair
from make_network import do_it_all as do_network


def read_csv(filename, col_names):
    '''
    Takes file name, list of column header names, and a course type.
    Creates a master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    return df_all_courses

### clean values in ingredients list ###

def make_course_dfs(df, compare_courses):
    '''
    In: Takes a dataframe, chosen course string. Ex: course chosen = 'Salads'. Source dataframe can have multiple course types.
    Out: Creates a new data frame with only recipes matching specified course type. And an ingredient file for that course.
    '''
    # print "compare_courses in make_course_dfs", compare_courses
    compare_courses = compare_courses
    for choice in compare_courses: # loops through choices in compare_courses list.
        # print "choice in compare_courses is", choice
        # print type(choice)
        d = {}
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

        c = Counter(d[choice].ingredient)
        print "counter of "+ choice + "recipe phrases", c
        print choice + " c_most", c.most_common(200)  # most common ingredient words
        print choice + " c_least", c.most_common()[:-20-1:-1]  # least common ingredient words
        return d[choice], c

        ## Create ingredient_list.txt for the course.
        top_200_ing = list(c.most_common(200))
        print choice + " top 200 ingredient list", top_200_ingx
        # top_200_ing.to_csv('top_200_ingredients_of_'+ choice +'.txt')


def course_info(course_chosen, df):
    print "course info course_chosen is", course_chosen
    print df.ingredient.nunique(), " unique ingredients in recipes for " + course_chosen
    print df.name.nunique(), " unique recipe names for " + course_chosen


# MAKE RECOMMENDATIONS
# def recommendations(course_chosen, course_chosen2):
#     return
 ## 5 recipes each for 2 courses with at least 1 common ingredient.
 # Return salad and soup recipes containing tomatoes.

# def common_ingredients(df_course, course_chosen, course_chosen2, counter1, counter2, ingredient1, ingredient2):
#     '''
#     In: Two names of courses. Two counters of ingredients for two courses.
#     Out: Ingredients common in both courses.
#     '''
#     # Check recipes for at least 1 ingredients in common.
    # recipes_match = d[choice][d[choice].ingredient.isin([ingredient1, ingredient2])]
    # print "recipes_match", recipes_match.head()
    # print len(recipes_match)




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
    df_course, c = make_course_dfs(df = df, compare_courses = compare_courses)
    course_info(course_chosen = course_chosen, df=df_course)


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

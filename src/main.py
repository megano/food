import pandas as pd
from collections import Counter

def read_csv(filename, col_names):
    '''
    Takes file name, list of column header names, and a course type.
    Creates a master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    return df_all_courses

### clean values in ingredients list ###


def make_course_df(df, col_names, coursetype, coursetypes):
    '''
    Takes a dataframe, column names, and string of course type.
    Ex: course type = 'Salads'. Dataframe can have multiple course types.
    Creates a new data frame with only recipes matching specified course type.
    If course type given does not match, returns error message with valid course types.
    '''
    if coursetype in coursetypes:
        # print coursetype
        # df_coursetype = pd.DataFrame()
        d = {}
        d[coursetype] = df[df['course'] == coursetype]
        d[coursetype].drop('course', axis=1, inplace=True)
        # df[coursetype].loc[:,[['id', 'name', 'ingredient']] = df[coursetype][['id', 'name', 'ingredient']].values
        #List unique values. Use the df['name'] column
        return d[coursetype]
        # print d[coursetype].head()  # verify the db created is of the specified course type.
    else:
        print 'Hmm, I don\'t know that course. Try one of these: Main Dishes, Desserts, Side Dishes, Lunch and Snacks, Appetizers, Salads, Breads, Breakfast and Brunch, Soups, Beverages, Condiments and Sauces, Cocktails'

def course_info(coursetype, df):
    print coursetype
    print df.head()
    print df.ingredient.nunique(), " unique recipes for this course"
    print df.ingredient.values()
    # print "salad_ing_phrases", salad_ing_phrases

def max_min_ingredients():
    return
    # c = Counter(salad_ing_phrases)
    # print "counter on salad_ing_phrases", c
    # c_most = c.most_common(10)  # 10 most common ingredient words
    # print "c_most", c_most
    # print "c_least", c.most_common()[:-10-1:-1]  # 10 least common ingredient words

def make_ingredient_txt():
    ## Create ingredient_list.txt for the course.
    return

# MAKE RECOMMENDATIONS
def recommendations():
    return
 ## 5 recipes each for 2 courses with at least 1 common ingredient.
 # Return salad and soup recipes containing tomatoes.

## Check salad recipes for at least 1 of ingredients in ingredient list.
# recipes_matching_ing_df = salads_df_all[salads_df_all.ingredient.isin(['tomatoes', 'onions'])]
# print recipes_matching_ing_df.head()
# print len(recipes_matching_ing_df)


if __name__ == '__main__':
    coursetype = 'Desserts'
    coursetype2 = 'Breakfast and Brunch'
    col_headers = ['id', 'name', 'course', 'ingredient']
    filename = '../data/ttest_api2_42_1_155501.csv'
    df = read_csv(filename, col_names = col_headers)
    coursetypes = ['Main Dishes', 'Desserts', 'Side Dishes', 'Lunch and Snacks', 'Appetizers', 'Salads', 'Breads', 'Breakfast and Brunch', 'Soups', 'Beverages', 'Condiments and Sauces', 'Cocktails']
    df_course = make_course_df(df, col_names = col_headers, coursetype = coursetype, coursetypes = coursetypes)
    course_info(coursetype, df_course)
    soup_mc_ing_10_mod = ['chicken',
     'onions',
     'broth',
     'oil',
     'olive',
     'garli',
     'carrots',
     'tomatoes',
     'celery',
     'onion',
     'stock',
     'butter',
     'cheese',
     'cream']
     salad_mc_ing_10_mod = ['oil',
      'olive',
      'vinegar',
      'lemon',
      'onion',
      'cheese',
      'garlic',
      'mayonnaise',
      'tomatoes',
      'mustard']

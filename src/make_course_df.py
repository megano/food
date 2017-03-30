import pandas as pd

def read_csv(filename, col_names):
    '''
    Takes file name, list of column header names, and a course type.
    Creates a master dataframe of all the data.
    '''
    # Create a master dataframe of all the data
    df_all_courses = pd.read_csv(filename, names = col_names)
    return df_all_courses

    # print len(df_all_courses)
    # print df_all_courses.id.nunique()

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
        return d[coursetype]
        # print d[coursetype].head()  # verify the db created is of the specified course type.
    else:
        print 'Hmm, I don't know that course. Try one of these: 'Main Dishes', 'Desserts', 'Side Dishes', 'Lunch and Snacks', 'Appetizers', 'Salads', 'Breads', 'Breakfast and Brunch', 'Soups', 'Beverages', 'Condiments and Sauces', 'Cocktails''

if __name__ == '__main__':
    col_headers = ['id', 'name', 'course', 'ingredient']
    df = read_csv('../data/ttest_api2_42_1_155501.csv', col_names = col_headers)
    coursetypes = ['Main Dishes', 'Desserts', 'Side Dishes', 'Lunch and Snacks', 'Appetizers', 'Salads', 'Breads', 'Breakfast and Brunch', 'Soups', 'Beverages', 'Condiments and Sauces', 'Cocktails']
    df_course = make_course_df(df, col_names = col_headers, coursetype = 'Salads', coursetypes = coursetypes)

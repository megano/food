# This Python file uses the following encoding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import re

df_all = pd.read_csv('../data/all_recipes_unfiltered.csv')  # names = ["id", "name", "course", "ingredient"]
df_all.id.nunique()    # 1,405,879 unique recipes when aggregated.

# How many soup recipes?
soups_df_all = df_all[df_all['course'] == 'Soups']
# print "soups_df_all header", soups_df_all.head()  # yep, it's grabbing the right rows
# print soups_df_all.id.nunique()  # 66,889 unique soup recipes

# How many recipes for course X?
# Create data frame for course X

salads_df_all = df_all[df_all['course'] == 'Salads']
# print "salads_df_all header", salads_df_all.head()  # yep, it's grabbing the right rows
# print len(salads_df_all.id.unique())  # 81,510 unique salad recipes

## Create ingredient_list.txt for all salads.
#List unique values in the df['name'] column
salad_ing_phrases = salads_df_all.ingredient.unique()
print "salad_ing_phrases", salad_ing_phrases
c = Counter(salad_ing_phrases)
print "counter on salad_ing_phrases", c
c_most = c.most_common(10)  # 10 most common ingredient words
print "c_most", c_most
print "c_least", c.most_common()[:-10-1:-1]  # 10 least common ingredient words

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



 ## 5 recipes each for 2 courses with at least 1 common ingredient.
 # Return salad and soup recipes containing tomatoes.

## Check salad recipes for at least 1 of ingredients in ingredient list.
# recipes_matching_ing_df = salads_df_all[salads_df_all.ingredient.isin(['tomatoes', 'onions'])]
# print recipes_matching_ing_df.head()
# print len(recipes_matching_ing_df)

# Result of 5 salad recipes with tomatoes in ingredients.
# tomatoes appears 8,960 times in ingredients.
#                                     name  course ingredient
# 4482     Chickpea Salad With Fresh Mango  Salads   tomatoes
# 5254   Tomato Salad with Thyme and Honey  Salads   tomatoes
# 8196     Onion Tomato Mixed Sprout Salad  Salads   tomatoes
# 16720                     Salad Nicoise  Salads   tomatoes
# 20627               Moms Macaroni Salad  Salads   tomatoes

## Check soup recipes for ingredients selected
# recipes_matching_ing_df = soups_df_all[soups_df_all.ingredient.isin(['tomatoes'])]
# print recipes_matching_ing_df.head()
# print len(recipes_matching_ing_df)

# Result of 5 soup recipes with tomatoes in ingredients?
# tomatoes appears 6,551 times in ingredients.
#                                            name course ingredient
# 29842  Spicy Cabbage Soup for Cabbage Soup Diet  Soups   tomatoes
# 33892                    Simple Black Bean Soup  Soups   tomatoes
# 49161                Easy Pork and 3-Bean Chili  Soups   tomatoes
# 51714                    Summer-Garden Gazpacho  Soups   tomatoes
# 63229                    Vegan Spanish Gazpacho  Soups   tomatoes

## Encoding error on recipe names: # 16720                     Salad Nicoise  Salads   tomatoes

## What are soup recipes with at least 1 of 3 of most common ingredients?
ing_to_match = ['tomatoes', 'onions', 'cheese']
row_mask = soups_df_all.ingredient.isin(ing_to_match).all(1)
recipes_matching_ing_df = soups_df_all[soups_df_all[row_mask]]
print "recipes with 3 common ingredients", recipes_matching_ing_df.head()
print len(recipes_matching_ing_df)

# 46550
#                                    name course ingredient
# 1430              Butternut Squash Soup  Soups     onions
# 4181           The Best Minestrone Soup  Soups     onions
# 5280     Soup Maker Greek Lemon Chicken  Soups     onions
# 5664               Chicken Pot Pie Soup  Soups     onions
# 7019  Souper Simple Chicken Noodle Soup  Soups     onions

# Butternut Squash Soup:  [onions, tomatoes, ...], The Best Minestrone Soup [onions, cilantro, ...]

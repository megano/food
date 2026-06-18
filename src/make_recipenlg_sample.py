"""
Build a sample dataset for this pipeline from RecipeNLG.

RecipeNLG (https://recipenlg.cs.put.poznan.pl/, open license) ships as
full_dataset.csv with columns: [index], title, ingredients, directions,
link, source, NER. It has no `course` field, so we derive course from
keywords in the title and explode the NER ingredient list into the
four-column shape main.py expects:

    id, name, course, ingredient   (headerless, one row per ingredient)

Usage:
    1. Download full_dataset.csv from recipenlg.cs.put.poznan.pl (accept the
       license on the site), put it in ../data/.
    2. python3 make_recipenlg_sample.py
    3. Point main.py's `filename` at ../data/recipenlg_sample.csv

Python 3. Requires pandas.
"""
import ast
import csv
import json
import os

SRC = os.path.join(os.path.dirname(__file__), '..', 'data', 'RecipeNLG_full_dataset.csv')
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'recipenlg_sample.csv')

# Title keyword -> course. First match wins, so order matters.
COURSE_RULES = [
    ('Soups',      ('soup', 'bisque', 'chowder', 'broth')),
    ('Salads',     ('salad',)),
    ('Desserts',   ('cake', 'cookie', 'pie', 'brownie', 'pudding', 'tart')),
    ('Breakfast and Brunch', ('pancake', 'waffle', 'omelet', 'frittata', 'granola')),
    ('Beverages',  ('smoothie', 'juice', 'latte', 'lemonade')),
    ('Cocktails',  ('cocktail', 'margarita', 'martini', 'mojito', 'sangria')),
]

PER_COURSE = 200   # cap recipes per course to keep it a sample


def course_for(title):
    t = title.lower()
    for course, keywords in COURSE_RULES:
        if any(k in t for k in keywords):
            return course
    return None


def parse_ner(cell):
    """NER cell is a list-as-string. Try JSON, then Python-literal."""
    for parse in (json.loads, ast.literal_eval):
        try:
            val = parse(cell)
            if isinstance(val, list):
                return val
        except (ValueError, SyntaxError):
            continue
    return []


def main():
    import pandas as pd
    if not os.path.exists(SRC):
        raise SystemExit(
            "Missing %s\nDownload full_dataset.csv from "
            "https://recipenlg.cs.put.poznan.pl/ and place it in data/." % SRC)

    counts = {course: 0 for course, _ in COURSE_RULES}
    target = {course for course, _ in COURSE_RULES}
    rows = []

    # The file is ~2GB; stream it in chunks.
    reader = pd.read_csv(SRC, chunksize=50000)
    for chunk in reader:
        for _, r in chunk.iterrows():
            if not target:
                break
            title = str(r.get('title', '')).strip()
            if not title:
                continue
            course = course_for(title)
            if course is None or counts[course] >= PER_COURSE:
                continue
            ings = parse_ner(str(r.get('NER', '[]')))
            if not ings:
                continue
            rid = r.iloc[0]  # the leading index column
            name = title.lower()
            for ing in ings:
                ing = str(ing).strip().lower()
                if ing:
                    rows.append((rid, name, course, ing))
            counts[course] += 1
            if counts[course] >= PER_COURSE:
                target.discard(course)
        if not target:
            break

    with open(OUT, 'w', newline='') as f:
        csv.writer(f).writerows(rows)

    print("wrote %d ingredient rows to %s" % (len(rows), OUT))
    for course, n in counts.items():
        print("  %-22s %d recipes" % (course, n))


if __name__ == '__main__':
    main()

# Background
My parents live in a rural area, and sometimes need to drive for 1 hour to get 1 or 2 ingredients for dinner.

# Challenge
Remove some of the manual and cognitive labor around making dinner. Make a meal planner that helps people like my parents save money by making dishes sharing ingredients, and save time by avoiding single item trips. 

# Approach
First I found an API (yummly.com) with 1 million recipes and features like grocery list, recipe name, ID, cuisine, and course (ex: dinner, lunch, salads). I did exploratory analysis and cleaning using Python, Pandas and MongoDB. I graphed ingredient networks and recipe networks with NetworkX. 

# Outcome
The result is a meal planner that uses distance, and co-occurrence of ingredients to generate dinner plans.  

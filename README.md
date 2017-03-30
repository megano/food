# graph-theory

## Network Graph on Recipe and Ingredient Data ##
This project is analyzing relationships between recipes and ingredients within them. 
I’m looking at what ingredients are most important in a particular course, like “soup”. 
And what ingredients are shared across courses like “soup” and “salad”. 
So if I want to buy the least number of ingredients to make soups and salads, what will be on my short grocery shopping list? 

# The primary question: What core components are the "essence" of a particular type of food? 
To answer this I'll create a network of recipes and ingredients for a course like "soup", and find the most important ingredients. 

# Secondary question: What is the minimum set of ingredients I need to buy to make 1 soup and 2 salads each week for a 6 week period? 
I'll locate soups and salads that have the most similar ingredients. 

# Presentation: 
Slides + graph.

# Next steps:
- Get access to API
- Understand the data. Explore it. Put into graph.
-- Gauge how much signal might be in the data.
- subset the data by courses sousp and salads 
- Unsupervised learning: pick a salad, find most similar soup (via jacard similarity via soup to salad ingredients). Then salad and soup to 2nd salad.   
- Build a minimum viable product

# Data source: 
Yummly Api. 
- 1 Million recipes aggregated from multiple sources. 
- 100k+ classifications based on Food Genome & Yummly Algorithms: ingredients, diets, allergies, nutrition, taste, techniques & more. 
- 10 Billion+ Data Points to deliver relevant recipes to user.

# Future/Phase 2:
- Graph theory clustering: Try clustering ingredients and see if there's a connection to cuisines. Try modularity and divisive clustering.  
- Network Analysis and Visualization in Spark using GraphX 

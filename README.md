# graph-theory

## Network Graph on Recipe and Ingredient Data ##
Context: I find data about relationships between people, personal attributes and communities pretty interesting. I chose to explore these kinds of relationships with graph theory. Say we want to know what skills are key for various "developer" roles at a company like Amazon. Let's take a food analogy. Pretend each ingredient is a skill like "Ruby on Rails", the set of ingredients is the role "backend developer", and the larger group of roles "developers" is the "cuisine". What can we find out about this system?  

Primary question: What core components are the "essence" of a particular type of food?
Secondary question: What is the minimum set of ingredients I would need to buy to make 1 soup and 2 salads each week for a 6 week period?

Presentation: Slides + graph.

Next steps:
- (done) Get access to API
- (in progress) Understand the data. Explore it and put into graph.
-- Gauge how much signal might be in the data.
- subset the data by soup and salad to make it more manageable 
- Unsupervised learning: pick a salad, find most similar soup (via jacard similarity via soup to salad ingredients). Then salad and soup to 2nd salad.  
- Graph theory clustering: Try clustering ingredients and see if there's a connection to cuisines. Try modularity and divisive clustering.   
- (not started) Build a minimum viable product

Data source: Yummly Api. 
- 1 Million recipes aggregated from multiple sources. 
- 100k+ classifications based on Food Genome & Yummly Algorithms: ingredients, diets, allergies, nutrition, taste, techniques & more. 
- 10 Billion+ Data Points to deliver relevant recipes to user.

Future/Phase 2:
- Try with more of the data set on spark

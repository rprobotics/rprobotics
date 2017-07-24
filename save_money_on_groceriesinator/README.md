The 'create_dummy_json.py' script has a dependency on the output of the recipeSpider in the scrapinator directory.
The recipes scraped from the web are put in the 'pickle_recipes' directory, and create_dummy_json uses these files to
create json files to be consumed into a Django database with the loaddata command

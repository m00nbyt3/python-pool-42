from recipe import Recipe
from book import Book

first = Book('raul', 1, 2, {"starter":None, "lunch":None, "dessert":None})
first.add_recipe(Recipe('myrec', 1, 12, {"cheese", "bacon", "egg"}, 'lunch'))
myrec = first.get_recipe_by_name("myrec")
print(myrec)
myrec2 = first.get_recipe_by_type("lunch")
print(myrec2)
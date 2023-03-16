class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.recipe_type = recipe_type
		self.description = description
	def __str__(self):
		txt = ''
		txt = f"{self.name}:{self.ingredients}({self.cooking_time}mins, lvl{self.cooking_lvl})" 
		return str(txt)

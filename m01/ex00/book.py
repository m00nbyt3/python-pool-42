class Book:
	def __init__(self, name, last_updated, creation_date, recipes_list):
		self.name = name
		self.last_updated = last_updated
		self.creation_date = creation_date
		self.recipes_list = recipes_list
	
	def add_recipe(self, recipe):
		self.recipes_list[recipe.recipe_type] = recipe

	def get_recipe_by_name(self, name):
		for r in self.recipes_list.values():
			if r and r.name == name:
				return r

	def get_recipe_by_type(self, recipe_type):
		for r in self.recipes_list:
			if r == recipe_type:
				return self.recipes_list[r]


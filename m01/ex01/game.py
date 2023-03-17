class Crews:
	'''Class for getting the character'''
	def __init__(self, first_name=None, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

class GroveSt(Crews):
	'''Welcome to the fam homms''' 
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "GroveSt Family"
		self.house_words = "Here we go again"

	def print_crew_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False

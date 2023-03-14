tortilla = {
'ingredients': ['patata', 'huevo', 'sal'],
'meal': 'comida',
'prep_time': '30',
}

bocadillo = {
	'ingredients': ['jamon', 'pan', 'queso', 'tomate'],
	'meal': 'almuerzo',
	'prep_time': '10',
}

tarta = {
	'ingredients': ['harina', 'azucar', 'huevos'],
	'meal': 'postre',
	'prep_time': '60',
}

ensalada = {
	'ingredients': ['aguacate', 'rucula', 'tomates', 'espinacas'],
	'meal': 'almuerzo',
	'prep_time': '15',
}

cookbook = {
	'bocadillo': bocadillo,
	'tarta': tarta,
	'ensalada': ensalada,
}

def show_recipies(cookbook):
	print("List of recipies:")
	for i, data in enumerate(cookbook):
		print(' '+str(i)+'.', data)

def get_recipie(name):
	try:
		print("Detalles de:", name)
		for i, data in enumerate(cookbook[name]):
			if i == 0:
				print(' '+data+':', end = ' ')
				print(*cookbook[name][data], sep = ', ')
			else:
				print(' '+data+':', cookbook[name][data])
	except:
		print("Error al obtener la receta")

def remove_recipie(name):
	try:
		del cookbook[name]
	except:
		print("Error al eliminar la receta")

def add_recipie():
	name = input("Enter a name: ")
	ingredients = []
	print("Enter ingredients:")
	while True:
			toadd = input()
			if not toadd:
				break
			ingredients.append(toadd)
	meal = input("Enter a meal type: ")
	prep_time = input("Enter a preparation time: ")
	cookbook[name] = dict(ingredients = ingredients, meal = meal, prep_time = prep_time)

def menu():
	print("Welcome to the Python Cookbook!")
	print("List of available options:")
	print("  1. Add a recipie")
	print("  2. Delete a recipie")
	print("  3. Print a recipie")
	print("  4. Print the cookbook")
	print("  5. Quit")
	print("\nPlease select an option:")
	return input(">> ")

def selector(option):
	if option == 1:
		print('\n')
		add_recipie()
	elif option == 2:
		print('\n')
		name = input("Enter the name of the recipe to remove: ")
		print('\n')
		remove_recipie(name)
	elif option == 3:
		print('\n')
		name = input("Enter the name of the recipie to get details: ")
		print('\n')
		get_recipie(name)
	elif option == 4:
		print('\n')
		show_recipies(cookbook)
	elif option == 5:
		return True
	else:
		return False


def main():
	quit = 0
	while not quit:
		option = menu()
		if not option.isnumeric():
			print("\nOpcion invalida\n")
			continue
		quit = selector(int(option))
		print('\n')

if __name__ == '__main__':
	main()
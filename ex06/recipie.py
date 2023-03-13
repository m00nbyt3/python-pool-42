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
	print("Detalles de:", name)
	for i, data in enumerate(cookbook[name]):
		if i == 0:
			print(' '+data+':', end = ' ')
			print(*cookbook[name][data], sep = ', ')
		else:
			print(' '+data+':', cookbook[name][data])

def remove_recipie(name):
	del cookbook[name]

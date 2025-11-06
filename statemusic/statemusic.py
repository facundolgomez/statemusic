import requests

menu_active = True

while menu_active:
	print("Welcome")
	user_input = int(input("Ingrese un numero: "))
	if user_input == 2:
		menu_active = False

print("Terminó el programa")

requests.get()
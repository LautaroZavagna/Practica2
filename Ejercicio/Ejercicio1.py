#Una tienda de ropa vende remeras a $4000 cada una y pantalones a $8000 cada uno.
#El programa debe:
#Pedir al usuario cuántas remeras quiere.
#Pedir cuántos pantalones quiere.
#Calcular el total a pagar.
#Calcular cuánto dinero debería pagar si decide dar una seña del 30% del total.
#Mostrar en pantalla:
#Precio de las remeras
#Precio de los pantalones
#Total general
#Monto de la seña

PrecioRemera = 4000
PrecioPantalones = 8000

CantRemeras = int(input("Ingrese la cantidad de remeras que desea comprar: "))
CantPantalones = int(input("Ingrese la cantidad de pantalones que desea comprar: "))

TotalRemeras = CantRemeras * PrecioRemera
TotalPantalones = CantPantalones * PrecioPantalones
Total = TotalPantalones + TotalRemeras

Seña = Total * 0.30
print(f"Por la cantidad de remeras pedidas deberas pagar: {TotalRemeras}")
print(f"Por la cantidad de pantalones pedidos deberas pagar {TotalPantalones}")
print(f"El precio total de las remeras y pantalones pedidos es de {Total}")
print(f"Si decides dejar una seña del 30% deberas pagar {Seña}")






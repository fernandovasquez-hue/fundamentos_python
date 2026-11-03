#-------------------EJERCICIO 8-----------------------------
lapices = int(input('Ingrese el numero de lapices'))
cuadernos = int(input('Ingrese el numero de cuadernos'))
print(f'Cantidad de objetos totales: {lapices + cuadernos}')

#-------------------EJERCICIO 9-----------------------------
presupuesto = int(input('Ingrese su presupuesto'))
compra = int(input('Ingrese el valor de la compra'))
print(f'Dinero restante despues de la compra: {presupuesto - compra}')

#-------------------EJERCICIO 10----------------------------
precio = int(input('Ingrese el precio de las entradas:'))
cantidad = int(input('Ingrese la cantidad de entradas:'))
print(f'El precio total al comprar las entradas: {precio * cantidad}')

#-------------------EJERCICIO 11----------------------------
objetos = int(input('Ingrese la cantidad de objetos que son en total:'))
personas = int(input('Ingrese la cantidad de personas a quienes se le van a repartir:'))
print(f'Cantidad de objetos que tendria cada persona: {objetos / personas}')

#-------------------EJERCICIO 12----------------------------
estudiantes = int(input('Ingrese'))
equipos = int(input('Ingrese'))
print(f'Cantidad de estudiante que tendria cada equipo: {estudiantes // equipos}')
#-------------------EJERCICIO 13----------------------------
print(f'Cantidad de estudiante que quedarian sin equipo: {estudiantes % equipos}')

#-------------------EJERCICIO 14----------------------------
base = int(input('Ingrese'))
exponente = int(input('Ingrese'))
print(f'Resultado de 2 elevado a 5: {base ** exponente}')

#-------------------EJERCICIO 15----------------------------
nota1 = int(input('Ingrese'))
nota2 = int(input('Ingrese'))
nota3 = int(input('Ingrese'))
promedio = (nota1 + nota2 + nota3) / 3
print(f'''Nota numero uno: {nota1}
Nota numero dos: {nota2}
Nota numero tres: {nota3}
Pomedio final: {promedio}''')


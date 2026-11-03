
nombre = "Camila"
ciudad = "Santiago"
print(nombre)
print(ciudad)
print(type(nombre))

#--------------------EJERCICIO 3-------------------------------
pelicula = input('Ingrese nombre de la pelicula:')
videojuego = input('Ingrese su videojuego favorito:')
asignatura = input('Ingrese su asignatura meos preferida:')

print(pelicula)
print(videojuego)
print(type(asignatura))

#----------------------------EJERCICIO 4-------------------------
edad = int(input('Ingrese su edad:'))
hermanos = int(input('Ingrese la cantidad de hermanos que tiene:'))
año_actual = int(input('Ingrese el año actual:'))

print(f'Edad actual: {edad}')
print(f'Cantidad de hermanos: {hermanos}')
print(type(año_actual))

#----------------------------EJERCICIO 5-------------------------
precio = float(input('Ingrese precio del producto(debe contener un decimal y se coloca con un "."):'))
temperatura = float(input('Ingrese la temperatura (minimo con un decimal):'))
promedio = float(input('Ingrese su promedio:'))

print(f'Precio de un producto: {precio}')
print(f'Temperatura del dia de hoy: {temperatura}')
print(type(promedio))

#----------------------------EJERCICIO 6-------------------------
internet = True
terminar_tarea = False
clases_manana = True

print(f'Tienes internet: {internet}')
print(f'Has terminado la tarea: {terminar_tarea}')
print(type(clases_manana))

#---------------------------EJERCICIO 7---------------------------
nombre_producto = input('Ingresar el nombre del producto:')
cantidad_partes = int(input('Ingresar cantidad o las partes de su producto:'))
precio_producto = float(input('Ingresar precio del producto(minimo con un decimal):'))
disponibilidad = True
print(f'''Nombre del producto: {nombre_producto}
Tipo de el valor del nombre: {type(nombre_producto)}

En cuantas partes se vende: {cantidad_partes}
Tipo de el valor de las partes que son: {type(cantidad_partes)}

Precio de la bateria: {precio_bateria}
Tipo de el valor del precio: {type(precio_bateria)}

Hay disponibilidad del producto: {disponibilidad}
Tipo de el valor del nombre: {type(disponibilidad)}
''')
"""
  @autor: andresGPY22
  nombre: ejercicio1.py
  descripción: ...

  Andres Jimenez -- 18
  Su suma de notas es: 30
  Su promedio es: 15
"""
# System.out.println("Ingrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre")
edad = input("Ingrese su edad)")
nota1 = input("Ingrese el valor de su nota 1: ")
nota2 = input("Ingrese el valor de su nota 2: ")

suma = int(nota1) + int(nota2);
promedio = int(suma)/2;
print("%s -- %s\n Su suma de nota es %s\n Su promedio es %s" % 
	(nombre, edad, suma, promedio))

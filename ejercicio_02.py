"""
EJERCICIO 02: Validación de contraseña segura

Implementa una función que reciba una contraseña y verifique: 
    1. Que tenga al menos 8 caracteres de longitud.
    2. Que contenga al menos un número (puedes usar un bucle o una verificación con dígitos).
    3. Que contenga al menos una letra mayúscula.

La función debe retornar True si cumple todas las condiciones, y False en caso contrario. 
(Ayuda: puedes crear funciones auxiliares pequeñas para cada validación, fomentando la modularidad de tu programa).

Ejemplos de casos de prueba:
    - es_contrasena_segura("Python123") -> True
    - es_contrasena_segura("clave") -> False
    - es_contrasena_segura("12345678") -> False
"""
contrasena = input("Escriba una contraseña: ")

if len(contrasena) < 8:
    print("La contraseña debe ser de al menos 8 caracteres")
else: 
    for i in contrasena: 
        if i.isdigit():
            print("La contraseña debe tener al menos un número")
            break
    else:
        for i in contrasena: 
            if i.isupper():
                print("La contraseña debe tener al menos una letra mayúscula")
                break
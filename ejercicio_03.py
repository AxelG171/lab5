"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""

mes = int(input("ingrese el mes actual: "))
dia = int(input("ingrese el dia actual: "))

for i in mes:
    if mes <= 0 or mes > 12:
        print("el mes ingresado no es valido")
        break
    else: 
         for i in mes and dia:
             if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                 if dia <= 0 or dia > 31:
                     print("el dia ingresado no es valido")
                     break
             elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                 if dia <= 0 or dia > 30:
                     print("el dia ingresado no es valido")
             else: mes == 2
             if dia <= 0 or dia > 28:
                 print("el dia ingresado no es valido")
                 break
         else:
            dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            dias_que_van_del_año = sum(dias_por_mes[:mes-1]) + dia
            print(f"llevamos {dias_que_van_del_año} días del año.")
            


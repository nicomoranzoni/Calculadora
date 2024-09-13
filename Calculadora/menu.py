import os
from funciones import *

def menu():
    bandera_numero_uno = False
    bandera_numero_dos = False
    bandera_operaciones = False

    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            
            primer_operando = int(input("Ingrese primer operando: "))
            bandera_numero_uno = True
        elif opcion == 2:
            
            segundo_operando = int(input("Ingrese segundo operando: "))
            bandera_numero_dos = True
        elif opcion == 3:
            #Puedo ingresar a esta opcion
            if bandera_numero_uno == True and bandera_numero_dos == True:
                resultado_suma = sumar(primer_operando, segundo_operando)
                resultado_resta = resta(primer_operando, segundo_operando)
                resultado_divir = dividir(primer_operando, segundo_operando)
                resultado_multiplicar = multiplicar(primer_operando, segundo_operando)
                resultado_potencia = calcular_potencia(primer_operando, segundo_operando)
                resultado_resto = calcular_resto(primer_operando, segundo_operando)
                resultado_factorial_a = calcular_factorial(primer_operando)
                resultado_factorial_b = calcular_factorial(segundo_operando)
                print("Se calcularon todas las operaciones")
                bandera_operaciones = True
            else:
                print("No se puede ingresar a la opcion 3 hasta no tener ambos operandos")


            
        elif opcion == 4:
            if bandera_operaciones == True:
                print("Informo todos los resultados")
                print(f"""El resultado de sumar {primer_operando} + {segundo_operando} es: {resultado_suma}
                El resultado de restar {primer_operando} - {segundo_operando} es: {resultado_resta}
                El resultado de dividir {primer_operando}/{segundo_operando} es: {resultado_divir}
                El resultado de multiplacar {primer_operando}*{segundo_operando}: {resultado_multiplicar}
                {primer_operando} elevevado a la {segundo_operando} da como resultado: {resultado_potencia}
                El resultado de {primer_operando} % {segundo_operando} es {resultado_resto}
                El factorial de {primer_operando} es: {resultado_factorial_a} y el factorial de {segundo_operando} es: {resultado_factorial_b}  
                        """)
            else:
                print("No puede ingresar a ver las operaciones")
            print()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()

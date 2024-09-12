import os
from funciones import *

def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            
            primer_operando = int(input("Ingrese primer operando: "))
        elif opcion == 2:
            
            segundo_operando = int(input("Ingrese segundo operando: "))
        elif opcion == 3:
            print("Calculo todas las operaciones")
            sumar(primer_operando, segundo_operando)
            resta(primer_operando, segundo_operando)
            dividir(primer_operando, segundo_operando)
            multiplicar(primer_operando, segundo_operando)
            calcular_potencia(primer_operando, segundo_operando)
            calcular_resto(primer_operando, segundo_operando)
            calcular_factorial(primer_operando)
            calcular_factorial(segundo_operando)
        elif opcion == 4:
            print("Informo todos los resultados")
            print(f"""El resultado de sumar {primer_operando} + {segundo_operando} es: {sumar(primer_operando, segundo_operando)}
            El resultado de restar {primer_operando} - {segundo_operando} es: {resta(primer_operando, segundo_operando)}
            El resultado de dividir {primer_operando}/{segundo_operando} es: {dividir(primer_operando, segundo_operando)}
            El resultado de multiplacar {primer_operando}*{segundo_operando}: {multiplicar(primer_operando, segundo_operando)}
            {primer_operando} elevevado a la {segundo_operando} da como resultado: {calcular_potencia(primer_operando, segundo_operando)}
            El resultado de {primer_operando} % {segundo_operando} es {calcular_resto(primer_operando, segundo_operando)}
            El factorial de {primer_operando} es: {calcular_factorial(primer_operando)} y el factorial de {segundo_operando} es: {calcular_factorial(segundo_operando)}




            """)
            print()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()

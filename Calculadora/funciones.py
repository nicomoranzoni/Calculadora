def sumar (numero:int, numero_dos:int) -> int:
    '''
    - Funcion que se encarga de realizar suma
    - Recibe dos numeros
    - Retorna la suma de los dos valores recibidos
    '''
    resultado = numero + numero_dos
    return resultado

def resta (numero:int, numero_dos:int) -> int:

    '''
    - Funcion que se encarga de realizar resta
    - Recibe dos numeros
    - Retorna la resta de los parametros recibidos
    '''

    resultado = numero - numero_dos
    return resultado

def dividir (numero:int, numero_dos:int) -> float:

    '''
    - Funcion que se encarga de realizar una division.
    - Recibe dos numeros.
    - Retorna el resultado de la division entre los parametros recibidos.
    '''
    if numero_dos != 0:
        resultado = numero / numero_dos
    else:
        #3 Opciones:
        # resultado = 0
        # resultado = None 
        # resultado -> str con mensaje de error
        resultado = "No se puede dividir por 0"

    return resultado


def multiplicar (numero:int, numero_dos:int) -> int:
    
    '''
    - Funcion que se encarga de realizar multiplicación
    - Recibe dos numeros
    - Retorna el resultado de la multiplicación de los parametros recibidos.
    '''

    
    resultado = numero * numero_dos
    return resultado 

def calcular_potencia (numero:int, numero_dos:int) -> int:

    '''
    - Funcion que se encarga de realizar la potencia entre dos numeros
    - Recibe dos numeros
    - Retorna el resultado de la potencia de los parametros recibidos.
    '''

    resultado = numero ** numero_dos
    return resultado


def calcular_resto (numero:int, numero_dos:int) -> int:

    '''
    - Funcion que se encarga de calcular el resto
    - Recibe dos numeros
    - Retorna el resto de los operacion entre los parametros recibidos.
    '''
    
    if numero_dos != 0:
        resultado = numero % numero_dos
    else:
        resultado = "No se puede dividir por cero, por lo que no se calculó el resto"
    
    return resultado
    
def calcular_factorial (numero:int) -> int:
    '''
    - Funcion que se encarga de calcular el factorial
    - Recibe un numero
    - Retorna el factorial del parametro ingresado.
    '''

    if numero > 1:
        #Calcular factorial
        resultado = numero * calcular_factorial(numero - 1)

        
    else:
        resultado = 1 


    return resultado
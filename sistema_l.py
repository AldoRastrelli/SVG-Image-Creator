from cola import Cola
from math import radians
UNIDAD_DE_AVANCE = 50

def elementos_sistema_l(ruta):
    """Devuelve el alfabeto, el axioma y las reglas del sistema-L"""

    archivo = open(ruta,'r')

    angulo = radians(float(archivo.readline()))
    axioma = archivo.readline()
    
    reglas_sistema_l = {}
    linea = archivo.readline().rstrip('\n')
    
    while linea:
        simbolo = linea[0]
        secuencia_generada = linea[2:]
        reglas_sistema_l.update({simbolo : secuencia_generada})
        
        linea = archivo.readline().rstrip('\n')

    archivo.close()
    return angulo, axioma, reglas_sistema_l

def iterar_sistema_l(iteraciones,axioma,reglas_sistema_l):
    """itera el sistema-l según el número de iteraciones ingresado por comando."""

    if iteraciones == 0:
        return axioma

    iterado = ""
    secuencia = axioma

    for caracter in secuencia:
        iterado += reglas_sistema_l.get(caracter,caracter)
    secuencia = iterado
    iteraciones -= 1

    if iteraciones != 0:
        return iterar_sistema_l(iteraciones, secuencia, reglas_sistema_l)
    
    return secuencia

def transcribir_secuencia(secuencia):
    """transcribe la secuencia de símbolos recibidos en forma de elementos significativos y los encola. Se devuelve una Cola al final.
    Los simbolos de avance (FG y fg) son acumulativos y se suman entre sí para dar una unidad -numero entero- de avance.
    Los cambios de pluma (fg) se encolan como "True" para "pluma abajo" y "False" para "pluma arriba".
    Los demás símbolos posibles se encolan como sí mismos""" 


    estados = Cola()
    avance = 0
    pluma = True

    for accion in secuencia:

        if accion in 'FG':
            if not pluma:
                estados.encolar(avance)
                avance = 0
                pluma = True
                estados.encolar(pluma)
            avance += UNIDAD_DE_AVANCE
            continue
       
        elif accion in 'fg':
        
            if pluma:
                estados.encolar(avance)
                avance = 0
                pluma = False
                estados.encolar(pluma)
            avance += UNIDAD_DE_AVANCE
            continue
        
        else:
            estados.encolar(avance)
            avance = 0
            estados.encolar(accion)
    
    if avance != 0:
        estados.encolar(avance)
    return estados

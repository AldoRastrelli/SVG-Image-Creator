import sys
import sistema_l
import svg

def main():
    """Desarrollo principal del programa"""

    try: 
        archivo = sys.argv[1]
        iteraciones = sys.argv[2]
        destino = sys.argv[3]
    except IndexError:
        print('Faltan ingresar parámetros.\nDebe ingresarse:\n- el archivo del SISTEMA-L\n- el NÚMERO de ITERACIONES\n- el archivo de DESTINO\nen ese orden.')
        return 

    if not validar_iteraciones(archivo,iteraciones):
        return
    iteraciones = int(iteraciones)

    try:    
        angulo, axioma, reglas = sistema_l.elementos_sistema_l(archivo)
    except IOError:
        print('El archivo del sistema-L no es válido ')
        return
    
    secuencia = sistema_l.iterar_sistema_l(iteraciones,axioma,reglas)  
    estados = sistema_l.transcribir_secuencia(secuencia)
    
    estados_inflexivos = svg.guardar_estados_clave(estados,angulo)
    # Estados inflexivos son todos aquellos que determinan un cambio en el diseño del dibujo.

    datos_svg = svg.convertir_datos_svg(estados_inflexivos)
    svg.generar_imagen(datos_svg,destino)
    print('Su imagen ha sido generada.')

def validar_iteraciones(archivo,iteraciones):
    """valida que el archivo pasado por parámetro exista y que las iteraciones sean un número entero. 
    Si son válidos, devuelve True. De lo contrario, informa al usuario y devuelve False."""

    if not iteraciones.isdigit():
        print('El número de iteraciones ingresado no es válido. Debe ser un entero.')
        return False
    
    return True

main()
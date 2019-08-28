from tortuga import Pluma
from tortuga import Tortuga
from cola import Cola
from pila import Pila

MARGEN = 50
CAMBIO_DE_TORTUGA = ['*' , '*' , '*']

def guardar_estados_clave(estados,angulo):
    """Devuelve una cola con los estados clave (de inflexión) que definen dibujo"""

    pluma = Pluma()
    tortuga = Tortuga(pluma)
    estados_clave = Cola()
    pila_tortugas = Pila()

    encolar_estado_clave(tortuga, estados_clave) #guarda la posición [0,0] con orientación 0 y pluma = True como "inicio"

    for _ in range(len(estados.items)):
        accion = estados.desencolar()
        if not str(accion).isdigit():
        
            if type(accion) == bool:
                tortuga.pluma.cambiar_estado()
            elif accion == '+':
                tortuga.derecha(angulo)
            elif accion == '-':
                tortuga.izquierda(angulo)
            elif accion == '|':
                tortuga.orientacion += radians(180)
            elif accion == '[':
                tortuga = apilar_tortuga(tortuga, pila_tortugas)
            elif accion == ']':
                encolar_estado_clave(tortuga, estados_clave)
                estados_clave.encolar(CAMBIO_DE_TORTUGA)
                tortuga = desapilar_tortuga(tortuga, pila_tortugas)

            encolar_estado_clave(tortuga, estados_clave)
        else:
            tortuga.adelante(accion)
    
    encolar_estado_clave(tortuga, estados_clave)
    return estados_clave

def encolar_estado_clave(tortuga,estados_clave):
    """agrega a la cola un estado clave"""

    estado = [tortuga.posicion[0], tortuga.posicion[1], tortuga.pluma.estado]
    estados_clave.encolar(estado)

def apilar_tortuga(tortuga, pila_tortugas):
    """apila una tortuga en la pila de tortugas"""

    pila_tortugas.apilar(tortuga)
    nueva_tortuga = Tortuga(tortuga.pluma, tortuga.posicion[0], tortuga.posicion[1], tortuga.orientacion)

    return nueva_tortuga

def desapilar_tortuga(tortuga, pila_tortugas):
    """desapila la tortuga de la linea de tortugas y reinicia el objeto Tortuga en ese valor"""

    try:
        nueva_tortuga = pila_tortugas.desapilar()
    except IndexError:
        return tortuga

    return nueva_tortuga

def convertir_datos_svg(estados_clave):
    """convierte los estados clave recibidos en datos del SVG"""

    # Formato estados_clave: [X, Y, estado_pluma] con estado_pluma = True or False
    datos_svg = []

    anterior = estados_clave.desencolar()
    x = anterior[0]
    y = anterior[1]
    pluma = anterior[2]

    datos_svg.append(['M',str(x),str(-y)])

    try:
        siguiente = estados_clave.desencolar()
    except ValueError:
        return datos_svg
    
    x2 = siguiente[0]
    y2 = siguiente[1]
    
    for _ in range(len(estados_clave.items)):
        

        if x != x2 or y != y2:

            if siguiente == CAMBIO_DE_TORTUGA:
                try:
                    siguiente =  estados_clave.desencolar()
                except ValueError:
                    break

                x = siguiente[0]
                y = siguiente[1]
                datos_svg.append(['M',str(x),str(-y)])
                
            elif pluma:
                datos_svg.append(['L',str(x2),str(-y2)])
            else:
                datos_svg.append(['M',str(x2),str(-y2)])
        
        anterior = siguiente
        try:
            siguiente =  estados_clave.desencolar()
        except ValueError:
            break

        x2 = siguiente[0]
        y2 = siguiente[1]
        orientacion2 = siguiente[2]

        x = anterior[0]
        y = anterior[1]
        pluma = anterior[2]

    return datos_svg

def generar_imagen(datos_svg, destino):
    """genera la imagen a partir de los datos SVG y la guarda en '{destino}'."""
    
    pluma = Pluma()
    x = []
    y = []
    for elemento in datos_svg:
        
        x.append(int(float(elemento[1])))
        y.append(int(float(elemento[2])))
    
    min_x_visible = min(x) - MARGEN
    min_y_visible = min(y) - MARGEN
    ancho = max(x) - min(x) + MARGEN * 2
    alto = max(y) - min(y) + MARGEN * 2
    
    dibujo = ""
    for elemento in datos_svg:
        dibujo += " ".join(elemento) + " "
    
    archivo = open(destino,'w+')
    archivo.write(f'<svg viewBox="{min_x_visible} {min_y_visible} {ancho} {alto}" xmlns="http://www.w3.org/2000/svg">\n')
    archivo.write(f'<path d="{dibujo}" stroke-width="{pluma.ancho}" stroke="{pluma.color}" fill="none"/>\n')
    archivo.write('</svg>')
    archivo.close()


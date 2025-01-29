import json
import argparse
from dfa import *

def cargar_datos(ruta_archivo):
    with open(ruta_archivo, "r") as a:
            datos = json.load(a)
    return datos

def crear_json(archivo_origen, cadena, resultado, aceptada):
    datos = {
        "type": "simulacion_dfa",
        "dfa": archivo_origen,
        "cadena": cadena,
        "resultado": resultado,
        "aceptada": aceptada
    }

    nombre_archivo = f"simulacion_{archivo_origen}"

    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

    print(f"{nombre_archivo} creado!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", type=str)
    parser.add_argument("cadena", type=str)
    
    # Parsear los argumentos
    args = parser.parse_args()

    try:
        datos = cargar_datos(args.archivo)
    
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo {args.archivo}")

    cadena = args.cadena

    dfa = DFA(datos["Q"], datos["Sigma"], datos["Delta"], datos["q0"], datos["F"])
    aceptada, visitados = dfa.run(cadena)

    crear_json(args.archivo, cadena, visitados, aceptada)

if __name__ == "__main__":
    main()
import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils_persistencia import cargar_json, exportar


"""
Base de datos en memoria con diccionario + persistencia JSON/CSV.
Clave: patente normalizada
Valor: dict con empresa, hora, estado
"""



from utils_persistencia import cargar_json, exportar

def normalizar(s: str) -> str:
    return s.replace("-", "").replace(" ", "").upper()

def menu():
    # base_datos.py
    print("\n=== Base de Datos (Memoria + Persistencia) ===")
    print("1) Agregar/Actualizar acceso")
    print("2) Buscar acceso por patente")
    print("3) Listar todos")
    print("4) Eliminar acceso por patente")
    print("0) Salir")

def main():
    accesos = cargar_json()  # Carga inicial
    while True:
        menu()
        op = input("Elige: ").strip()
        if op == "1":
            p = normalizar(input("Patente: "))
            empresa = input("Empresa: ").strip()
            hora = input("Hora (HH:MM): ").strip()
            estado = input("Estado (Permitido/Denegado/Visita): ").strip().title()
            accesos[p] = {"empresa": empresa, "hora": hora, "estado": estado}
            exportar(accesos)
            print("Guardado/Actualizado (JSON/CSV).")
        elif op == "2":
            p = normalizar(input("Patente a buscar: "))
            data = accesos.get(p)
            if data:
                print(f"{p} → {data}")
            else:
                print("No encontrado.")
        elif op == "3":
            if not accesos:
                print("Sin registros.")
            else:
                for p, d in accesos.items():
                    print(f"{p} → Empresa: {d['empresa']} | Hora: {d['hora']} | Estado: {d['estado']}")
        elif op == "4":
            p = normalizar(input("Patente a eliminar: "))
            if p in accesos:
                del accesos[p]
                exportar(accesos)
                print("Eliminado (JSON/CSV actualizado).")
            else:
                print("No existe.")
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
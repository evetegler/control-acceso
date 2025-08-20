import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils_persistencia import cargar_json, exportar


"""
Sistema modular de control de acceso con persistencia JSON/CSV.
Usa funciones para reutilizar lógica y utilidades de persistencia.
"""

from utils_persistencia import cargar_json, exportar

# Lista de patentes autorizadas de ejemplo (puedes moverla a un archivo externo si deseas persistencia)
AUTORIZADAS = {"ABC123", "AB1234", "CD4567", "ZX99AA", "KLMN12"}

def normalizar(s: str) -> str:
    return s.replace("-", "").replace(" ", "").upper()

def registrar_acceso(accesos: dict, patente: str, empresa: str, hora: str, estado: str):
    p = normalizar(patente)
    accesos[p] = {"empresa": empresa, "hora": hora, "estado": estado.title()}
    exportar(accesos)  # Persistir de inmediato
    return p

def verificar_acceso(patente: str) -> str:
    p = normalizar(patente)
    if p in AUTORIZADAS:
        return "Permitido"
    elif p.isalnum() and 4 <= len(p) <= 7:
        return "No registrado"
    else:
        return "Formato inválido"

def listar_accesos(accesos: dict):
    if not accesos:
        print("Sin accesos registrados.")
    else:
        for p, d in accesos.items():
            print(f"{p} → Empresa: {d['empresa']} | Hora: {d['hora']} | Estado: {d['estado']}")

def menu():
    print("\n=== Sistema de Control de Acceso (Funciones + Persistencia) ===")
    print("1) Verificar patente")
    print("2) Registrar acceso")
    print("3) Listar accesos")
    print("0) Salir")

def main():
    accesos = cargar_json()  # Cargar registros previos
    while True:
        menu()
        op = input("Elige: ").strip()
        if op == "1":
            placa = input("Patente: ")
            resultado = verificar_acceso(placa)
            print(f"Resultado: {resultado}")
        elif op == "2":
            placa = input("Patente: ")
            empresa = input("Empresa: ")
            hora = input("Hora (HH:MM): ")
            estado = verificar_acceso(placa)
            p = registrar_acceso(accesos, placa, empresa, hora, estado)
            print(f"Acceso para {p} registrado con estado '{estado}'. (Guardado JSON/CSV)")
        elif op == "3":
            listar_accesos(accesos)
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
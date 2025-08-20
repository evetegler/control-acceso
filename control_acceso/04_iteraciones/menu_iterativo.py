"""
Menú iterativo de ejemplo para control de acceso.
Demuestra while (repetición) y for (recorrido de colecciones).
"""

def menu():
    print("\n=== Menú Iterativo (Demo) ===")
    print("1) Registrar ingreso (simulado)")
    print("2) Listar últimos N ingresos (simulado)")
    print("0) Salir")

def main():
    ultimos = ["AB1234", "CD4567", "ABC123", "ZX99AA", "KLMN12"]
    registros = []

    while True:
        menu()
        op = input("Elige: ").strip()
        if op == "1":
            p = input("Patente: ").strip().upper()
            registros.append(p)
            print(f"Ingreso registrado para {p}. Total registros: {len(registros)}")
        elif op == "2":
            try:
                n = int(input("¿Cuántos quieres ver?: "))
            except ValueError:
                print("Número inválido.")
                continue
            print("-- Últimos N (lista fija + registros) --")
            # Recorrido con for
            for i, placa in enumerate((ultimos + registros)[-n:], start=1):
                print(f"{i}. {placa}")
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
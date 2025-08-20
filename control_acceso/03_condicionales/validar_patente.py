"""
Valida si una patente está autorizada.
"""

AUTORIZADAS = {"ABC123", "AB1234", "CD4567", "ZX99AA", "KLMN12"}  # Ejemplos

def normalizar(s: str) -> str:
    return s.replace("-", "").replace(" ", "").upper()

def main():
    print("=== Validación de Patente ===")
    placa = input("Patente: ")
    p = normalizar(placa)

    if p in AUTORIZADAS:
        print(f"Patente {p}: ACCESO PERMITIDO")
    elif p.isalnum() and 4 <= len(p) <= 7:
        print(f"Patente {p}: NO REGISTRADA (solicitar autorización)")
    else:
        print(f"Patente {p}: FORMATO INVÁLIDO (rechazada)")

if __name__ == "__main__":
    main()
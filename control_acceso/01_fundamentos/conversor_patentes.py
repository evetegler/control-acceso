"""
Conversor/normalizador de patentes.
Demuestra variables, operadores, entrada/salida y control básico.
"""

def normalizar_patente(raw: str) -> str:
    # Quitar espacios y guiones, y pasar a mayúsculas
    limpia = raw.replace("-", "").replace(" ", "").upper()
    return limpia

def main():
    print("=== Conversor de Patentes ===")
    original = input("Ingresa la patente (ej: ab-cd12, abc123, ab 1234): ")
    normal = normalizar_patente(original)
    print(f"Normalizada: {normal}")
    print(f"Largo: {len(normal)} caracteres")
    # Ejemplo muy simple de chequeo de patrón básico (solo letras y/o números)
    solo_alnum = normal.isalnum()
    print(f"¿Solo letras y/o números? {solo_alnum}")

if __name__ == "__main__":
    main()
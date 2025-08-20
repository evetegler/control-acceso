"""
Formulario simple que utiliza str, int (para año), bool y muestra resumen.
"""

def str_a_bool(valor: str) -> bool:
    return valor.strip().lower() in {"s", "si", "sí", "y", "yes", "true", "t", "1"}

def main():
    print("=== Registro de visitante/vehículo ===")
    rut = input("RUT (str): ").strip()
    nombre = input("Nombre (str): ").strip()
    empresa = input("Empresa (str): ").strip()
    tipo_vehiculo = input("Tipo de vehículo (auto/camioneta/camión) (str): ").strip()
    anio = int(input("Año del vehículo (int): ").strip())
    proveedor_habitual = str_a_bool(input("¿Proveedor habitual? (s/n): "))

    print("\n--- Resumen ---")
    print(f"RUT: {rut} (tipo: {type(rut).__name__})")
    print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
    print(f"Empresa: {empresa} (tipo: {type(empresa).__name__})")
    print(f"Tipo de vehículo: {tipo_vehiculo} (tipo: {type(tipo_vehiculo).__name__})")
    print(f"Año: {anio} (tipo: {type(anio).__name__})")
    print(f"Proveedor habitual: {proveedor_habitual} (tipo: {type(proveedor_habitual).__name__})")

if __name__ == "__main__":
    main()
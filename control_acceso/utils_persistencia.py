"""
Utilidades de persistencia en JSON y CSV para el Sistema de Control de Acceso.
Los archivos se guardan en la carpeta `data/` (vecina a los módulos).
"""

import os, json, csv
from typing import Dict, Any, List

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
JSON_FILE = os.path.join(DATA_DIR, "accesos.json")
CSV_FILE = os.path.join(DATA_DIR, "accesos.csv")

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def cargar_json() -> Dict[str, Any]:
    _ensure_data_dir()
    if not os.path.exists(JSON_FILE):
        return {}
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def guardar_json(data: Dict[str, Any]) -> None:
    _ensure_data_dir()
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _fila_desde_registro(patente: str, reg: Dict[str, Any]) -> List[str]:
    return [
        patente,
        reg.get("empresa", ""),
        reg.get("hora", ""),
        reg.get("estado", ""),
    ]

def guardar_csv(data: Dict[str, Any]) -> None:
    _ensure_data_dir()
    encabezados = ["patente", "empresa", "hora", "estado"]
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)
        for p, reg in data.items():
            writer.writerow(_fila_desde_registro(p, reg))

def exportar(data: Dict[str, Any]) -> None:
    """
    Guarda simultáneamente JSON y CSV para mantener ambos formatos al día.
    """
    guardar_json(data)
    guardar_csv(data)
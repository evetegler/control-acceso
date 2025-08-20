# Sistema de Control de Acceso (Portafolio Python)

Este repositorio contiene un **Sistema de Control de Acceso de Vehículos y Proveedores** diseñado para evidenciar los **requerimientos mínimos** de la evaluación del portafolio (variables, tipos de datos, condicionales, iteraciones, estructuras de datos y funciones).

## Estructura
- `01_fundamentos/` – Variables y operadores: normalización de patentes.
- `02_tipos_datos/` – Tipos de datos: registro de visitante/vehículo.
- `03_condicionales/` – If/elif/else: validación de patentes autorizadas.
- `04_iteraciones/` – Bucles: menú iterativo de acciones.
- `05_estructuras_datos/` – Diccionarios: pequeña "base de datos" en memoria.
- `06_funciones/` – Modularización del sistema: registrar/verificar/listar accesos.

## Requisitos
- Python 3.10+ (sin dependencias externas).

## Ejecución rápida
```bash
# Ejecutar módulos individuales
python 01_fundamentos/conversor_patentes.py
python 02_tipos_datos/registro_usuario.py
python 03_condicionales/validar_patente.py
python 04_iteraciones/menu_iterativo.py
python 05_estructuras_datos/base_datos.py
python 06_funciones/control_acceso.py
```

## Flujo sugerido
1. **06_funciones/control_acceso.py** es el "menú principal" más completo.
2. Usa utilidades de las demás carpetas para mostrar el dominio de cada tema.

## GitHub
1. Crea un repositorio vacío en GitHub (sin README inicial).
2. En la carpeta del proyecto:
```bash
git init
git add .
git commit -m "Estructura inicial: Sistema de Control de Acceso (portafolio)"
git branch -M main
git remote add origin <URL-DE-TU-REPO>.git
git push -u origin main
```
3. Realiza **al menos tres commits** adicionales con mensajes descriptivos
   (ej.: "mejora validación de patente", "agrega persistencia JSON", "actualiza README").

## Licencia
Uso educativo. Adáptalo a tu contexto (por ejemplo, Segurycel).

---

## Persistencia
Se agregó **persistencia en JSON y CSV** (carpeta `data/`) mediante `utils_persistencia.py`.
- Los módulos de **05_estructuras_datos** y **06_funciones** ahora **cargan/guardan** automáticamente.
- Puedes abrir `data/accesos.json` o `data/accesos.csv` para ver los registros.

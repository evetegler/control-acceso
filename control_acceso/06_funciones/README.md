# 06 – Funciones: control_acceso.py

Sistema modular que **registra**, **verifica** y **lista** accesos usando **funciones**.
Este archivo es un menú "principal" simple para demostrar reutilización.

```bash
python 06_funciones/control_acceso.py
```

---
### Persistencia
Este módulo ahora **carga** registros desde `data/accesos.json` al iniciar y **guarda** automáticamente en **JSON y CSV** (`data/accesos.json` y `data/accesos.csv`) cada vez que se modifica la base.

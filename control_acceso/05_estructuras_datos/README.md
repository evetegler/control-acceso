# 05 – Estructuras de datos: base_datos.py

Pequeña "base de datos" en **diccionario** (en memoria) para accesos:
- Agregar
- Buscar
- Listar
- Eliminar

```bash
python 05_estructuras_datos/base_datos.py
```

---
### Persistencia
Este módulo ahora **carga** registros desde `data/accesos.json` al iniciar y **guarda** automáticamente en **JSON y CSV** (`data/accesos.json` y `data/accesos.csv`) cada vez que se modifica la base.

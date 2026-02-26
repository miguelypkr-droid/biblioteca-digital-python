# Biblioteca Digital (POO en Python)

Proyecto educativo para practicar **Programación Orientada a Objetos** en Python combinando **clases, listas y diccionarios**. Incluye actividades para principiantes y avanzados, código plantilla y **pruebas unitarias**.

## 🎯 Objetivos
- Modelar un dominio con clases (`Libro`, `Usuario`, `Prestamo`, `Biblioteca`).
- Usar **listas** para colecciones y **diccionarios** como índices/historiales.
- Implementar reglas de negocio, búsquedas y **reportes**.
- Ejecutar **tests unitarios** con `unittest`.

## 🧩 Componentes principales
- Código en `src/biblioteca/`
- Pruebas en `tests/`
- Actividades detalladas en `docs/`

## 🛠️ Requisitos
- Python **3.9+** (recomendado 3.10 o superior)

## 🚀 Instalación
```bash
# Clonar el repositorio (o descargar zip)
# git clone <URL-del-repo> && cd biblioteca-digital-python

# Crear entorno virtual
python -m venv .venv

# Activar entorno
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

## ✅ Ejecutar pruebas unitarias
Usa `unittest` (estándar en Python, **no requiere paquetes extra**):

```bash
# Desde la raíz del repo
python -m unittest discover -s tests -p "test_*.py" -v
```

## ▶️ Demo rápida
```bash
# (Opcional) Ejecutar el demo
python -m src.biblioteca.main_demo
```

## 📂 Estructura
```text
src/biblioteca/
  ├─ libro.py        # Clase Libro
  ├─ usuario.py      # Clase Usuario
  ├─ prestamo.py     # Clase Prestamo
  ├─ biblioteca.py   # Orquestación y reglas de negocio
  └─ main_demo.py    # Script de demostración
```

## 🔍 Licencia y uso
Uso académico. Puedes reutilizar y modificar con atribución.

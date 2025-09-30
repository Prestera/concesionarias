# 🚗 Sistema de Gestión de Autos y Concesionarias

Este proyecto es una aplicación de consola en **Python** que permite gestionar autos dentro de distintas concesionarias.  
Fue desarrollado con fines de práctica en **Programación Orientada a Objetos (POO)**, manejo de archivos **JSON** y organización modular de código en Python.  

---

## ✨ Funcionalidades principales

- 📥 **Agregar autos** a una concesionaria.
- 📋 **Listar todos los autos** cargados en el sistema.
- 🔎 **Buscar autos** por concesionaria y/o modelo.
- ✏️ **Editar autos** (con reubicación automática si cambia de marca/concesionaria).
- 🗑️ **Eliminar autos** con confirmación.
- 🆔 **Gestión de IDs únicos** para cada auto, reutilizando los IDs libres.
- 💾 **Persistencia en JSON** para mantener los datos entre ejecuciones.

---

## 🛠️ Tecnologías utilizadas

- [Python 3.x](https://www.python.org/)  
- Módulos estándar: `json`  
- Programación Orientada a Objetos (clases `Autos` y `Concesionaria`)  

---

## 📂 Estructura del proyecto

```
.
├── autos.py             # Clase Autos
├── concesionarias.py    # Clase Concesionaria
├── config.py            # Diccionario con concesionarias iniciales
├── autos_cliente.py     # Script principal con el menú
├── autos.json           # Base de datos en formato JSON
└── README.md            # Este archivo
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. Asegurarse de tener **Python 3** instalado:
   ```bash
   python --version
   ```

3. Ejecutar el programa principal:
   ```bash
   python autos_cliente.py
   ```

---

## 📖 Ejemplo de uso

```
=== Menú Concesionarias ===
1. Agregar auto
2. Listar autos
3. Buscar autos por concesionaria
4. Editar auto
5. Eliminar auto
6. Salir
```

### ➕ Agregar auto
```
Ingrese la marca del auto: Toyota
Ingrese el modelo: Corolla
Ingrese el año del auto: 2022
¿El auto es 0 km? (si/no): si
✅ Auto agregado a Concesionaria Ginza
```

### 🔎 Buscar autos
```
Ingrese el nombre de la concesionaria: Ginza
Autos en Concesionaria Ginza:
Id: 1 Marca: Toyota, Modelo: Corolla, Año: 2022, Estado: Nuevo
```

---

## 📌 Próximos pasos / mejoras

- Agregar **filtros avanzados** (ej: por año o por estado).  
- Implementar exportación de reportes en **CSV** o **Excel**.  
- Interfaz gráfica simple con **Tkinter** o una API REST con **Flask/FastAPI**.  
- Tests unitarios con `unittest` o `pytest`.  

---

## 👨‍💻 Autor

Proyecto desarrollado por **Hernán Prestera** como práctica de Programación en Python y POO.  

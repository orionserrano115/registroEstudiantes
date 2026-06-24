# 📚 Sistema de Registro de Estudiantes

Aplicación web full stack para gestionar el registro de estudiantes de una institución educativa. Permite crear, consultar, editar y eliminar estudiantes desde una interfaz sencilla y responsiva.

---

## 🖥️ Demo

> 🔗 [Ver aplicación en producción](https://trainee115.alwaysdata.net/cliente3/)

---

## ✨ Funcionalidades

- Registrar nuevos estudiantes con nombre, apellido, cédula, edad y curso
- Listar todos los estudiantes en una tabla ordenada por fecha de registro
- Editar la información de un estudiante existente
- Eliminar estudiantes con confirmación previa
- Validaciones en backend: campos obligatorios, edad válida y cédula única
- Diseño responsivo adaptado a móviles y tablets
- Deploy automático al hacer push a la rama principal

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python 3, Flask |
| Base de datos | MySQL |
| Frontend | HTML, CSS, JavaScript vanilla |
| Servidor WSGI | Gunicorn |
| Hosting | AlwaysData |
| CI/CD | GitHub Actions + FTP Deploy |

---

## 📁 Estructura del proyecto

```
registroEstudiantes/
├── .github/
│   └── workflows/
│       └── deployAlways.yml   # Pipeline de despliegue automático
├── static/
│   └── img/
│       └── university.jpg
├── templates/
│   └── index.html             # Interfaz principal
├── app.py                     # Lógica del servidor y rutas Flask
├── wsgi.py                    # Punto de entrada para Gunicorn
├── registro_estudiantes.sql   # Script de creación de la base de datos
└── requirements.txt           # Dependencias de Python
```

---

## ⚙️ Instalación local

### Requisitos previos

- Python 3.8 o superior
- MySQL 8.0 o superior
- pip

### Pasos

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/registroEstudiantes.git
cd registroEstudiantes
```

2. Crear y activar un entorno virtual:

```bash
python -m venv env
source env/bin/activate        # Linux / macOS
env\Scripts\activate           # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Crear la base de datos:

```bash
mysql -u root -p < registro_estudiantes.sql
```

5. Crear el archivo `.env` con las credenciales de la base de datos:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=registro_estudiantes
```

6. Ejecutar la aplicación:

```bash
python app.py
```

7. Abrir en el navegador: `http://localhost:5000`

---

## 🗄️ Esquema de la base de datos

```sql
CREATE TABLE estudiantes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    cedula      VARCHAR(50)  UNIQUE NOT NULL,
    edad        INT          NOT NULL,
    curso       VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 🔌 API Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/estudiantes` | Retorna todos los estudiantes |
| GET | `/estudiantes/<id>` | Retorna un estudiante por ID |
| POST | `/estudiantes` | Crea un nuevo estudiante |
| PUT | `/estudiantes/<id>` | Actualiza un estudiante existente |
| DELETE | `/estudiantes/<id>` | Elimina un estudiante |

### Ejemplo de body para POST / PUT

```json
{
  "nombre": "Juan",
  "apellido": "Pérez",
  "cedula": "1234567890",
  "edad": 20,
  "curso": "Ingeniería de Sistemas"
}
```

---

## 🚀 Despliegue automático

El proyecto usa GitHub Actions para desplegar automáticamente en AlwaysData cada vez que se hace push a `main`. El workflow sincroniza los archivos del repositorio con el servidor vía FTP seguro (FTPS).

```
push a main → GitHub Actions → FTP Deploy → AlwaysData
```

---

## 🔮 Mejoras futuras

### 🔴 Seguridad (prioritario)

- [ ] Mover credenciales FTP del workflow a GitHub Secrets
- [ ] Corregir vulnerabilidad XSS: sanitizar datos antes de insertarlos con `innerHTML`
- [ ] Agregar `.env` al `.gitignore` para evitar subir credenciales accidentalmente

### 🟠 Funcionalidad

- [ ] Agregar sistema de autenticación con roles (Admin, Docente, Estudiante)
- [ ] Agregar botón "Cancelar" al modo edición
- [ ] Validar que la cédula sea numérica y tenga entre 6 y 10 dígitos
- [ ] Implementar paginación en el listado de estudiantes
- [ ] Agregar manejo de errores (`try/except`) al endpoint `GET /estudiantes`
- [ ] Cerrar conexiones a la BD con `try/finally` para evitar conexiones abiertas

### 🟡 Calidad del código

- [ ] Refactorizar `app.py` usando Blueprints de Flask (separar rutas, servicios y modelos)
- [ ] Fijar versiones en `requirements.txt` (generar con `pip freeze`)
- [ ] Agregar `python-dotenv` a `requirements.txt`
- [ ] Eliminar `print()` de debug en producción

### 🟢 Portafolio y escalabilidad

- [ ] Agregar `.env.example` como plantilla de configuración para nuevos desarrolladores
- [ ] Escribir pruebas unitarias para las validaciones del backend
- [ ] Agregar búsqueda y filtros en el frontend

---

## 👤 Autor

Desarrollado por **[Orion Serrano]** — Desarrollador Full Stack  
📍 Cali, Colombia  
🔗 [LinkedIn](https://linkedin.com/in/tu-perfil) · [GitHub](https://github.com/tu-usuario)
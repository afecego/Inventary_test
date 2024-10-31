# Proyecto CRUD de Inventario

Este proyecto es una aplicación web que permite gestionar un inventario de productos perecederos. Está desarrollado con **Python Flask** en el backend y **Vue.js** en el frontend.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)

## Características

- Crear, leer, actualizar y eliminar (CRUD) productos del inventario.
- Conexión a la base de datos MySQL.
- Información sobre el estado de los productos: vigente, por vencer y vencido.

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Frontend**: Vue.js, Axios
- **Base de Datos**: MySQL
- **Gestión de Dependencias**: pip, npm
- **Control de Versiones**: Git

## Instalación

* Configuración del backend

1. Crea entorno virtual y activalo
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux / macOS
    source venv/bin/activate

1. Instala dependencias del backend
    pip install -r requirements.txt

* Configuración del frontend

1. Navega a la carpeta del frontend

    cd frontend

2. Instala dependencias del frontend

    npm install

* Requirements for Python:

```
    blinker==1.8.2
    click==8.1.7
    colorama==0.4.6
    Flask==3.0.3
    Flask-Cors==5.0.0
    Flask-SQLAlchemy==3.1.1
    greenlet==3.1.1
    importlib_metadata==8.5.0
    itsdangerous==2.2.0
    Jinja2==3.1.4
    MarkupSafe==3.0.2
    mysql-connector-python==9.1.0
    mysqlclient==2.2.5
    PyMySQL==1.1.1
    SQLAlchemy==2.0.36
    typing_extensions==4.12.2
    Werkzeug==3.0.6
    zipp==3.20.2
```

* Dependencies for Vue:

```
  "dependencies": {
    "axios": "^1.7.7",
    "vue": "^3.5.12",
    "vue-router": "^4.4.5"
  },
  "devDependencies": {
    "@vue/cli-service": "^5.0.8"
  },
```

### Uso

1. Inicia el servidor backend:

    python run.py

2. Inicia el servidor frontend:

    npm run serve


### Prerequisitos

1. Asegúrate de tener instalado [Python](https://www.python.org/downloads/) (3.x).
2. Instala [Vue.js](https://es.vuejs.org/v2/guide/installation).
3. Ten un servidor MySQL corriendo y una base de datos creada para el proyecto.

### Clonación del Repositorio

```bash
git clone https://github.com/afecego/inventary_test
cd Inventary_test

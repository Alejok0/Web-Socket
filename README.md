# Chat Application con Flask y Socket.IO

## Descripción

Web socket en Node.js con conexión a MySQL y cliente en una página. Esta es una aplicación de chat sencilla que utiliza Flask y Socket.IO en el backend, y una página web estática en el frontend. A continuación, se detallan las instrucciones para configurarla y ejecutarla en un entorno XAMPP.

## Estructura del Proyecto

```
/Web-Socket
│
├───client                # Archivos del cliente
│   └───index.html        # Archivo HTML del cliente
│
└───server                # Código del servidor
    └───main.py           # Código del servidor Flask
```

## Instrucciones de Configuración

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/Alejok0/Web-Socket.git
cd Web-Socket
git checkout distribuido
```

### 2. Configurar el Backend (Flask y Socket.IO)

#### a. Crear la Base de Datos en MariaDB

1. Abre tu cliente de MariaDB (puede ser desde la terminal o usando una herramienta como phpMyAdmin).
2. Ejecuta el siguiente comando para crear la base de datos:

   ```sql
   CREATE DATABASE sockets;
   USE sockets;

   CREATE TABLE messages (
       id INT AUTO_INCREMENT PRIMARY KEY,
       content TEXT,
       user TEXT
   );
   ```

#### b. Instalar Dependencias

Navega al directorio `server`:

```bash
cd server
```

Luego, instala las dependencias necesarias:

```bash
py -m pip install flask
py -m pip install flask-socketio
py -m pip install mysql-connector-python
```

#### c. Modificar el Archivo `main.py`

Asegúrate de que la configuración de conexión a la base de datos sea correcta en `main.py`. Busca la sección que contiene `db_config` y ajusta el `user`, `password` y `host` según sea necesario.

### 3. Configurar el Frontend

Copia el contenido de la carpeta `client` a la carpeta `htdocs` de XAMPP. Por ejemplo:

```bash
C:\xampp\htdocs\Web-Socket\
```

### 4. Iniciar el Servidor Flask

Desde el directorio `server`, ejecuta el servidor:

```bash
python main.py
```

Asegúrate de que el servidor Flask esté corriendo en la IP y puerto especificados (por defecto `http://localhost:2002`).

### 5. Acceder a la Aplicación

Abre tu navegador y accede a la dirección:

```
http://localhost/Web-Socket/index.html
```

## Diagrama de Funcionamiento

```
+-------------------+                                    +-------------------+
|                   |                                    |                   |
|    Cliente (Web)  |                                    |  Servidor Flask   |
|                   |                                    |   (Socket.IO)     |
|                   |        <--------------------->     |                   |
|   Envia Mensaje   |                                    |    Recibe Mensaje |
|                   |                                    |                   |
|                   |                                    |                   |
+-------------------+                                    +-------------------+
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
   +-------------------+                                            |
   |                   |                                            |
   |   Base de Datos   | <--- Almacena Mensaje en Base de Datos --- |
   |     (MariaDB)     | ---> Lee Mensajes de la Base de Datos ---> |
   |                   |                                 
   +-------------------+                                 
```

## Notas Adicionales

- Asegúrate de que el puerto 2002 esté abierto en tu firewall si no puedes conectarte al servidor Flask.
- Si necesitas hacer ajustes en las configuraciones de CORS, revisa la sección correspondiente en `main.py`.

### Personalización

- **Archivos del Cliente**: Si tienes más archivos en la carpeta `client`, puedes listarlos en la estructura.
- **Ruta de Acceso**: Asegúrate de que la ruta de acceso sea correcta según tu configuración.


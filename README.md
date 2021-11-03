# Looking4Gamers

_Una primera fase de este proyecto es crear una aplicación/red social que permita conectar a usuarios y formar grupos para jugar a un videojuego. Para ello se requiere el registro del usuario._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

_Lo primero debes clonar el proyecto:_

```
git clone https://github.com/Jarauta1/looking4gamers.git
```

_Crear e iniciar un entorno virtual:_

```
virtualenv env --no-site-packages

source env/bin/activate
```

### Instalación 🔧

_Debes instalar las siguientes dependencias:_

```
- Django
- Django Rest Framework
- Psycopg2 2.8.6
- Django Rest Auth
- Django All Auth
```

_Esto lo consigues ejecutando en el terminal lo siguiente:_

```
$ pip install django
$ pip install djangorestframework
$ pip install psycogp2
$ pip install django-rest-auth
$ pip install django-allauth

```

## Modificar los datos de la BBDD en settings.py 🔩

```
DATABASES = {
    'default': {
        'ENGINE': 'Django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '****',
        'Host': 'localhost',
        'PORT': '5432',
    }
}

```

_Después de modificar estos parámetros deberás ejecutar en tu terminal:_

```
$ python manage.py migrate
```

## Crear usuario administrador de Django 🤓

_Esta aplicación web de Django necesita crear un usuario administrador de Django, para acceder y administrar la interfaz de administrador, ejecute el siguiente comando:_

```
$ python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: your-user@mail.com
Password: 
Password (again): 
Superuser created successfully.
```

_A continuación ejecuta en tu terminal lo siguiente:_

```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Ejecutar la aplicación web Django ⌨️

_Necesita ejecutar el servidor de Django, ejecute el siguiente comando:_

```
$ python manage.py runserver
```

_Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) y vea la aplicación web Django._

_Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) y vea la interfaz de administración de Django, use el usuario admin y contraseña admin._


## Construido con 🛠️

```
- PostgreSQL (psycopg2 2.9.1)
- Python 3.6
- Django 3.2.8
- Django Rest Framework 3.12.4
```

## Autor ✒️

* **Diego Jarauta** - *Desarrollador Full Stack* - [DJarauta](https://github.com/Jarauta1)

## Rutas de esta API ⚙️

_Este es el listado de rutas:_

`/admin` Dentro de esta ruta está accesible el dashboard que viene por defecto con Django donde se puede gestionar toda la información.

`/` Ruta principal.

_Las rutas para acceder a cada apartado son:_

`/servers` : GET, POST, PATCH, DELETE
`/users` : GET, POST, PATCH, DELETE
`/groups` : GET, POST, PATCH, DELETE
`/messages` : GET, POST, PATCH, DELETE
`/channels` : GET, POST, PATCH, DELETE

_En los grupos se puede realizar búsqueda por nombre de grupo:_

`/groups?search=nombreabuscar`

_Y en los canales por topic:_

`/channels?search=topicabuscar`


`/api-auth` Bajo esta ruta están todas aquellas relacionadas con la sesión del usuario:

```
    `/login` : Iniciar una sesión
    `/logout` : Cerrar sesión
    `/user` : Recibir la información del usuario activo 
    `/registration` : Registrar un nuevo usuario
    `/password/reset/` : Resetear la contraseña
    `/password/reset/confirm/` : Confirmar el reseteo de la contraseña
    `/password/change/` : Cambiar la contraseña
```

## Modelos / Models

_Los modelos que se han utilizado para realizar esta API:_


```
- Server
- Users
- Groups
- Message
- Channels
```

### Server

_Este modelo incluye los siguientes campos:_

```
- server_id: Identificador del servidor
- server_name: Nombre del servidor
- members: JSON con todos los usuarios del servidor
- groups: JSON con todos los grupos creados en el servidor
```

### Users

_Este modelo incluye los siguientes campos:_

```
- user_id: Identificador del usuario
- password: Contraseña
- email: Email del usuario
- avatar: URL del avatar del usuario
- discord_user: Nombre del usuario en Discord
- epicgames_user: Nombre del usuario en EpicGames
- steam_user: Nombre del usuario en Steam
- groups: JSON con todos los grupos a los que pertenece el usuario
- msg: JSON con todos los mensajes escritos por el usuario
```

### Group

_Este modelo incluye los siguientes campos:_

```
- group_id: Identificador del grupo
- server_id: Identificador del servidor al que pertenece
- user_id: Identificador del usuario que creo el grupo
- icon: URL del icono del grupo
- group_name: Nombre del grupo (se puede realizar búsquedas)
- members: JSON con todos los usuarios que pertenecen al grupo
- channels: JSON con todos los canales que posee el grupo
```
### Channel

_Este modelo incluye los siguientes campos:_

```
- msg_id: Identificador del mensaje
- channel_id: Identificador del canal donde ha sido escrito el mensaje
- user_id: Identificador del usuario que ha escrito el mensaje
- msg: Mensaje escrito
- date: Fecha en la que se escribe el mensaje
- edited_date: Fecha en la que se edita el mensaje
```

---
⌨️ con ❤️ por [DJarauta](https://github.com/Jarauta1) 😊
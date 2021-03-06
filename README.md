# Looking4Gamers

_Una primera fase de este proyecto es crear una aplicaci贸n/red social que permita conectar a usuarios y formar grupos para jugar a un videojuego. Para ello se requiere el registro del usuario._

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

_Lo primero debes clonar el proyecto:_

```
git clone https://github.com/Jarauta1/looking4gamers.git
```

_Crear e iniciar un entorno virtual:_

```
virtualenv env --no-site-packages

source env/bin/activate
```

### Instalaci贸n 馃敡

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

## Modificar los datos de la BBDD en settings.py 馃敥

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

_Despu茅s de modificar estos par谩metros deber谩s ejecutar en tu terminal:_

```
$ python manage.py migrate
```

## Crear usuario administrador de Django 馃

_Esta aplicaci贸n web de Django necesita crear un usuario administrador de Django, para acceder y administrar la interfaz de administrador, ejecute el siguiente comando:_

```
$ python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: your-user@mail.com
Password: 
Password (again): 
Superuser created successfully.
```

_A continuaci贸n ejecuta en tu terminal lo siguiente:_

```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Ejecutar la aplicaci贸n web Django 鈱笍

_Necesita ejecutar el servidor de Django, ejecute el siguiente comando:_

```
$ python manage.py runserver
```

_Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) y vea la aplicaci贸n web Django._

_Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) y vea la interfaz de administraci贸n de Django, use el usuario admin y contrase帽a admin._


## Construido con 馃洜锔?

```
- PostgreSQL (psycopg2 2.9.1)
- Python 3.6
- Django 3.2.8
- Django Rest Framework 3.12.4
```

## Autor 鉁掞笍

* **Diego Jarauta** - *Desarrollador Full Stack* - [DJarauta](https://github.com/Jarauta1)

## Rutas de esta API 鈿欙笍

_Este es el listado de rutas:_

`/admin` Dentro de esta ruta est谩 accesible el dashboard que viene por defecto con Django donde se puede gestionar toda la informaci贸n.

`/` Ruta principal.

_Las rutas para acceder a cada apartado son:_

- `/servers` : GET, POST, PATCH, DELETE
- `/users` : GET, POST, PATCH, DELETE
- `/groups` : GET, POST, PATCH, DELETE
- `/messages` : GET, POST, PATCH, DELETE
- `/channels` : GET, POST, PATCH, DELETE

_En los grupos se puede realizar b煤squeda por nombre de grupo:_

`/groups?search=nombreabuscar`

_Y en los canales por topic:_

`/channels?search=topicabuscar`


`/api-auth` Bajo esta ruta est谩n todas aquellas relacionadas con la sesi贸n del usuario:

- `/login` : Iniciar una sesi贸n
- `/logout` : Cerrar sesi贸n

_Ejemplo de ruta:_

`/api-auth/login`

`/auth` Bajo esta ruta est谩n:

- `/user` : Recibir la informaci贸n del usuario activo 
- `/registration` : Registrar un nuevo usuario
- `/password/reset/` : Resetear la contrase帽a
- `/password/reset/confirm/` : Confirmar el reseteo de la contrase帽a
- `/password/change/` : Cambiar la contrase帽a

_Ejemplo de ruta:_

`/auth/registration`


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
- password: Contrase帽a
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
- group_name: Nombre del grupo (se puede realizar b煤squedas)
- members: JSON con todos los usuarios que pertenecen al grupo
- channels: JSON con todos los canales que posee el grupo
```

### Channel

_Este modelo incluye los siguientes campos:_

```
- channel_id: Identificador del canal
- group_id: Identificador del grupo donde ha sido creado el canal
- channel_name: Nombre del canal
- topic: Topic del canal (se puede realizar b煤squedas)
- wall: JSON donde almacenar todos los mensajes para mostrarlos (muro)
```

### Message

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
鈱笍 con 鉂わ笍 por [DJarauta](https://github.com/Jarauta1) 馃槉
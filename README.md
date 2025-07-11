Instituto Técnico Superior Córdoba
Tecnicatura Superior en Desarrollo de Software
Práctica Profesionalizante I
Práctico 2:
CRUD básico con autenticación.
Consigna:
Implementar en Django un CRUD que almacene registros de tipo “Persona” y “Oficina”.
Campos de “Oficina”:
● nombre
● nombre_corto
Campos de “Persona”:
● apellido
● nombre
● edad
● oficina (foreign key del modelo “Oficina”)
Cada uno de estos modelos deben implementarse en aplicaciones por aparte. Cada
aplicación debe tener su propio archivo urls.py.
La autenticación deberá implementarse con una aplicación llamada “accounts”. La misma
debe manejar el registro de usuarios, como asi también el login y el logout. Obviamente, con
un urls.py propio. También, el registro de usuarios deberá contar con un captcha simple
(investigar django-simple-captcha)
La interfaz deberá contar con una barra de navegación superior (usar bootstrap), en la cual
haya:
● Link hacia la lista de personas
● Link hacia la lista de oficinas
● Barra de búsqueda (de personas por nombre)
● Boton de “Ingresar” si el usuario no está logueado, y de “Salir” si el usuario está
logueado
Deberá contar con un mecanismo de carga masiva (De oficinas y de personas).
Vistas para “Oficina”:
● Lista completa (con paginación)
● Detalle de oficina (debe incluir la lista de personas que la componen)
● Alta de oficina
● Modificación de oficina
● Eliminación de oficina
● Búsqueda (con paginación)
Vistas para “Persona”:
● Lista completa (con paginación)
● Detalle
● Alta de persona
● Modificacion de persona
● Eliminación de persona
● Búsqueda (implementada en conjunto con la barra de busqueda)
Los templates encargados de mostrar listados (de ambos modelos), deberán hacerlo
siguiendo este estilo (a modo de ejemplo):
Fulano de tal —-- Ver - Modificar - Eliminar
Los enlaces de Ver - Modificar - Eliminar deben aparecer como botones (bootstrap) de
distintos colores.
La aplicación debe ser responsiva (Investigar “Boostrap grid layout”).
La creación, modificación y eliminación de registros deben ser con login obligatorio.
Se deberá subir un informe a google drive, el cual debe tener permisos de sugerencias. En
dicho informe, incluir enlace al repositorio en github (mínimo 10 commits). Redactar el
proceso de instalación de entorno virtual, django, inicialización del proyecto y creación de
las aplicaciones.
El trabajo es INDIVIDUAL.
SUERTE!!!!

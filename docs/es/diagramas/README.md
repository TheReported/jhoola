# Análisis y Diseño de la Aplicación

En este documento analizaremos y diseñaremos nuestra aplicación utilizando los diferentes diagramas y especificaciones que conocemos.

## Especificación del diagrama E/R de la BBDD

En esta sección se presentará una imagen del diagrama E/R de la BD.

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/jhoola-er.png">

## Especificación del diagrama MR de la BBDD

En este apartado se mostrará una imagen del diagrama MR de la BBDD.

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/jhoola-mr.png">

## Especificación de los CU

En este apartado se mostrará una imagen del diagrama y la especificación de los casos de uso.

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/usecase_diagram_jhoola.png">

Se puede ver como el usuario debe autenticarse para poder acceder a la posibilidad de hacer reservas en las cuales tendrá que pasar por una pasarela de pago para en un final acceder a la posibilidad de borrar reservas, descargarse un PDF con los datos de la misma y consultarla. Por otro lado el administrador tendrá que pasar por un proceso de autenticación muy similiar para lograr gestionar usuarios, productos y reservas.

### Especificación de los actores

En este documento se especifican los actores que intervienen en la solución propuesta.

#### Usuario

| Actor | Usuario |
|---|---|
| Descripción | El usuario puede reservar hamacas en el hotel iniciando sesión. |
| Características | Debe pasar por autenticación para realizar las acciones. |
| Relaciones | _Sin relaciones con otros actores_ |
| Referencias |  |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Administrador 

| Actor | Administrador |
|---|---|
| Descripción | El administrador puede gestionar productos, reservas y usuarios. |
| Características | Debe pasar por autenticación para realizar las acciones. |
| Relaciones | _Sin relaciones con otros actores_ |
| Referencias |  |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Banco

| Actor | Banco |
|---|---|
| Descripción | El banco comprueba si el pago puede realizarse o no. |
| Características |  |
| Relaciones | _Sin relaciones con otros actores_ |
| Referencias | | 
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

### Especificación de casos de uso

Este documento especifica los casos de uso que forman parte de la solución propuesta.

#### Autenticarse

| Caso de uso CU.1 | Autenticarse |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | El usuario debe autenticarse antes de realizar cualquier acción. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Reservar

| Caso de uso CU.2 | Reservar |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | El usuario puede reservar hamacas. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | Pagar la reserva. |  
| Requisitos | Estar autenticado. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Pago

| Caso de uso CU.3 | Pago |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | El usuario debe pagar a la hora de realizar la reserva. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | |  
| Requisitos | Estar autenticado y haber hecho la reserva. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Comprobar

| Caso de uso CU.4 | Comprobar |
|---|---|
| Fuentes | |
| Actor | Banco |
| Descripción | El banco comprueba si el pago se puede realizar. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | |  
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Aceptado

| Caso de uso CU.5 | Aceptado |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | El pago ha sido aceptado. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | |   
| Requisitos | Que se haya realizado un pago. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Cancelar Reserva

| Caso de uso CU.6 | Cancelar Reserva |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | Cancelar reserva en caso de error. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | |   
| Requisitos | Que se haya aceptado un pago. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Denegado

| Caso de uso CU.7 | Denegado |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | El  pago ha sido rechazado. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | | 
| Requisitos | Que se haya realizado un pago. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Borrar

| Caso de uso CU.8 | Borrar |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | La reserva se borra. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | | 
| Requisitos | Que se haya realizado una reserva. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _07/05/2024_ |

#### Consultar

| Caso de uso CU.9 | Consultar |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | Se consulta la reserva. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | | 
| Requisitos | Que se haya realizado una reserva. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _07/05/2024_ |

#### Descargar PDF

| Caso de uso CU.10 | Descargar PDF |
|---|---|
| Fuentes | |
| Actor | Usuario |
| Descripción | Se descarga un PDF con los datos de la reserva. |
| Flujo básico | |
| Pre-condiciones | |   
| Post-condiciones | | 
| Requisitos | Que se haya realizado una reserva. |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _07/05/2024_ |

#### Autenticarse

| Caso de uso CU.11 | Autenticarse |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador debe autenticarse antes de realizar cualquier acción. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Gestionar Usuario

| Caso de uso CU.12 | Gestionar Usuario |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede gestionar los usuarios de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Crear

| Caso de uso CU.13 | Crear |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede crear usuarios en la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Consultar

| Caso de uso CU.14 | Consultar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede consultar los usuarios de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Modificar

| Caso de uso CU.15 | Modificar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede modificar los usuarios de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Borrar

| Caso de uso CU.16 | Borrar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede borrar los usuarios de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Gestionar Reserva

| Use Case CU.17 | Gestionar Reserva |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede gestionar las reservas de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Consultar

| Caso de uso CU.18 | Consultar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede consultar las reservas hechas en la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Borrar

| Caso de uso CU.19 | Borrar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede borrar las reservas de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Gestionar Producto

| Use Case CU.20 | Gestionar Producto |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede gestionar los productos de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Crear

| Caso de uso CU.21 | Crear |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede crear productos en la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Consultar

| Caso de uso CU.22 | Consultar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede consultar los productos que hay en la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Modificar

| Caso de uso CU.23 | Modificar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede modificar los productos que hay en la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

#### Borrar

| Caso de uso CU.24 | Borrar |
|---|---|
| Fuentes | |
| Actor | Administrador |
| Descripción | El administrador puede borrar los productos de la aplicación. |
| Flujo básico | |
| Pre-condiciones | | 
| Post-condiciones | |
| Requisitos | |
| Notas | |
| Autor |  _Abián Castañeda Méndez_ |
| Fecha | _08/03/2024_ |

## Especificación del diagrama de clases

En esta sección se presentará una imagen del diagrama de clases y una breve explicación del mismo.

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/class_diagram_jhoola.png">

En este esquema un hotel tiene un gran número de productos y usuarios y al mismo tiempo tienen la posibilidad de hacer desde ninguna hasta muchas reservas. Por otro lado, el administrador, que dispone de las mismas herramientas que el usuario, tiene poderes superiores que le permiten gestionar las diferentes áreas.

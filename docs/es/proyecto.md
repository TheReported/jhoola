<center>

# Dpto. INFORMÁTICA - I.E.S. PUERTO DE LA CRUZ – TELESFORO BRAVO 
***
### MÓDULO PROYECTO (PRW)
### C.F.G.S. Desarrollo de Aplicaciones Web (DAW) 

TÍTULO DEL PROYECTO 

</center>

<right>


***Autor/es:*** Abián Gustavo Castañeda Méndez, Diego Peraza Cabo, Samuel Eloy González Díaz

***Fecha:*** 10 de Mayo de 2024

***Tutor:*** Alejandro Martín Zarza



</right>

<center>

# INDICE 

</center>

1. [***INTRODUCCIÓN.***](#id1)
2. [***ORIGEN, CONTEXTUALIZACIÓN Y JUSTIFICACIÓN DEL PROYECTO.***](#id2)
3. [***OBJETIVO GENERAL DEL PROYECTO.***](#id3)
4. [***DESCRIPCIÓN GENERAL DEL PROYECTO (ALCANCE).***](#id4)
5. [***TAREAS.***](#id5)
6. [***CRONOGRAMA.***](#id6)
7. [***RESUMEN DE RECURSOS HUMANOS Y MATERIALES.***](#id7)
8. [***CONTROL DE RIESGOS.***](#id8)
9. [***POLÍTICA DE SEGUIMIENTO, EVALUACIÓN Y CONTROL DE CALIDAD.***](#id9)
10. [***CLAUSULAS.***](#id10)
11. [***BIBLIOGRAFÍA.***](#id11)
12. [***GLOSARIO.***](#id12)
13. [***ANEXOS.***](#id13)

### 1. INTRODUCCIÓN. <a name="id1"></a>

Este documento tiene como objetivo principal establecer las bases y el camino ha seguir para el desarrollo de un proyecto destinado a la gestión de reservas de hamacas en hoteles. En él se detallarán los objetivos, alcance, requisitos y recursos necesarios para llevar a cabo el mismo de manera exitosa.

### 2. ORIGEN, CONTEXTUALIZACIÓN Y JUSTIFICACIÓN DEL PROYECTO. <a name="id2"></a>

#### Origen de la idea

La idea de desarrollar un sistema de gestión de reservas de hamacas en hoteles surge como respuesta a una situación vivida por muchos individuos. En muchas ocasiones se ha vivido la mala experiencia de tener que lidiar con personas que se levantan desde muy temprano para tomar las hamacas o que dejan sus pertenencias desde la noche provocando una mala gestión y peleas de las cuales los hoteles no se hacen responsables. Además, con la digitalización en aumento en la industria hotelera, se busca aprovechar la tecnología para mejorar la calidad del servicio ofrecido.

#### Necesidades detectadas

A raiz de la información mencionada en el anterior punto, se han identificado diversas necesidades que no están siendo completamente satisfechas. Entre estas necesidades se destacan:

**Complejidad en la reserva:** Los clientes a menudo encuentran complicado y poco intuitivo el proceso de reserva de hamacas, lo que puede resultar en una experiencia frustrante.

**Falta de control y seguimiento:** Los administradores de los hoteles carecen de herramientas adecuadas para gestionar y supervisar las reservas de hamacas de manera efectiva, lo que puede llevar a una distribución desigual de los espacios disponibles.

**Oportunidades de mejora en la experiencia del cliente:** Existe un potencial para mejorar la experiencia del cliente ofreciendo un proceso de reserva más ágil y personalizado, así como una mayor transparencia en la disponibilidad de hamacas.

#### Problemas a resolver

Los problemas principales que se intentan abordar con este proyecto es la falta de un sistema integral de gestión de reservas de hamacas que satisfaga las necesidades tanto de los clientes como de los administradores de hoteles. Este problema puede resultar en una experiencia insatisfactoria para los clientes, una distribución ineficiente de los espacios y una pérdida de oportunidades de ingresos para el hotel.

#### Justificación del proyecto

La justificación de este proyecto radica en la importancia de mejorar la experiencia del cliente, optimizar los recursos del hotel y aumentar su competitividad en el mercado turístico a lo que también se suma generar más puestos de trabajo y favorecer la economía de los territorios dando la posibilidad de generar más riqueza a los hoteles con el sistema de reservas.

En resumen, este proyecto busca resolver una necesidad identificada en el mercado hotelero mediante la implementación de una solución tecnológica que beneficie tanto a los clientes como a los administradores de hoteles.

### 3. OBJETIVO GENERAL DEL PROYECTO. <a name="id3"></a>

El objetivo general de este proyecto es desarrollar una aplicación web utilizando el framework Django, que permita la gestión eficiente de reservas de hamacas en hoteles. Esta aplicación proporcionará a los clientes una plataforma intuitiva para realizar reservas de hamacas de manera rápida y sencilla usando un sistema de pagos seguro, mientras que a los administradores les brindará herramientas para supervisar y gestionar estas reservas de manera efectiva.

### 4. DESCRIPCIÓN GENERAL DEL PROYECTO (ALCANCE). <a name="id4"></a>


El proyecto consiste en desarrollar una aplicación web para gestionar reservas de hospedaje de manera eficiente y accesible. La aplicación estará diseñada para ofrecer una experiencia fluida tanto para los usuarios que realicen reservas como para los administradores que gestionen el sistema. A continuación, se detalla la descripción general del proyecto:

#### Funcionamiento general de la aplicación

Tanto los usuarios como los administradores podrán acceder a la aplicación a través de un navegador web desde cualquier dispositivo con conexión a internet. Podrán buscar el hotel en el que se están quedando para después pasar a una ventana en la que tendrán que iniciar sesión con los datos que se les proporcionará. 

En el caso de los clientes, cuando hayan accedido a su zona podrán realizar reservas elegiendo el producto a reservar y las características que vengan con este y gestionar sus reservas existentes.

Los administradores tendrán acceso a un panel de administración donde podrán gestionar las reservas, gestionar los productos que se puedan reservar y gestionar la creación de usuarios.

#### Divisiones de la aplicación

La aplicación estará dividida en dos partes principales: el frontend y el backend.

- El frontend será ese conjunto de diseños que se realizarán para que la experiencia del administrador y el cliente sean del diez.

- El backend será responsable de procesar las solicitudes del cliente, interactuar con la base de datos y realizar la lógica de negocio. Además, se aplicará una capa intermedia para la autenticación y la gestión de sesiones de usuario.

#### Arquitectura y estructura

- Para el backend, se empleará el framework web Django, conocido por su robustez, escalabilidad y seguridad. Django proporciona una estructura que facilita el desarrollo y la organización del código.

- Para el frontend se utilizará HTML, CSS y JavaScript para la parte estática de la interfaz de usuario. Además, se integrará Bootstrap 5 para garantizar un diseño responsivo y atractivo.

- La autenticación de usuarios se realizará utilizando mecanismos proporcionados por Django, como el sistema de autenticación integrado o mediante bibliotecas externas como Django REST Framework para la autenticación basada en tokens.

- La validación de datos se llevará a cabo tanto en el frontend como en el backend para garantizar la integridad de la información.

#### Tecnologías a utilizar:

- Backend: Django, Django REST Framework, Python.

- Frontend: HTML, CSS, JavaScript, Bootstrap 5.

- Base de datos: Posiblemente se utilizará SQLite para desarrollo y pruebas, y se migrará a una base de datos más robusta como PostgreSQL para producción.

- Despliegue: Se contempla el uso de una VPS en Azure para el despliegue del proyecto, con la posibilidad de implementar contenedores Docker para facilitar la gestión y escalabilidad.

En resumen, el proyecto se estructurará utilizando tecnologías modernas y robustas para ofrecer una aplicación web eficiente y segura para la gestión de reservas de hospedaje.

### 5. TAREAS. <a name="id5"></a>

Para cada tarea:
+ **Título**
+ **Descripción y metodología.** 
>En este apartado se define tanto el objetivo que persigue la ejecución de esta tarea así como una definición de la misma, es decir, en qué consiste la tarea, qué se va a hacer durante el desarrollo de la misma, etc.
+ **Duración (en horas).** 
+ **Fecha de inicio y fecha de fin**
+ **Recursos humanos**
+ **Recursos materiales**
+ **Coste**
+ **Responsable**

>Consejo: NO programen tareas hasta el último minuto, ¡establezcan contingencias!! 	La mayoría de tareas se dividirán en subtareas, que deberán indicarse (pero en este caso no detallar). Bastará con algo como lo siguiente :

<center>

| Tarea     | Título                  | Depend  | Duración | Fecha Ini | Fecha Fin |
|-----------|-------------------------|---------|----------|-----------|-----------|
| Tarea 5   | Front-end               |         | 20h      | 25/3/19   | 27/3/19   |
| Tarea 5.1 | Conectar a la API       | 2, 3, 4 | 3 h      | 25/3/19   | 25/3/19   |
| Tarea 5.2 | Listar un elemento      | 5.1     | 1 h      | 25/3/19   | 25/3/19   |
| Tarea 5.3 | Crear un nuevo elemento | 5.1     | 4 h      | 26/3/19   | 26/3/19   |
| ...       | ...                     | ...     | ...      | ...       | ...       |

</center>

A partir de esta información, RELLENAR LAS TAREAS EN EL TEAM-GANTT (o similar)

### 6. CRONOGRAMA. <a name="id6"></a>

Este apartado nos servirá como resumen de alcance, temporalización y coste. Utilizar la información anterior de las tareas, para establecer un resumen de los principales aspectos del proyecto (debería bastar con las tareas principales, y evitar un excesivo detalle de las subtareas). Se puede reflejar con un diagrama de Gantt que podemos sacar de los **PROJECTS** de **GitHub** ( adjuntamos capturas de pantalla )

### 7. RESUMEN DE RECURSOS HUMANOS Y MATERIALES. <a name="id7"></a>

Como en el caso anterior, hacer una tabla para cada tarea principal

<center>

| TAREA                | Recursos Humanos                                   | Recursos materiales                           |
|----------------------|----------------------------------------------------|-----------------------------------------------|
| 1. Instalar software | Técnico de sistemas: 2 Técnico de base de datos: 3 | Servidor de pruebas Licencia de base de datos |
| ...                  | ...                                                | ...                                           |

</center>

### 8. CONTROL DE RIESGOS. <a name="id8"></a>

#### 8.1 Riesgo de cambios menores en los requisitos del cliente

**Probabilidad:** Baja (0.10)

**Impacto:** Bajo (0.20) → Suelen ser cambios menores que no afectan significativamente el alcance o el tiempo del proyecto.

**Tipo de riesgo:** Bajo

**Acción a llevar a cabo:** Dividir dichos cambios con calma entre los distintos trabajadores involucrados en el proyecto. El equipo puede manejar estos cambios fácilmente sin necesidad de intervención adicional. Se pueden implementar prácticas ágiles para adaptarse a los cambios de manera eficiente y garantizar la satisfacción del cliente.


#### 8.2 Riesgo de fallos en la infraestructura de despliegue

**Probabilidad:** Muy Bajo (0.10)

**Impacto:** Medio (0.40) → Podría causar interrupciones en el servicio y afectar la disponibilidad de la aplicación.

**Tipo de riesgo:** Medio

**Acción a llevar a cabo:** Plan de mitigación → Realizar distintas pruebas exhaustivas de la infraestructura de despliegue y configurar sistemas para detectar posibles problemas. A su vez hay que establecer un protocolo de respuesta rápida para abordar cualquier fallo y minimizar el tiempo de inactividad.

#### 8.3 Riesgo de falta de experiencia con tecnologías seleccionadas

**Probabilidad:** Alto (0.60)

**Impacto:** Medio (0.50) → Podría generar retrasos en el desarrollo y requerir tiempo adicional para aprender y adaptarse a las nuevas tecnologías.

**Tipo de riesgo:** Alto

Acción a llevar a cabo: Plan de mitigación → Cambiar el modelo de trabajo aplicado en el proyecto para lanzarlo con las tecnologías que se controlan en el equipo o directamente pasar a un proceso de aprendizaje agil con el que poder lograr sacar hacia adelante el proyecto.
  
### 9. POLÍTICA DE SEGUIMIENTO, EVALUACIÓN Y CONTROL DE CALIDAD. <a name="id9"></a>


Para asegurar que el proyecto se mantenga en curso y cumpla con los objetivos planteados, se implementarán diversas acciones de seguimiento, evaluación y control de calidad. Aquí algunas de las acciones a llevar a cabo:

#### 9.1 Reuniones regulares de seguimiento

Se realizarán reuniones periódicas con el equipo del proyecto para revisar el progreso, discutir cualquier cambio o problema y tomar medidas si es necesario.

#### 9.2 Seguimiento de hitos

Se establecerán hitos en el cronograma del proyecto. Se realizará un seguimiento constante para asegurar que se cumplan en los plazos establecidos.

#### 9.3 Revisiones de código y Testing

Se llevarán a cabo revisiones regulares del código para garantizar su calidad y coherencia. Además, se realizarán pruebas para asegurar que los diferentes componentes del sistema funcionen correctamente juntos.

#### 9.4 Encuestas de satisfacción del cliente y Beta-Testing

Se enviarán encuestas a los clientes para evaluar su satisfacción con el proyecto y recopilar comentarios que ayuden a identificar áreas de mejora y a su vez se les dejará probar la aplicación con el fin de que aquellos menos enterados en dicho ambito nos ayuden a encontrar errores.

#### 9.5 Retroalimentación del equipo

Se fomentará un ambiente sano dentro del equipo, donde los miembros puedan compartir sus ideas, preocupaciones y sugerencias para mejorar el proceso y el producto final.
Implementando estas acciones de seguimiento, evaluación y control de calidad, el equipo podrá estar en sintonía con el progreso del proyecto, identificar y abordar casos inesperados de manera oportuna y asegurar la entrega de un producto de alta calidad que cumpla con los requisitos y expectativas del cliente.

### 10.  CLAUSULAS. <a name="id10"></a>

#### 10.1 Entrega y plazos

- La entrega de la aplicación web a la empresa se realizará en la fecha acordada entre las partes, especificada en el contrato inicial.

- En caso de algún tipo de retraso en la entrega por parte de nuestro equipo, se aplicarán penalizaciones financieras.

- Los plazos para cada funcionalidad del proyecto se detallarán en el cronograma y podrán ser modificados post-contrato solo con el consentimiento mutuo de equipo y cliente.

#### 10.2 Pagos

- El pago se realizará de acuerdo con el cronograma establecido en el contrato, detallando la cantidad mensual y la fecha de cuando se debe realizar.

- El cliente se compromete a efectuar los pagos según lo acordado, y el equipo entregará el proyecto y el soporte **si se adquiere** según lo establecido.

- En caso de incumplimiento en los pagos por parte del cliente, el equipo se reserva el derecho de suspender sus labores hasta que se solucione la situación.

#### 10.3 Propiedad intelectual

- Todos los derechos de propiedad intelectual del software desarrollado, incluidos el código fuente, la documentación y cualquier material asociado, serán propiedad exclusiva de Jhoola.

#### 10.4 Soporte

- Se ofrecerá soporte al cliente si este adquiere la suscripción en la que se incluye dicho servicio

#### 10.5 Confidencialidad

- Ambas partes se comprometen a mantener la confidencialidad de toda la información que se proporcione durante el proyecto, incluidos los datos del cliente, los detalles del proyecto y cualquier otra información que sea sensible.

- El punto anteriormente mencionado eguirá en vigor incluso después de la aplicación del proyecto o la terminación del contrato.

#### 10.6 Calidad y control de cambios

- El equipo de desarrollo se compromete a cumplir con los estándares de calidad acordados y a realizar pruebas exhaustivas para garantizar el funcionamiento adecuado de la aplicación web.

- Los cambios o mejoras que se quieran implementar requerirán la aprobación por escrito del cliente, y podrán implicar ajustes en el cronograma y el aumento del coste de la aplicación.

#### 10.7 Resolución de conflictos

- Si surge un problema entre equipo y cliente ambas partes intentarán resolverlos de manera amistosa y mediante negociaciones directas.

#### 10.8 Cancelación del servicio

- En caso de que el cliente desee cancelar su servicio, solo tendrá que hacerlo previo al pago del siguiente mes. Si el pago ya ha sido realizado no nos comprometemos a devolver el dinero.


### 11.  BIBLIOGRAFÍA. <a name="id11"></a>
    
### 12.  GLOSARIO. <a name="id12"></a>

### 13.  ANEXOS. <a name="id13"></a>

Aquí se puede indicar: 
+ Documentación externa de utilidad
+ Modelos de datos
+ Diagramas y esquemas
+ Diagrama de Entidad-Relación o similar.
+ Tabla de roles de los usuarios
+ etc.

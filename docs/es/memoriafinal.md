<center>

# MEMORIA FINAL
***

</center>

<right>

***Autor/es:*** Abián Gustavo Castañeda Méndez, Diego Peraza Cabo, Samuel Eloy González Díaz
<br>
***Fecha:*** 10 de Mayo de 2024
<br>
***Tutor:*** Alejandro Martín Zarza

</right>

<center>

# INDICE 

</center>

1. [***INTRODUCCIÓN.***](#id1)
2. [***TECNOLOGÍAS UTILIZADAS.***](#id2)
3. [***GUIA DE ESTILO DE LA WEB.***](#id3)
4. [***INVESTIGACIÓN.***](#id4)
5. [***DERECHOS DE AUTOR.***](#id5)
6. [***RIESGOS Y MEDIDAS.***](#id6)
7. [***GRADO DE CUMPLIMIENTO EN ALCANCE.***](#id7)
8. [***GRADO DE CUMPLIMIENTO EN TIEMPO.***](#id8)
9. [***GRADO DE CUMPLIMIENTO EN COSTE.***](#id9)
10. [***PRODUCTO FINAL.***](#id10)
11. [***EXPEIRNECIAS APRENDIDAS A TENER EN CUENTA EN PRÓXIMOS PROYECTOS.***](#id11)
12. [***CONCLUSIONES, COMENTARIOS Y VALORACIÓN FINAL.***](#id12)


### 1. INTRODUCCIÓN. <a name="id1"></a>

El presente documento constituye la memoria final del proyecto de desarrollo de una aplicación de reserva de hamacas para clientes y un sistema de gestión para el administrador. El propósito principal de esta memoria es documentar de manera exhaustiva el proceso de planificación, diseño, implementación y evaluación del sistema, así como resaltar los logros alcanzados y las lecciones aprendidas a lo largo del proyecto.

### 2. TECNOLOGÍAS UTILIZADAS. <a name="id2"></a>

Las tecnologías usadas en el proyecto han sido las siguientes:

**Django==4.2:** Django es un framework web de alto nivel escrito en Python que permite el desarrollo rápido de aplicaciones web seguras y mantenibles. Proporciona un conjunto de componentes y patrones de diseño que facilitan la creación de aplicaciones web complejas.

**prettyconf==2.2.1:** PrettyConf es una biblioteca de Python que facilita la gestión de la configuración de una aplicación mediante el uso de archivos de configuración simples y legibles. Permite definir variables de entorno y valores predeterminados de manera clara y ordenada.

**djangorestframework==3.15.1:** Django REST Framework es una biblioteca de Django que facilita la creación de APIs web utilizando el estilo de arquitectura REST. Proporciona herramientas para la serialización de datos, la autenticación de usuarios, la gestión de permisos y la creación de vistas basadas en clases.

**pillow==10.3.0:** Pillow es una biblioteca de procesamiento de imágenes en Python que se utiliza comúnmente para manipular imágenes en aplicaciones web. Proporciona herramientas para abrir, manipular y guardar imágenes en una variedad de formatos.

**WeasyPrint==61.2:** WeasyPrint es una biblioteca de Python que permite generar documentos PDF a partir de contenido HTML y CSS. Es útil para generar informes o facturas en aplicaciones web.

**django-cors-headers==4.3.1:** Django CORS Headers es una biblioteca de Django que facilita la configuración de encabezados CORS (Cross-Origin Resource Sharing) en una aplicación web. Permite que el servidor indique a los navegadores web si se permite o no que una página web acceda a recursos de otro origen.

**stripe==9.1.0:** Stripe es una plataforma de pagos en línea que facilita la aceptación de pagos en aplicaciones web y móviles. La biblioteca Stripe proporciona herramientas para integrar la funcionalidad de pago de Stripe en una aplicación Django.

**django-debug-toolbar==4.3.0:** Django Debug Toolbar es una herramienta de depuración para aplicaciones Django que muestra información útil para desarrolladores mientras están depurando una aplicación. Proporciona paneles interactivos que muestran información sobre consultas de base de datos, solicitudes HTTP y rendimiento.

**gunicorn==22.0.0:** Gunicorn es un servidor HTTP de Python que se utiliza comúnmente para implementar aplicaciones web Django en producción. Proporciona un entorno de ejecución eficiente y escalable para aplicaciones web Python.

**psycopg2-binary==2.9.9:** Psycopg2 es un adaptador de base de datos PostgreSQL para Python que permite a las aplicaciones Python interactuar con bases de datos PostgreSQL.

**celery==5.4.0:** Celery es una biblioteca de Python para la ejecución de tareas en segundo plano o en paralelo, de manera asíncrona. Es comúnmente utilizado para realizar tareas que son intensivas en CPU o que pueden tardar mucho tiempo en completarse, como el envío de correos electrónicos o la generación de informes.

**redis==5.0.4:** Redis es una base de datos en memoria de código abierto que se utiliza comúnmente como almacén de datos en caché o como cola de mensajes en aplicaciones web. La biblioteca Redis proporciona herramientas para interactuar con un servidor Redis desde una aplicación Python.

**qrcode==7.4.2:** Es una biblioteca de Python que permite generar códigos QR de forma programática. Los códigos QR son códigos de barras bidimensionales que pueden contener una variedad de datos, como enlaces URL, texto simple, información de contacto, etc.

### 3. GUIA DE ESTILO DE LA WEB. <a name="id3"></a>

El logro que nos hemos propuesto es establecer pautas visuales y de diseño para una aplicación que permite reservar hamacas y gestionarlas, tanto para usuarios como para administradores. La aplicación debe ser intuitiva, fácil de usar y brindar una experiencia agradable tanto en términos de funcionalidad como de estética:

#### 3.1 Responsividad

Asegurarnos de que la aplicación sea accesible y funcional en todos los dispositivos posibles, desde ordenadores hasta móviles, adaptando el diseño y la disposición según el tamaño de la pantalla.

#### 3.2 Colores

Seleccionar colores que transmitan una sensación de relajación y frescura, acorde con el logo creado y logrando transmitir una sensación de calma y tranquilidad.

#### 3.3 Interfaz

Diseñar una interfaz de usuario que sea intuitiva y fácil de navegar tanto para los usuarios que buscan reservar una hamaca como para los administradores que necesitan gestionarlas. Esto incluye un diseño correcto, botones y elementos con los que se pueda interactuar.

#### 3.4 Respuesta visual

Proporcionar una repuesta visual clara en relación a las acciones del usuario, como confirmaciones de reserva exitosa o mensajes de error. Esto ayuda a mantener al usuario informado sobre el estado de la aplicación y sus acciones.

#### 3.5 Testing y Mejora Continua

Realizar pruebas exhaustivas de usabilidad y recopilar comentarios de los usuarios para identificar áreas de mejora en la interfaz y la experiencia de usuario. La guía de estilo web debe estar sujeta a revisiones y actualizaciones periódicas para garantizar que la aplicación siga siendo efectiva y atractiva para su público objetivo.


### 4. INVESTIGACIÓN. <a name="id4"></a>

Antes de ponernos manos a la obra tuvimos que buscar algunos posibles ejemplos en internet dado que estabamos muy perdidos en como podría ser un diseño apropiado y atractivo. No encontramos gran cosa puesto que la idea había pasado por muy pocas cabezas y nos propusimos a dar rienda suelta a nuestra imaginación. 

Cuando empezamos tuvimos grandes ideas que podíamos aplicar pero el tiempo se nos vino encima y por ende tuvimos que desechar la muy buena idea de aplicar Angular en nuestro proyecto ello influenció en nuestro ritmo y motivación pero logramos seguir hacia adelante y finalizamos el proyecto más o menos por el mismo camino.

### 5. DERECHOS DE AUTOR. <a name="id5"></a>

En todo momento se ha hecho uso de contenido público y el cual se ha sido referenciado para no tener problemas con nadie dado que al igual que nosotros valoramos que respeten lo que hemos desarrollado, también valoramos el trabajo de otras personas los cuales se ganan el pan con mucho esfuerzo.

### 6. RIESGOS Y MEDIDAS. <a name="id6"></a>

Durante el desarrollo del proyecto se nos echó el tiempo encima y tuvimos que dar un paso hacia atras tomando la decisión de no usar un framework de frontend puesto que ello requería el aprenderlo desde cero en un mes y medio que tenemos para realizar el proyecto aproximadamente. Como medida, nos reunimos y tomamos la decisión de seguir hacia adelante y hacerlo lo mejor posible haciendo uso de las herramientas que nos daba Django, HTML, CSS, Bootstrap y JS.

### 7. GRADO DE CUMPLIMIENTO EN ALCANCE. <a name="id7"></a>

Se ha implementado todo lo acordado entre el equipo y el supuesto cliente a excepción de que en el frontend no se ha usado la tecnología acordada debido a la falta de tiempo pero ello no ha impedido que el producto final se vea apropiadamente.

Entre las funcionalidades acordadas que han sido implementadas destacan:

- Pagina Inicial
- Login
- Zona de Clientes para Reservas
- Sistema de Pagos
- PDF para comprobar los pagos vinculado a QR
- Zona de Admin para Gestiones
- API

### 8. GRADO DE CUMPLIMIENTO EN TIEMPO. <a name="id8"></a>

En todo momento se ha cumplido con los periodos de tiempo asignados y de ello ha surgido un beneficio y es el hecho de que gracias a dicha organización adelantamos varias partes del proyecto antes de lo proyectado lo que nos ayudó a mejorar el producto final.
  
### 9. GRADO DE CUMPLIMIENTO EN COSTE. <a name="id9"></a>

Para garantizar que el proyecto se mantenga bien economicamente y cumpla con los objetivos establecidos, se implementarán diversas acciones y pruebas:

#### 9.1 Seguimiento de Presupuesto

Se establecer un sistema de seguimiento y control del presupuesto para monitorear continuamente los costos del proyecto.

#### 9.2 Planificación Detallada

Se realizará una planificación detallada del proyecto que incluya estimaciones de costos para cada tarea y actividad. Esto ayuda a identificar posibles áreas de desviación y tomar medidas preventivas antes de que ocurran.

#### 9.3 Revisiones Periódicas

Se llevarán a cabo revisiones periódicas del estado del proyecto para evaluar el progreso en relación con el presupuesto y los objetivos establecidos. Estas revisiones se harán semanalmente.

#### 9.4 Evaluación de Riesgos

Se evaluarán los riesgos potenciales que podrían afectar los costos del proyecto y desarrollar estrategias para evitar estos riesgos.

#### 9.5 Test de Costeo

Se propondrán pruebas de costeo para asegurarse de que el costo mensual del producto sea realista y preciso. 

#### 9.6 Comunicación

Se mantendrá una comunicación transparente con todas las partes interesadas del proyecto sobre cualquier cosa relacionado al costo del mismo. Esto permite una mayor colaboración y apoyo en la toma de decisiones para mantener el proyecto en curso.

#### 9.7 Aprendizaje Continuo

Se analizará los resultados y lecciones aprendidas para mejorar continuamente los procesos de gestión de costos y evitar errores similares en el futuro.

### 10.  PRODUCTO FINAL. <a name="id10"></a>

#### 10.1 Landing Page

En este apartado se tendrá a disposición de cualquier persona una web en la que podrán encontrar información sobre nosotros, el producto que se ha creado, contacto y lo más importante, un apartado en el que escogerán el hotel donde estén hospedándose o en el caso del administrador donde esté trabajando.

#### 10.2 Login 

En esta zona tanto usuario como administrador tendrán que introducir sus datos para pasar a sus respectivas areas. Si eres administrador pasa directamente al paso **10.4**.

#### 10.3 Zona Cliente

En esta zona el cliente tendrá la posibilidad de hacer una reserva mediante la cual encontrará una serie de apartados en los que seleccionar la fecha y posteriormente la parte de la piscina en la que se quiere quedar. Acto seguido pasará al pago en el cual introducirá sus datos para poder completar la reserva. Por último tendrá la posibilidad de consultar su reserva descargándose un PDF y allí escanear el QR o borrarla en el caso de que se haya equivocado o quiera dar marcha atrás.

#### 10.4 Zona Administrador

En esta zona el administrador llegará a un menú en el que podrá decidir a que área ir (productos, reservas o usuarios) y en cada de uno de ellos hacer modificaciones, borrados, consultas o adiciones ( a excepción de las reservas en las cuales solo se pueden hacer consultas y borrados para ofrecer al consumidor una mejor eficiencia y usabilidad).
    
### 11.  EXPERIENCIAS APRENDIDAS A TENER EN CUENTA EN PRÓXIMOS PROYECTOS. <a name="id11"></a>

**Abián:** Por mi parte creo que el proyecto ha servido bastante puesto que nos ha puesto a mis compañeros y a mi en situaciones difíciles de toma de decisiones y a su vez en conflictos que nos han servido para mejorar el proyecto y también para mejorar como personas y en nuestros ámbitos laborales.

### 12.  CONCLUSIONES, COMENTARIOS Y VALORACIÓN FINAL. <a name="id12"></a>

**Abián:** Creo que para un proyecto como este a sabiendas del poco tiempo que hay puesto que también tenemos que ir a trabajar, no es justo el poco tiempo que se ha proporcionado para el mismo y por ende se debería enfocar que el  trabajo en este proyecto empiece mucho antes de Navidades con el fin de lograr los objetivos en un entorno más realista y tranquilo. Igualmente, dentro de lo que cabe lo hemos logrado sacar hacia adelante y nos hemos llevado una muy buena de experiencia que quedará ahí siempre.

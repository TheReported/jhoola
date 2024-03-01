<div align="center">

# ANTEPROYECTO PARA SOLICITAR LA REALIZACIÓN DEL MÓDULO
# PROYECTO

</div>

<div align="center">
<img src="../img/imagen-descriptiva-si-existe.png" />
</div>


## Indice

1. [IDENTIFICACIÓN](#id1)
2. [OBJETIVOS](#id2)
3. [PREANÁLISIS DE LO EXISTENTE](#id3)
4. [PRE-ANÁLISIS DEL SISTEMA](#id4)
5. [PRE-DISEÑO DEL SISTEMA](#id5)
6. [ESTIMACIÓN DE COSTES](#id6)



### 1. IDENTIFICACIÓN <a name="id1"></a>


+ Nombre del proyecto: Jhoola
+ Alumnos: Abián Gustavo Castañeda Méndez, Diego Peraza Cabo, Samuel Eloy González Díaz
+ Curso: 2ºDAW
+ Tutor: Alejandro Martín Zarza

### 2. OBJETIVOS <a name="id2"></a>

Este proyecto tiene como objetivo el crear una aplicación web dedicada a la reserva y gestión de hamacas en hoteles. Todo el proceso está pensado para realizarse en la distribución Debian GNU/Linux siendo fácil la adaptación para las otras distribuciones existentes. El fin de todo esto, es ofrecer a los huéspedes de un hotel la facilidad de reservar una hamaca sin verse perjudicados de que otros individuos hagan uso de otros objetos para guardarlas durante muchísimas horas.


### 3. PREANÁLISIS DE LO EXISTENTE <a name="id3"></a>

En muchos hoteles, se realiza una mala gestión en lo que se refiere la asignación de hamacas a los huéspedes provocando conflictos entre los mismos a la hora de tomar una. Es injusto para muchos individuos, el despertarse a primera hora de la mañana y ver que otros huéspedes han puesto sus pertenencias en ciertos lugares con el fin de reservar su sitio, por ello se debe asegurar un sistema con el que poner fin a dicha injusta práctica.


### 4. PRE-ANÁLISIS DEL SISTEMA <a name="id4"></a>

Es muy trivial el tener que gestionar este nuevo sistema a papel o mediante alguna aplicación de gestión obsoleta, por ello, una aplicación web a la cual se pueda acceder desde cualquier lado es lo idóneo, puesto que se pueden hacer uso de distintas herramientas con las que hacer la gestión de este proceso. Además, en dicha acción el huésped pueda disponer de la información de su reserva en caso de que lo necesite.


### 5. PRE-DISEÑO DEL SISTEMA <a name="id5"></a>

Para la realización del proyecto se requerirá lo siguiente:

- **Backend**: en lo que respecta el lado servidor hemos optado por usar el Framework Web Django debido a que estamos muy familiarizados con dicha tecnología.

- **Frontend**: en lo referido al lado cliente usaremos HTML / CSS debido a que son herramientas vitales en cualquier proyecto. También usaremos JS, Bootstrap 5 y React con el fin de ofrecer un diseño exquisito e interactivo para el usuario.

- **Despliegue**: en lo relacionado al despliegue del proyecto seguramente usaremos una VPS de Azure, además de el uso de la herramienta Docker. 


### 6. ESTIMACIÓN DE COSTES <a name="id6"></a>

Las estimaciones de costes son las siguientes:

- Aplicación: hemos llegado a la conclusión de ofrecer de manera gratuita un primer mes para más tarde cobrar al cliente 300€ con soporte y 250€ sin soporte (en el caso de). La idea es que a su vez el cliente pueda ganar dinero con las reservas de las hamacas de los huespedes sin que nosotros nos llevemos una parte de ello.

- VPS: hemos realizado una estimación y con una VPS de 4 GB RAM, 2 Cores y 200 GB de almacenimiento SSD nos costaría 30€ al mes aproximadamente.

- Dominio: hemos encontrado un precio bastante fiable que sería 6,95€ al año por el dominio.

    | Servicio | Explicación | Coste | Fuente |
    |----------|-------------|-------|--------|
    | Aplicación con Soporte | La aplicación recibirá soporte por parte de nuestro equipo | 300€ mes | - |
    | Aplicación sin Soporte | La aplicación no recibirá soporte y en el caso de que se requiera se realizaría un precio especial para dicho problema que haya surgido o se le daría la posibilidad al cliente de cambiar de suscripción | 250€ mes | - |
    | Soporte no Incluido | En el caso de que haya que ofrecer soporte a alguien que no ha adquirido la suscripción con soporte | 25€ hora | - |
    | VPS | Una VPS con 4 GB RAM, 2 Cores y 200 GB de almacenimiento SSD | 30 € mes | https://clouding.io/ | 
    | Dominio | Un dominio donde alojar nuestra aplicación web | 6,95€ año | https://www.dondominio.com/ |
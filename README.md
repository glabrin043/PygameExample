# Juego en Python: Conejos y Tejones

## 1. PyGame: ¿Qué vamos a utilizar?

Para desarrollar nuestro juego vamos a utilizar un paquete de Python llamado **Pygame**.

### ¿Qué son los paquetes en Python?

Una de las principales ventajas de utilizar Python es la gran cantidad de librerías y paquetes de código que están disponibles.

Estos paquetes contienen funcionalidades que nos permiten ahorrar tiempo y código, ya que ofrecen herramientas para realizar determinadas tareas de manera más sencilla.

Por ejemplo, Pygame es un paquete que nos proporciona herramientas para desarrollar videojuegos, trabajar con imágenes, reproducir sonidos, detectar eventos y controlar el teclado y el mouse.

### ¿Cómo se instalan los paquetes?

Para instalar un paquete de Python utilizamos el siguiente comando en la terminal:

```bash
pip install nombre-del-paquete
```

Una vez instalado, podemos utilizarlo en nuestros programas importándolo al comienzo del código:

```python
import nombre_del_paquete
```

En nuestro caso, como vamos a trabajar con Pygame, escribimos:

```python
import pygame
```

## 2. Instalación de Pygame

Para instalar Pygame seguimos estos pasos:

1. Abrimos la línea de comandos de Windows presionando `Windows + R`.
2. Escribimos `cmd` y presionamos Enter.
3. En la terminal ejecutamos el siguiente comando:

```bash
pip install pygame
```

Si aparece algún error durante la instalación, podemos probar con:

```bash
python -m pip install -U pygame --user
```

Una vez instalado, ya podemos utilizar Pygame en nuestros programas.

### Documentación oficial

Podemos consultar la página oficial de Pygame para encontrar tutoriales, ejemplos y explicaciones sobre sus funcionalidades:

https://www.pygame.org/docs/

## 3. Descarga de los recursos del juego

Para desarrollar nuestro juego vamos a necesitar diferentes recursos, como imágenes y sonidos.

Podemos descargarlos desde el siguiente repositorio:

**Repositorio de recursos:**

https://github.com/swapagarwal/bunnies-and-badgers/tree/master

Descargamos los recursos del repositorio y los guardamos dentro de la carpeta de nuestro proyecto.

## 4. Organización de las carpetas

Primero, creamos una carpeta nueva donde vamos a guardar todos los archivos de nuestro juego.

Dentro de esa carpeta colocamos el archivo Python y la carpeta de recursos descargados.

La organización del proyecto debería quedar de la siguiente manera:

```text
Pygame/
│
├── juego.py
│
└── resources/
    │
    ├── audio/
    │
    └── images/
```

- **juego.py:** contiene el código fuente de nuestro videojuego.
- **resources:** contiene todos los recursos necesarios para el juego.
- **audio:** almacena los sonidos y archivos de audio.
- **images:** almacena las imágenes que vamos a utilizar, como el conejo, el pasto, los castillos, las flechas y los tejones.

Es importante respetar la ubicación de las carpetas y los nombres de los archivos, ya que nuestro programa necesitará encontrar estos recursos para poder cargarlos correctamente.

A partir de esta estructura comenzaremos a desarrollar nuestro juego paso a paso.
   


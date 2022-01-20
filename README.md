# Pygame-Button-Object
Este proyecto es una clase botón que permite al usuario generar botones al utilizar el módulo pygame, pudiendo generarlos con imagenes o colores lisos, con o sin texto dentro, asi como la posibilidad de asignar funciones a cada botón generado.
Se utilizó python con su módulo pygame ya que es un lenguaje relativamente sencillo de aprender y desarrollar en una institución educativa.

## ¿Como usarla?
Es recomendable poner el archivo dentro de la misma carpeta que el programa principal, de esta forma podremos llamar al módulo sin referir directorios en la computadora.

Para instanciar un objeto botón es como cualquier otra clase creada, es decir, 
```
nombre_variable = Boton(parametros)
```
donde dentro de los parametros, los necesarios para la inicializacion del boton son:

  - **coordenada X del plano** (tipo entero).
 
  - **coordenada Y del plano** (tipo entero).
  
  - **ancho del botón** (tipo entero).
  
  - **alto del botón** (tipo entero).
  
  - **color del botón** (debe ser una tupla con el código RGB).
  
_Dichos parametros puestos en ese orden_, luego tenemos lo kwargs, estos pueden ser cargados luego de los parametros de inicialización dentro de la primera instancia o luego, llamando a la función "opciones" de tal modo que: 
```
nombre_variable.opciones(**kwargs)
```
puestos por ejemplo: 
```
nombre_variable.opciones(command=lambda:funcion(), texto="Hola Mundo!")
```
Estos argumentos claves son:

  - **command**: en este argumento pondremos la función que ejecutará el botón dentro de una función sin nombre (lambda), de esta forma conseguiremos una correcta ejecución de las funciones a llamar, es decir, 
  ```
  command=lambda:funcion()
  ```
  
  
  - **color**: permite cambiar el color asignado anteriormente.
  
  - **texto**: permite asignar texto dentro del botón, dicho texto escalará automaticamente dentro del mismo, asi que es recomendable no ingresar palabras muy largas o frases.
  
  - **ctexto**: opción que permite asignar un color específico a al texto y al igual que el color del botón, debe ser una tupla con el código RGB.
  
  - **press_fx**: opción tipo booleana, activa o desactiva el efecto al presionar el botón, en algunos casos, la animación de presión del botón genera errores por eso es necesario desactivarlo en caso de ser necesario.
  
  - **image**: este parametro toma un objeto tipo pygame.image y lo escala dentro del botón de forma por defecto.
  
  - **imgSize**: al establecer en True este parametro, el botón tomará el tamaño de la imagen asignada anteriormente, cabe destacar que luego de asignar en verdadero este parámetro, no puede deshacerse el reescalado del botón, la unica forma es cambiando el ancho y alto como: 
  ```
  nombre_variable.ancho,nombre_variable.alto=tamaño_ancho,tamaño_alto
  ```
  
## Funciones del objeto

  - **.opciones(kwargs)**:esta función permite ajustar parametros anteriormente detallados.
  
  - **.graf(ventana)**: dicha función es la que dibujará el botón en el plano, tomando como parámetro la ventana de pygame en que se dibujará.
  
  - **.presion(posicion_raton,ventana)**: tomando como parámetros la posicion del raton y la ventana que estamos usando para el botón, nos devolverá True o False dependiendo si presionamos el botón, haciendo la animación (en caso de estar activa) y ejecutando (si tiene) la función asignada.
  
# Créditos
Esta clase fue hecha en conjunto entre Macias Luciano (github user: luichinni) y Payajo Shein (github user: Shein-P)

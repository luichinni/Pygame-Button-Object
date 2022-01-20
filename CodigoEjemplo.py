"""
PYGUTILIDADES BY: MACÍAS LUCIANO, PAYAJO SHEIN
"""

# Importamos las librerias
import pygame.locals 
from pygutilidades import Boton
import sys
# Iniciamos pygame
pygame.init()
# Ancho y alto de la pantalla
ancho, alto = 800, 500
resolucion = (ancho,alto)
pantalla = pygame.display.set_mode(resolucion) # Resolucion
pygame.display.set_caption("Boton") # Nombre del programa
# Instancia del clock
clock = pygame.time.Clock()
# Color 		R 		G 		B
negro 	= 	(0		,0		,0		)
blanco 	=	(255	,255	,255	)
naranja = 	(255	,112	,40		)
# Función 
def saludo():
	print("Hola Mundo")

# Cargamos la imagen del boton
iboton = pygame.image.load('imagenes/Boton.png').convert_alpha()

# Declaramos el boton
Botn_img = Boton(450,200,100,50,negro)
# Añadimos las opciones
# Damos la imagen y modificamos el area de presion al de la imagen
Botn_img.opciones(image=iboton,imgSize=True)
Botn_img.opciones(texto="pygutilidades",ctexto=negro)

# Declaramos el boton
Botn_1 = Boton(100,100,200,100,naranja)
# Añadimos las opciones
Botn_1.opciones(command=lambda:saludo(),texto="Hola!",ctexto=negro)

# Los almacenamos en lista para poder iterar sobre ellos
botones = [Botn_img,Botn_1]

# Graficamos los botones
for botonsito in botones:
	botonsito.graf(pantalla)

# Bucle principal
done = False
while not done:
	# Detector de eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Evento para finalizar el bucle
			done=True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			"""
			Detectamos si el mouse fue presionado para luego tomar sus
			coordenadas y pasarlas.
			"""
			posi = pygame.mouse.get_pos()

			# Detectamos si fue presionado alguno
			for botonsito in botones:
				botonsito.presion(posi,pantalla)

	clock.tick(60) # Bucle 60 veces por segundo

	pygame.display.flip() # Actualización de la pantalla

sys.exit()
pygame.quit
# Importamos las librerias
import pygame.locals
import sys

#================================================================================================================
#================================================================================================================
# Clase Boton para Pygame
class Boton:
	def __init__ (self,x,y,ancho,alto,bcolor,**kwargs):
		# Permitimos solo int para las coordenadas
		if not type(x) is int:
			raise TypeError("Valor de 'x' debe ser tipo 'int'")
		else: 
			self.x = x

		if not type(y) is int:
			raise TypeError("Valor de 'y' debe ser tipo 'int'")
		else:
			self.y = y

		# Permitimos solo int para el tamaño
		if not type(ancho) is int:
			raise TypeError("Valor de 'ancho' debe ser tipo 'int'")
		else:
			self.ancho = ancho

		if not type(alto) is int:
			raise TypeError("Valor de 'alto' debe ser tipo 'int'")
		else:
			self.alto = alto

		# El color debe ser ingresado como tupla
		if not type(bcolor) is tuple:
			raise TypeError("'Color de boton' debe ser tipo 'tupla'")
		else:
			self.color = bcolor

		self.press_fx = True
		self.image = None
		# Forma del boton
		self.cuadro = pygame.Rect(self.x,self.y,self.ancho,self.alto)
		# Argumentos especiales
		self.opciones(**kwargs)

	def opciones(self,**kwargs):
		for key in kwargs:
			if key == "command":
				self.command = kwargs[key]
			elif key == "color":
				if not type(kwargs[key]) is tuple:
					raise TypeError("'Color de boton' debe ser tipo 'tupla'")
				else:
					self.color = kwargs[key]
			elif key == "texto":
				if not type(kwargs[key]) is str:
					raise TypeError("El atributo 'texto' debe ser tipo 'str'")
				else:
					self.texto = kwargs[key]
			elif key == "ctexto":
				if not type(kwargs[key]) is tuple:
					raise TypeError("'Color de texto' debe ser tipo 'tupla'")
				else:
					self.ctexto = kwargs[key]
			elif key == "press_fx":
				if not type(kwargs[key]) is bool:
					raise TypeError("'Efecto de presion' debe ser tipo 'bool'")
				else:
					self.press_fx = kwargs[key]
			elif key == "image":
				self.image = kwargs[key]
				darken_percent = .50
				self.dimage = pygame.Surface(self.image.get_size()).convert_alpha()
				self.dimage.fill((0, 0, 0, darken_percent*255))

			elif key == "imgSize" and kwargs[key] == True and self.image != None:
				self.ancho,self.alto = self.image.get_size()
				self.cuadro = pygame.Rect(self.x,self.y,self.ancho,self.alto)

	def graf(self,ventana):
		
		if self.image == None:
			# Lo dibujamos
			pygame.draw.rect(ventana,self.color,self.cuadro)
		else:
			# Cargamos la imagen a la pantalla
			ventana.blit(self.image,(self.x,self.y))

		# Si se le ha dado una imagen intetaremos dibujarla en el tamaño que corresponde

		# Si se le ha dado un texto intentaremos escribirlo sobre el boton
		try:
			"""
			#Detectamos si se ha pasado texto como parametro y de esta forma
			#solo renderizamos cuando es necesario
			"""
			if self.texto != "":
				# Por temas de diseño, el tamaño máximo de fuente es 40
				self.tsize = self.ancho
				if self.tsize > 40: 
					fuente = pygame.font.SysFont("Times New Roman", 40)
				else:
					fuente = pygame.font.SysFont("Times New Roman", self.tsize)

				# Obtenemos el tamaño del texto para poder acomodar sus coordenadas
				fx,fy = fuente.size(self.texto)
				fux,fuy = int(self.x+(self.ancho/2)-(fx/2)), int(self.y+(self.alto/2)-(fy/2))

				"""
				#Para evitar que el texto se salga del boton establecemos que cuando
				#este es mayor al tamaño pasado, se hará más pequeño
				"""
				if fx > self.ancho:
					while fx >= self.ancho and fx > 0:
						self.tsize -= 1
						fuente = pygame.font.SysFont("Times New Roman", self.tsize)
						fx,fy = fuente.size(self.texto)
						fux,fuy = int(self.x+(self.ancho/2)-(fx/2)), int(self.y+(self.alto/2)-(fy/2))

					if fx >= self.ancho:
						self.texto = ""

				# Finalmente lo renderizamos
				rendertxt = fuente.render(self.texto,0,self.ctexto)

				# Lo cargamos
				ventana.blit(rendertxt,(fux,fuy))
		except:
			pass

	def presion(self,pos,ventana):
		"""
		#Haciendo uso de la herramienta collidepoint de pygame,
		#detectamos si las coordenadas del mouse se encuentran 
		#dentro del area del boton
		"""
		if self.cuadro.collidepoint(pos) and self.press_fx == True:

			if self.image == None:
				aux = self.color # Guardamos el color original
				R,G,B = self.color # Desarmamos la tupla
				R,G,B = R-50,G-50,B-50 # Modificamos los valores

				# Verificamos que no hayan numeros negativos
				if R < 0: R=0
				if G < 0: G=0
				if B < 0: B=0
				# Almacenamos los nuevos colores oscurecidos en una tupla
				sombra = (R,G,B)

				# Establecemos esta sombra como color del boton
				self.color = sombra

				# Redibujamos el boton presionado para dar el efecto
				self.graf(ventana)
				pygame.display.flip()

				# Reestablecemos el color original
				self.color = aux
				self.graf(ventana)

			else:
				# Cargamos la imagen oscurecida
				ventana.blit(self.dimage,(self.x,self.y))
				# Actualizamos para dar el efecto
				pygame.display.update(self.cuadro)
				# Cargamos la antigua imagen
				self.graf(ventana)
			
			try:
				self.command()
			except:
				pass

			return True
			
		else:
			return False

#================================================================================================================
#================================================================================================================
from arbolB import arbolB
from nodoUsuario import nodoUsuario
import os
class Sesion():
	def __init__(self):
		self.ultimo=None

	def crear(self,user,password):
		cad =str(os.path.abspath(""))+"/DRIVE"
		print cad
		usuario = nodoUsuario(user,password,user,None,None)
		if self.ultimo==None:
			usuario.next=usuario
			usuario.prev=usuario
			self.ultimo=usuario
			return user+" fue creado con exito"
		else:
			temp = self.ultimo.next
			while temp!=self.ultimo:
				if temp.user>user:
					usuario.prev = temp.prev
					temp.prev.next=usuario
					usuario.next= temp
					temp.prev = usuario
					# ****ACA SE CREA LA CARPETA *** #
					# ****ACA SE CREA LA CARPETA *** #
					# ****ACA SE CREA LA CARPETA *** #
					return user+" fue creado con exito"
				elif temp.user==user:
					return "este usuario ya existe"
				temp=temp.next

			if temp.user>user:
				usuario.prev = temp.prev
				temp.prev.next=usuario
				usuario.next= temp
				temp.prev = usuario

			elif temp.user<user:
				temp.next.prev=usuario
				usuario.next=temp.next
				temp.next=usuario
				usuario.prev=temp
				self.ultimo=temp
			else:
				return "este usuario ya existe"

			# ****ACA SE CREA LA CARPETA *** #
			# ****ACA SE CREA LA CARPETA *** #
			# ****ACA SE CREA LA CARPETA *** #
			return user+" fue creado con exito"

	def login(self,user,password):
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user and temp.password == password:
					# ****ACA SE MUESTRA LA CARPETA ***
					# ****ACA SE MUESTRA LA CARPETA ***
					# ****ACA SE MUESTRA LA CARPETA ***
					return "V"
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user==user and temp.password==password:
				# ****ACA SE MUESTRA LA CARPETA ***
				# ****ACA SE MUESTRA LA CARPETA ***
				# ****ACA SE MUESTRA LA CARPETA ***
				return "V"
			else:
				return "F"
		else:
			return "F"





	def crearCarpeta(self,nombre):
		cad =str(os.path.abspath(""))
		print cad
		return cad
		



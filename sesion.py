from arbolB import arbolB
from nodoUsuario import nodoUsuario
from random import choice

import os
class Sesion():
	def __init__(self):
		self.ultimo=None

	def crear(self,user,password):
		cad =str(os.path.abspath(""))+"/NUBE/"+user
		longitud = 18
		valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		key = ""
		key = key.join([choice(valores) for i in range(longitud)])
		nuevo = arbolB()
		cad=nuevo.crear()

		usuario = nodoUsuario(user,password,cad,key,None,None)
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
					os.mkdir(cad)
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

			os.mkdir(cad)
			return user+" fue creado con exito"

	def login(self,user,password):
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user and temp.password == password:
					return temp.carpetas
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user==user and temp.password==password:
				return temp.carpetas
			else:
				return "F"
		else:
			return "F"



	def obtener_ruta(self,user):
		temp=self.ultimo.next
		while temp!=self.ultimo:
			if temp.user==user:
				return temp.carpetas
			elif temp.user>user:
				return "-"
			temp=temp.next

		if temp.user==user:
			return temp.carpetas
		else:
			return "-"

	def obtener_grafo(self):
		temp = self.ultimo.next
		cad="digraph g{";
		while temp!=self.ultimo:
			cad=cad+temp.user+"->"+temp.next.user+";"
			cad=cad+temp.next.user+"->"+temp.user+";"
			temp=temp.next
		return cad+"}"




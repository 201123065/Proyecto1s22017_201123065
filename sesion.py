from arbolB import arbolB
from nodoUsuario import nodoUsuario
from random import choice

import os
class Sesion():
	def __init__(self):
		self.ultimo=None

	def crear(self,user,password):
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
					return "V"
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user==user and temp.password==password:
				return "V"
			else:
				return "F"
		else:
			return "F"
	def obtener_raiz(self,user):
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user:
					return temp.carpetas
				elif temp.user>user:
					return None
				else:
					temp=temp.next
			if temp.user==user:
				return temp.carpetas
			else:
				return None
		return None
	def carpetas(self,tst):
		folder = self.obtener_raiz(tst)
		if folder==None:
			return "F"
		else:
			return "<ul>"+self.muestra(folder)+"</ul>"

	def muestra(self,folder):
		cad=""
		if folder.p1!=None:
			cad=cad+self.muestra(folder.p1)
		if folder.c1!=None:
			cad=cad+"<li>"+folder.c1+"</li>"
		if folder.p2!=None:
			cad=cad+self.muestra(folder.p2)
		if folder.c2!=None:
			cad=cad+"<li>"+folder.c2+"</li>"
		if folder.p3!=None:
			cad=cad+self.muestra(folder.p3)
		if folder.c3!=None:
			cad=cad+"<li>"+folder.c3+"</li>"
		if folder.p4!=None:
			cad=cad+self.muestra(folder.p4)
		if folder.c4!=None:
			cad=cad+"<li>"+folder.c4+"</li>"
		if folder.p5!=None:
			cad=cad+self.muestra(folder.p5)
		return cad



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




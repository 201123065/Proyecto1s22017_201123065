from nodoB import nodoB
from nodoUsuario import nodoUsuario
from random import choice
from tupla import tupla

import os
class Sesion():
	def __init__(self):
		self.ultimo=None
		self.logrado="F"
# ---------------------------------------------------------------------
# --------------------------- CREAR USUARIO ---------------------------
# ---------------------------------------------------------------------
	def crear(self,user,password):
		longitud = 18
		valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		key = ""
		key = key.join([choice(valores) for i in range(longitud)])
		cad=nodoB(None,None,None,None,None,None,None,None,None)

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
			return user+" fue creado con exito"

# ---------------------------------------------------------------------
# -------------------------- INICIAR SESION ---------------------------
# ---------------------------------------------------------------------

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
# ---------------------------------------------------------------------
# --------------------------- MOSTRAR ARCHIVOS -------------------------
# ---------------------------------------------------------------------
	def mostrarArchivos(self,ruta):
		user= ruta.split("/")[0]
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user == user:
					return self.listar_documentos(ruta,temp.carpetas)
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user == user:
				return self.listar_documentos(ruta,temp.carpetas)
			else:
				return "F"
		else:
			return "F"

	def listar_documentos(self,url,carpetas):
		i=1
		cad="raiz/"
		while len(url.split("/"))-1>i:
			cad=cad+url.split("/")+"/"
			carpetas=self.buscar_carpeta(url.split[i],carpetas)
			i=i+1
		print cad
		retorno = self.showFiles(cad,carpetas)
		if retorno=="":
			return "F"
		else:
			return retorno

	def showFiles(self,url,raiz):
		cad=""
		if raiz.p1!=None:
			cad=cad+self.showFiles(raiz.p1)
		if raiz.c1!=None:
			cad=cad+"<input type='button' value='"+raiz.c1.nombre+"' class='btn-warning'  onclick='aURL()' id='boton'><br/>"
		if raiz.p2!=None:
			cad=cad+self.showFiles(raiz.p2)
		if raiz.c2!=None:
			cad=cad+"<input type='button' value='"+raiz.c2.nombre+"' class='btn-warning' onclick='aURL() id='boton'><br/>"
		if raiz.p3!=None:
			cad=cad+self.showFiles(raiz.p3)
		if raiz.c3!=None:
			cad=cad+"<input type='button' value='"+raiz.c3.nombre+"' class='btn-warning' onclick='aURL() id='boton'><br/>"
		if raiz.p4!=None:
			cad=cad+self.showFiles(raiz.p4)
		if raiz.c4!=None:
			cad=cad+"<input type='button' value='"+raiz.c4.nombre+"' class='btn-warning' onclick='aURL() id='boton'><br/>"
		if raiz.p5!=None:
			cad=cad+self.showFiles(raiz.p5)
		return cad


# ---------------------------------------------------------------------
# --------------------------- CARGAR CARPETA --------------------------
# ---------------------------------------------------------------------
	def setFolder(self,url,folder):
		user= url.split("/")[0]
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user == user:
					temp.carpetas=self.agregarFolder(url,temp.carpetas,folder)
					return self.logrado
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user == user:
				temp.carpetas=self.agregarFolder(url,temp.carpetas,folder)
				return self.logrado
			else:
				return "F"
		else:
			return "F"

	def agregarFolder(self,url,carpetas,nombre):
		i=1
		self.logrado="F"
		while len(url.split("/"))-1>i:
			carpetas=self.buscar_carpeta(url.split[i],carpetas)
			i=i+1
		nuevoB= nodoB(None,None,None,None,None,None,None,None,None)
		folder=tupla(nombre,nuevoB,None)
		print "siii, entra aca"
		return self.recursivo(folder,carpetas)


	def recursivo(self,folder,raiz):
		if raiz.c1==None:
			print "agrega en c1"
			raiz.c1=folder
			self.logrado="V"
		elif raiz.c1.nombre>folder.nombre:
			print "nombre < c1.nombre"
			if raiz.p1==None:
				print "es hoja"
				if raiz.c2==None:
					print "agrega en c1, desplaza c1"
					raiz=nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
				elif raiz.c3==None:
					print "agrega en c1, desplaza c1,c2"
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,None,None)
				elif raiz.c4==None:
					print "agrega en c1, desplaza c1,c2,c3"
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,raiz.c3,None)
				else:
					print "agrega en c1, crea arbol c1,c2,r,c3,c4"
					izq =nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
					der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
					return raiz
				self.logrado="V"
			else:
				print "es padre, entra a p1"
				temp = self.recursivo(folder,raiz.p1)
				if temp.p1==None:
					print "hijo unico"
					raiz.p1=temp
				else:
					print "retorno una hoja"
					if raiz.c2==None:
						print "entro a p1, corre c1 "
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
					elif raiz.c3==None:
						print "entro a p1, corre c1,c2 "
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None)
					elif raiz.c4==None:
						print "entro a p1, corre c1,c2,c3 "
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
					else:
						print "entro a p1, genera arbol (c2) "
						izq =nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
						der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
						return raiz
				self.logrado="V"
		elif raiz.c1.nombre<folder.nombre:
			if raiz.c2==None:
				if raiz.p2==None:
					print "es hoja"
					raiz=nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
				else:
					# BAANNDEEERAAA
					print "es padre"
					temp= self.recursivo(folder,raiz.p2)
					if temp.p1==None:
						raiz.p2=temp
					else:
						raiz=nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
				self.logrado="V"
			elif raiz.c2.nombre>folder.nombre:
				if raiz.p2==None:
					print "es hoja"
					if raiz.c3==None:
						print "agrega en c2, desplaza c2"
						raiz=nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,None,None)
					elif raiz.c4==None:
						print "agrega en c2, desplaza c2,c3"
						raiz=nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,raiz.c3,None)
					else:
						print "genera arbol (c2) "
						izq =nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
						der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
						return raiz
					self.recursivo="V"
				else:
					temp=self.recursivo(folder,raiz.p2)
					if temp.p1==None:
						print "es hoja"
						raiz.p2=temp
					else:
						if raiz.c3==None:
							raiz=nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,None,None)
						elif raiz.c4==None:
							raiz=nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
						else:
							izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
							der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
							raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
							return raiz
					self.logrado="V"
			elif raiz.c2.nombre<folder.nombre:
				if raiz.c3==None:
					if raiz.p3==None:
						print "es hoja"
						raiz=nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,None,None)
					else:
						temp= self.recursivo(folder,raiz.p3)
						if temp.p1==None:
							raiz.p3=temp
						else:
							return nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,None,None)
					self.logrado="V"
				elif raiz.c3.nombre>folder.nombre:
					if raiz.p3==None:
						print "es hoja"
						if raiz.c4==None:
							print "agrega en c3, desplaza c3,c4"
							raiz=nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,raiz.c3,None)
						else:
							print "genera arbol (folder) "
							izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
							der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
							raiz=nodoB(izq,folder,der,None,None,None,None,None,None)
							return raiz
						self.recursivo="V"
					else:
						temp=self.recursivo(folder,raiz.p3)
						if temp.p1==None:
							print "es hoja"
							raiz.p3=temp
						else:
							if raiz.c4==None:
								raiz=nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,raiz.c3,raiz.p4)
							else:
								izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,None,None,None,None)
								der =nodoB(temp.p2,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
								raiz=nodoB(izq,temp.c1,der,None,None,None,None,None,None)
								return raiz
						self.logrado="V"
				elif raiz.c3.nombre<folder.nombre:
					if raiz.c4==None:
						if raiz.p4==None:
							print "es hoja"
							raiz=nodoB(None,raiz.c1,None,raiz.c2,None,raiz.c3,None,folder,None)
						else:
							temp= self.recursivo(folder,raiz.p4)
							if temp.p1==None:
								raiz.p4=temp
							else:
								raiz=nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,temp.p1,temp.c1,temp.p2)
						self.logrado="V"

					elif raiz.c4.nombre>folder.nombre:
						if raiz.p4==None:	
							print "genera arbol (c3) "
							izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
							der =nodoB(None,folder,None,raiz.c4,None,None,None,None,None)
							raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
							self.recursivo="V"
							return raiz
						else:
							temp=self.recursivo(folder,raiz.p4)
							if temp.p1==None:
								print "es hoja"
								raiz.p4=temp
							else:	
								izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
								der =nodoB(temp.p1,temp.c1,temp.p2,raiz.c4,raiz.p5,None,None,None,None)
								raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								return raiz
							self.logrado="V"
					elif raiz.c4.nombre<folder.nombre:
						print "aca llega,ok,es c4"
						if raiz.p5==None:
							print "es hoja, genera un arbol"
							izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
							der =nodoB(None,raiz.c4,None,folder,None,None,None,None,None)
							raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
							return raiz
							self.recursivo="V"
						else:
							temp=self.recursivo(folder,raiz.p5)
							print "aca habra clavo?"
							if temp.p1==None:
								raiz.p5=temp
							else:
								izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
								der =nodoB(raiz.p4,raiz.c4,temp.p1,temp.c1,temp.p2,None,None,None,None)
								raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								return raiz
							self.logrado="V"
					else:
						self.logrado="F"
				else:
					self.logrado="F"
			else:
				self.logrado="F"
		else:
			self.logrado="F"
		return raiz













	def obtener_grafo(self):
		temp = self.ultimo.next
		cad="digraph g{";
		while temp!=self.ultimo:
			cad=cad+temp.user+"->"+temp.next.user+";"
			cad=cad+temp.next.user+"->"+temp.user+";"
			temp=temp.next
		return cad+"}"




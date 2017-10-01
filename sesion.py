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
		print ruta
		print user
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
		while len(url.split("/"))-1>i:
			carpetas=self.buscar_carpeta(url.split[i],carpetas)
			i=i+1
		retorno = self.showFiles(carpetas)
		if retorno=="":
			return "F"
		else:
			return "<ul>"+retorno+"</ul>"

	def showFiles(self,raiz):
		cad=""
		if raiz.p1!=None:
			cad=cad+self.showFiles(raiz.p1)
		if raiz.c1!=None:
			cad=cad+"<li>"+raiz.c1.nombre+"</li>"
		if raiz.p2!=None:
			cad=cad+self.showFiles(raiz.p2)
		if raiz.c2!=None:
			cad=cad+"<li>"+raiz.c2.nombre+"</li>"
		if raiz.p3!=None:
			cad=cad+self.showFiles(raiz.p3)
		if raiz.c3!=None:
			cad=cad+"<li>"+raiz.c3.nombre+"</li>"
		if raiz.p4!=None:
			cad=cad+self.showFiles(raiz.p4)
		if raiz.c4!=None:
			cad=cad+"<li>"+raiz.c4.nombre+"</li>"
		if raiz.p5!=None:
			cad=cad+self.showFiles(raiz.p5)
		return cad


# ---------------------------------------------------------------------
# --------------------------- CARGAR CARPETA --------------------------
# ---------------------------------------------------------------------
	def setFolder(self,url,folder):
		print url
		print folder
		user= url.split("/")[0]
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user == user:
					print "hola?"
					temp.carpetas=self.agregarFolder(url,temp.carpetas,folder)
					return self.logrado
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user == user:
				print "hay alguien aca?"
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
		return self.recursivo(folder,carpetas)


	def recursivo(self,folder,raiz):
		if raiz.c1==None:
			raiz.c1=folder
			self.logrado="V"
		elif raiz.c1.nombre>folder.nombre:
			if raiz.p1==None:
				if raiz.c2==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
				elif raiz.c3==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,None,None)
				elif raiz.c4==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,raiz.c3,None)
				else:
					izq =nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
					der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
			else:
				temp = self.recursivo(folder,raiz.p1)
				if temp.p1!=None:
					if raiz.c2==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
					elif raiz.c3==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None)
					elif raiz.c4==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
					else:
						izq =nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
						der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
		elif raiz.c1.nombre<folder.nombre:
			if raiz.p2==None:
				if raiz.c2==None:
					raiz =nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
				elif raiz.c2.nombre>folder.nombre:
					if raiz.c3==None:
						raiz =nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,None,None)
					elif raiz.c4==None:
						raiz =nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,raiz.c3,None)
					else:
						izq =nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
						der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
					self.logrado="V"
				elif raiz.c2.nombre<folder.nombre:
					if raiz.p3==None:
						if raiz.c3==None:
							raiz =nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,None,None)
						elif raiz.c3.nombre>folder.nombre:
							if raiz.c4==None:
								raiz =nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,raiz.c3,None)
							else:
								izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
								der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
								raiz=nodoB(izq,folder,der,None,None,None,None,None,None)
							self.logrado="V"
						elif raiz.c3.nombre<folder.nombre:
							if raiz.p4==None:
								if raiz.c4==None:
									raiz =nodoB(None,raiz.c1,None,raiz.c2,None,raiz.c3,None,folder,None)
								elif raiz.c4.nombre>folder.nombre:
									izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
									der =nodoB(None,folder,None,raiz.c4,None,None,None,None,None)
									raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								elif raiz.c4.nombre<folder.nombre:
									if raiz.p5==None:
										izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
										der =nodoB(None,raiz.c4,None,folder,None,None,None,None,None)
										raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
									else:
										temp = self.recursivo(folder,self.p5)
										if temp.p1!=None:
											izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
											der =nodoB(raiz.p4,raiz.c4,temp.p1,temp.c1,temp.p2,None,None,None,None)
											raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
										self.logrado="V"
								else:
									self.logrado="F"
								return raiz
							else:
								temp= self.recursivo(folder,raiz.p4)
								if temp.p1!=None:
									if raiz.c4==None:
										raiz=nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,temp.p1,temp.c1.temp.p2)
									else:
										izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
										der =nodoB(temp.p1,temp.c1,temp.p2,raiz.c4,raiz.c5,None,None,None,None)
										raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								self.logrado="V"
						else:
							self.logrado="F"
					else:
						temp = self.recursivo(folder,raiz.p3)
						if temp.p1!=None:
							if raiz.c3==None:
								raiz =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,None,None)
							elif raiz.c4==None:
								raiz =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,raiz.c3,raiz.p4)
							else:
								izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,None,None,None,None)
								der =nodoB(temp.p2,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
								raiz=nodoB(izq,temp.c1,der,None,None,None,None,None,None)
						self.logrado="V"
				else:
					self.logrado="F"
			else:
				temp= self.recursivo(folder,raiz.p2)
				if raiz.c2==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
				elif raiz.c3==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,None,None)
				elif raiz.c4==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
				else:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
					der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.c5,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
		else:
			self.logrado="F"
		return raiz














# ---------------------------------------------------------------------
# --------------------------- LISTAR ARCHIVOS -------------------------
# ---------------------------------------------------------------------

	def listarArchivos(self,url,nombre):

		name=""
		i=1
		while len(ruta.split("/"))>i:
			name=name+ruta.split("/")[i]+"/"
			i=i+1
		user= url.split("/")[0]
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user :
					return file_route(url,temp.carpetas,nombre)
				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user==user:
				return file_route(url,temp.carpetas,nombre)
			else:
				return "F"
		else:
			return "F"

	def file_route(self,ruta,carpetas,nombre):
		name=""
		i=1
		hoja=carpetas
		while len(ruta.split("/"))-1>i:
			hoja=buscar_carpeta(ruta.split("/")[i],hoja)
			i=i+1
		carpeta=tupla()
		return "recursivo(,hoja)"

	def buscar_carpeta(self,nombre,hoja):
		if hoja.c1!=None:
			if hoja.c1.nombre>nombre:
				if hoja.p1!=None:
					return self.buscar_carpeta(nombre,hoja.p1)
				return None
			elif hoja.c1.nombre<nombre:
				if hoja.c2.nombre>nombre:
					if hoja.p2!=None:
						return self.buscar_carpeta(nombre,hoja.p2)
					return None
				elif hoja.c2.nombre<nombre:
					if hoja.c3.nombre>nombre:
						if hoja.p3!=None:
							return self.buscar_carpeta(nombre,hoja.p3)
						return None
					elif hoja.c3.nombre<nombre:
						if hoja.c4.nombre>nombre:
							if hoja.p4!=None:
								return self.buscar_carpeta(nombre,hoja.p4)
							return None
						elif hoja.c4.nombre<nombre:
							return self.buscar_carpeta(nombre,hoja.p5)
						else:
							return hoja.c4
					else:
						return hoja.c3
				else:
					return hoja.c2
			else:
				return hoja.c1
		else:
			return None


	def recursivo(self,folder,raiz):
		if raiz.c1==None:
			raiz.c1=folder
			self.logrado="V"
		elif raiz.c1.nombre>folder.nombre:
			if raiz.p1==None:
				if raiz.c2==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
				elif raiz.c3==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,None,None)
				elif raiz.c4==None:
					raiz=nodoB(None,folder,None,raiz.c1,None,raiz.c2,None,raiz.c3,None)
				else:
					izq =nodoB(None,folder,None,raiz.c1,None,None,None,None,None)
					der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
			else:
				temp = self.recursivo(folder,raiz.p1)
				if temp.p1!=None:
					if raiz.c2==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
					elif raiz.c3==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None)
					elif raiz.c4==None:
						raiz = nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
					else:
						izq =nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
						der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
		elif raiz.c1.nombre<folder.nombre:
			if raiz.p2==None:
				if raiz.c2==None:
					raiz =nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
				elif raiz.c2.nombre>folder.nombre:
					if raiz.c3==None:
						raiz =nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,None,None)
					elif raiz.c4==None:
						raiz =nodoB(None,raiz.c1,None,folder,None,raiz.c2,None,raiz.c3,None)
					else:
						izq =nodoB(None,raiz.c1,None,folder,None,None,None,None,None)
						der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
					self.logrado="V"
				elif raiz.c2.nombre<folder.nombre:
					if raiz.p3==None:
						if raiz.c3==None:
							raiz =nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,None,None)
						elif raiz.c3.nombre>folder.nombre:
							if raiz.c4==None:
								raiz =nodoB(None,raiz.c1,None,raiz.c2,None,folder,None,raiz.c3,None)
							else:
								izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
								der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
								raiz=nodoB(izq,folder,der,None,None,None,None,None,None)
							self.logrado="V"
						elif raiz.c3.nombre<folder.nombre:
							if raiz.p4==None:
								if raiz.c4==None:
									raiz =nodoB(None,raiz.c1,None,raiz.c2,None,raiz.c3,None,folder,None)
								elif raiz.c4.nombre>folder.nombre:
									izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
									der =nodoB(None,folder,None,raiz.c4,None,None,None,None,None)
									raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								elif raiz.c4.nombre<folder.nombre:
									if raiz.p5==None:
										izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
										der =nodoB(None,raiz.c4,None,folder,None,None,None,None,None)
										raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
									else:
										temp = self.recursivo(folder,self.p5)
										if temp.p1!=None:
											izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
											der =nodoB(raiz.p4,raiz.c4,temp.p1,temp.c1,temp.p2,None,None,None,None)
											raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
										self.logrado="V"
								else:
									self.logrado="F"
								return raiz
							else:
								temp= self.recursivo(folder,raiz.p4)
								if temp.p1!=None:
									if raiz.c4==None:
										raiz=nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,raiz.c3,temp.p1,temp.c1.temp.p2)
									else:
										izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
										der =nodoB(temp.p1,temp.c1,temp.p2,raiz.c4,raiz.c5,None,None,None,None)
										raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
								self.logrado="V"
						else:
							self.logrado="F"
					else:
						temp = self.recursivo(folder,raiz.p3)
						if temp.p1!=None:
							if raiz.c3==None:
								raiz =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,None,None)
							elif raiz.c4==None:
								raiz =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,temp.c1,temp.p2,raiz.c3,raiz.p4)
							else:
								izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,temp.p1,None,None,None,None)
								der =nodoB(temp.p2,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
								raiz=nodoB(izq,temp.c1,der,None,None,None,None,None,None)
						self.logrado="V"
				else:
					self.logrado="F"
			else:
				temp= self.recursivo(folder,raiz.p2)
				if raiz.c2==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
				elif raiz.c3==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,None,None)
				elif raiz.c4==None:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,raiz.c2,raiz.p3,raiz.c3,raiz.p4)
				else:
					izq =nodoB(raiz.p1,raiz.c1,temp.p1,temp.c1,temp.p2,None,None,None,None)
					der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.c5,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
				self.logrado="V"
		else:
			self.logrado="F"
		return raiz








































	def obtener_raiz(self,user):
		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user:
					return self.inspeccionar_folder(temp)
				elif temp.user>user:
					return None
				else:
					temp=temp.next
			if temp.user==user:
				return self.inspeccionar_folder(temp)
			else:
				return None
		return None

	def inspeccionar_folder(self,folder):
		prueba = arbolB()
		print folder
		print folder.carpetas.p1
		return ";)"






	def crear_folder(self,nombre,ruta):
		user = ruta.split("/")[0]
		name=""
		i=1
		while len(ruta.split("/"))>i:
			name=name+ruta.split("/")[i]+"/"
			i=i+1

		este=None

		if self.ultimo!=None:
			temp=self.ultimo.next
			while temp!=self.ultimo:
				if temp.user==user:
					este= temp.carpetas

				elif temp.user>user:
					return "F"
				else:
					temp=temp.next
			if temp.user==user:
				este= temp.carpetas

			else:
				return "F"
		else:
			return "F"
		print str(este)
		return "V"








	def carpetas(self,folder):
		if folder==None:
			return "F"
		else:
			par= arbolB()
			return par.listar(folder)

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




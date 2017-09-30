from nodoB import nodoB
from carpeta import carpeta
from tupla import tupla
class arbolB :
	def __init__(self):
		self.raiz=None
		self.logrado="F"
	def crear(self):
		self.raiz=nodoB(None,None,None,None,None,None,None,None,None)

	def ver(self):
		return "<ul>"+self.listar(self.raiz)+"</ul>"

	def listar(self,raiz):
		cad=""
		if raiz.p1!=None:
			cad=cad+"<li>"+self.listar(raiz.p1)+"</li>"
		if raiz.c1!=None:
			cad=cad+"<li>"+raiz.c1+"</li>"
		if raiz.p2!=None:
			cad=cad+"<li>"+self.listar(raiz.p2)+"</li>"
		if raiz.c2!=None:
			cad=cad+"<li>"+raiz.c2+"</li>"
		if raiz.p3!=None:
			cad=cad+"<li>"+self.listar(raiz.p3)+"</li>"
		if raiz.c3!=None:
			cad=cad+"<li>"+raiz.c3+"</li>"
		if raiz.p4!=None:
			cad=cad+"<li>"+self.listar(raiz.p4)+"</li>"
		if raiz.c4!=None:
			cad=cad+"<li>"+raiz.c4+"</li>"
		if raiz.p5!=None:
			cad=cad+"<li>"+self.listar(raiz.p5)+"</li>"
		return cad



	def agregar(self,name):
		folderlist=self.crear()
		carpeta = tupla(name,folderlist,None)
		self.raiz = self.recursivo(carpeta,self.raiz)
		return self.logrado

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




			
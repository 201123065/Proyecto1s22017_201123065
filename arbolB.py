from nodoB import nodoB
from carpeta import carpeta
class arbolB :
	def __init__(self):
		self.raiz=None
	def crear(self):
		self.raiz=nodoB(None,None,None,None,None,None,None,None,None)

	def agregar(self,archivo):


		if self.raiz==None:
			self.raiz=nodoB(None,nombre,None,None,None,None,None,None,None)

		else:
			self.recursivo(nombre,self.raiz)

	def recursivo(self,nombre,raiz):
		if raiz.p1==None:
			if raiz.c1==None:
				raiz.c1=nombre
			elif raiz.c2==None:
				raiz.c2=nombre
			elif raiz.c3==None:
				raiz.c3=nombre
			elif raiz.c4==None:
				raiz.c3=nombre





			
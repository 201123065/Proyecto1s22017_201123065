from nodoB import nodoB
from carpeta import carpeta
class arbolB :
	def __init__(self):
		self.raiz=None
		self.logrado="F"
	def crear(self):
		self.raiz=nodoB(None,None,None,None,None,None,None,None,None)

	def agregar(self,archivo):
		self.raiz = self.recursivo(archivo,self.raiz,None,None)

		(self,p1,c1,p2,c2,p3,c3,p4,c4,p5):

	def recursivo(self,nombre,raiz):
		if raiz.c1==None:
			raiz.c1=nombre
			self.logrado="V"
		elif raiz.c1>nombre:
			if raiz.p1==None:
				if raiz.c2==None:
				elif raiz.c3==None:
					raiz.c3=raiz.c2
				elif raiz.c4==None:
					raiz.c4=raiz.c3
					raiz.c3=raiz.c2
				else:
					izq =nodoB(None,nombre,None,raiz.c1,None,None,None,None,None)
					der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
					raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
					self.logrado="V"
					return raiz
				raiz.c2=raiz.c1
				raiz.c1=nombre

				self.logrado="V"
				return raiz

			else:
				temp = self.recursivo(nombre,raiz.p1)
				if temp.p1!=None:
					if raiz.c2==None:
					elif raiz.c3==None:
						raiz.c3=raiz.c2
						raiz.p4=raiz.p3
					elif raiz.c4==None:
						raiz.c4=raiz.c3
						raiz.c3=raiz.c2
						raiz.p5=raiz.p4
						raiz.p4=raiz.p3
					else:
						izq =nodoB(temp.p1,temp.c1,temp.p2,raiz.c1,raiz.p2,None,None,None,None)
						der =nodoB(raiz.p3,raiz.c3,raiz.p4,raiz.c4,raiz.p5,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
						self.logrado="V"
						return raiz
					raiz.c2=raiz.c1
					raiz.c1=temp.c1
					raiz.p3=raiz.p2
					raiz.p2=temp.p2
					raiz.p1=temp.p1
					self.logrado="V"
					return raiz
		elif raiz.c1<nombre:
			if raiz.p2==None:
				if raiz.c2==None:
					raiz.c2=nombre
					self.logrado="V"
				elif raiz.c2>nombre:
					if raiz.c3==None:
					elif raiz.c4==None:
						raiz.c4=raiz.c3
						raiz.c3
					else:
						izq =nodoB(None,raiz.c1,None,nombre,None,None,None,None,None)
						der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
						raiz=nodoB(izq,raiz.c2,der,None,None,None,None,None,None)
						self.logrado="V"
						return raiz
					raiz.c3=raiz.c2
					raiz.c2=nombre
					self.logrado="V"
					return raiz
				elif raiz.c2<nombre:
					if raiz.p3==None:
						if raiz.c3==None:
							raiz.c3=nombre
							self.logrado="V"
						elif raiz.c3>nombre:
							if raiz.c4==None:
								raiz.c4=raiz.c3
								raiz.c3=nombre
							else:
								izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
								der =nodoB(None,raiz.c3,None,raiz.c4,None,None,None,None,None)
								raiz=nodoB(izq,nombre,der,None,None,None,None,None,None)
							self.logrado="V"
							return raiz
						elif raiz.c3<nombre:
							if raiz.p4==None:
								if raiz.c4==None:
									raiz.c4=nombre
									self.logrado="V"
									return raiz
								elif raiz.c4>nombre:
									izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
									der =nodoB(None,nombre,None,raiz.c4,None,None,None,None,None)
									raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
									self.logrado="V"
									return raiz
								elif raiz.c4<nombre:
									if raiz.p5==None:
										izq =nodoB(None,raiz.c1,None,raiz.c2,None,None,None,None,None)
										der =nodoB(None,raiz.c4,None,nombre,None,None,None,None,None)
										raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
										self.logrado="V"
										return raiz
									else:
										temp = self.recursivo(nombre.self.p5)
										if temp.p1!=None:
											izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
											der =nodoB(raiz.p4,raiz.c4,temp.p1,temp.c1,temp.p2,None,None,None,None)
											raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
											self.logrado="V"
										return raiz

								else:
									self.logrado="F"
									return raiz
							else:
								# raiz.p4!=None
								temp= self.recursivo(nombre,raiz.p4)
								if temp.p1!=None:
									izq =nodoB(raiz.p1,raiz.c1,raiz.p2,raiz.c2,raiz.p3,None,None,None,None)
									der =nodoB(temp.p1,temp.c1,temp.p2,raiz.c4,raiz.c5,None,None,None,None)
									raiz=nodoB(izq,raiz.c3,der,None,None,None,None,None,None)
									self.logrado="V"
								return raiz
						else:
							self.logrado="F"
							return raiz
						return raiz
					else:
						# raiz.p3!=None
				else:
					self.logrado="F"
				return self.raiz
			else:
				# raiz.p2!=None

		else:
			# raiz.c1==nombre
			self.logrado="F"
		return raiz




			
from nodoAVL import nodoAVL

class AVL:
	def __init__(self):
		self.raiz==None

	def agregar(self,nombre,contenido):
		nuevo = nodoAVL(nombre,contenido,0,izq,der)
		if self.raiz==None:
			self.raiz=nuevo
		else:
			self.raiz=self.insertarAVL(nuevo,raiz)


		return retorno

	def obtenerFE(raiz):
		if raiz==None:
			return -1
		else:
			return raiz.fe
	def rotaIzq(raiz):
		aux=raiz.izq
		raiz.izq=raiz.der
		aux.der=raiz
		c.fe=max(self.obtenerFE(raiz.izq),self.obtenerFE(raiz.der))+1
		aux.fe=max(self.obtenerFE(aux.izq),self.obtenerFE(aux.der))+1
		return aux

	def rotaDer(raiz):
		aux=raiz.der
		raiz.der=raiz.izq
		aux.izq=raiz
		c.fe=max(self.obtenerFE(raiz.izq),self.obtenerFE(raiz.der))+1
		aux.fe=max(self.obtenerFE(aux.izq),self.obtenerFE(aux.der))+1
		return aux

	def rotaDIzq(raiz):
		raiz.izq=self.rotaDer(raiz.izq)
		temp=self.rotaIzq(raiz)
		return temp

	def rotaDder(raiz):
		raiz.der=self.rotaIzq(raiz.der)
		temp=self.rotaDer(raiz)
		return temp


	def insertarAVL(nuevo,subAr):
		nuevoPadre=subAr
		if nuevo.nombre<subAr.nombre:
			if subAr.izq==None:
				subAr.izq=nuevo
			else:
				subAr.izq=self.insertarAVL(nuevo,subAr.izq)
				if self.obtenerFE(subAr.izq)-self.obtenerFE(subAr.der)==2:
					if nuevo.nombre<subAr.izq.nombre:
						nuevoPadre=self.rotaIzq(subAr)
					else:
						nuevoPadre=self.rotaDIzq(subAr)
		elif nuevo.nombre>subAr.nombre:
			if subAr.der==None:
				subAr.der=nuevo
			else:
				subAr.izq=self.insertarAVL(nuevo,subAr.der)
				if self.obtenerFE(subAr.der)-self.obtenerFE(subAr.izq)==2:
					if nuevo.nombre>subAr.der.nombre:
						nuevoPadre=rotaDer(subAr)
					else:
						nuevoPadre=self.rotaDder(subAr)
		else:
			print "ya existe"
		if subAr.izq==None and subAr.der!=None:
			subAr.fe=subAr.der.fe+1
		elif subAr.der==None and subAr.izq!=None:
			subAr.fe=subAr.izq.fe+1
		else:
			subAr.fe=max(obtenerFE(subAr.izq),obtenerFE(subAr.der))+1
		return nuevoPadre














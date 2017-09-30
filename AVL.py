from nodoAVL import nodoAVL

class AVL:
	def __init__(self):
		self.raiz==None

	def agregar(self,nombre,contenido):
		hoja = nodoAVL(nombre,contenido,0,None,None)
		retorno=""
		if self.raiz==None:
			self.raiz=hoja
			retorno= "agregado correctamente"
		else:
			retorno=self.setHoja(self.raiz,hoja)

		if "agregado" in retorno:
			self.balancear(self.raiz,0)


		return retorno

	def obtenerFE(raiz):
		if raiz==None:
			return -1
		else:
			return raiz.fe
	def rotaIZQ(raiz):
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


	def setHoja(self,raiz,hoja):

		if raiz.nombre>hoja.nombre:
			if raiz.izq==None:
				raiz.izq=hoja
				return "agregado correctamente"
			else:
				return self.setHoja(raiz.izq,hoja)
		elif raiz.nombre<hoja.nombre:
			if raiz.der==None:
				raiz.der=hoja
				return "agregado correctamente"
			else:
				return self.setHoja(raiz.der,hoja)
		else:
			return "error al agregar"

	def balancear(self,raiz,num):
		izq=0
		der=0

		if raiz.izq!=None:
			izq=self.balancear(raiz.izq,0)
		if raiz.der!=None:
			der=self.balancear(raiz.der,0)





from nodoUsuario import nodoUsuario
import os
class Usuarios():
	def __init__(self):
		self.raiz=None
		self.primero=None

	def crear(self,usuario,passwd):
		hoja = nodoUsuario(usuario,passwd,usuario,None,None)

		if self.raiz==None:
			self.raiz=hoja
			self.primero=hoja
			return "El usuario ha sido creado con exito"
		else:
			return self.comparaHijo(self.raiz,hoja)

	def comparaHijo(self,padre,hoja):
		
		if padre.usuario<hoja.usuario:
			if padre.hijomayor!=None:
				return self.comparaHijo(padre.hijomayor,hoja)
			else:
				padre.hijomayor=hoja
				return "V"
		elif padre.usuario>hoja.usuario:
			if padre.hijomenor!=None:
				return self.comparaHijo(padre.hijomenor,hoja)
			else:
				padre.hijomenor=hoja
				return "V"
		else:
			return "F"

	def verificar(self,usuario,passwd):
		if self.raiz!=None:
			return self.V_o_F(self.raiz,usuario,passwd)
		return "el arbol esta vacio"

	def V_o_F(self,nodo,usuario,passwd):
		if nodo.usuario==usuario and nodo.password==passwd:
			return self.postorden(self.raiz)
		else:
			if nodo.usuario>usuario:
				if nodo.hijomayor!=None:
					return self.V_o_F(nodo.hijomayor,usuario,passwd)
				else:
					return "No se encontro el usuario,menor"
			elif nodo.usuario<usuario:
				if  nodo.hijomenor!=None:
					return self.V_o_F(nodo.hijomenor,usuario,passwd)
				else:
					return "No se encontro el usuario,mayor"
			else:
				return "No se encontro el usuario,fin"


	def postorden(self,visita):
		iz=""
		der=""
		if visita.hijomenor!=None:
			iz= self.postorden(visita.hijomenor)+","
		if visita.hijomayor!=None:
			der = self.postorden(visita.hijomayor)+","

		return iz+der+visita.usuario








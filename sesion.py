from arbolB import arbolB
from nodoUsuarios import nodoUsuarios
class Sesion():
	def __init__(self):
		self.ultimo=None
		self.primero=None

	def crear(self,user,password):
		usuario = nodoUsuarios(user,password,None,None)
		if self.ultimo==None:
			usuario.next=usuario
			usuario.prev=usuario
			self.ultimo=usuario;
			self.primero=usuario;
			return user+" fue creado con exito"
		else:
			if self.ultimo==self.primero:
				if self.ultimo.user==user:
					return "este usuario ya existe"
				else:
					if self.ultimo.user>user:
						usuario.next=self.ultimo.user
						self.ultimo.next=usuario.




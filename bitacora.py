from info import info
class bitacora:
	def __init__(self):
		self.ultimo=None
	def cargar(self,informacion):
		agregar = info(informacion,None)
		if self.ultimo==None:
			self.ultimo=agregar
		else:
			agregar.next=self.ultimo
			self.ultimo=agregar
		return "agregado a la lista"

	def mostrar(self):
		temp = self.ultimo
		cadena="<ul>"
		while temp!=None:
			cadena= cadena+"<li>"+temp.informacion+"</li>"
			temp=temp.next
		return cadena+"</ul>"
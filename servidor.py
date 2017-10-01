from flask import Flask,request

from usuarios import Usuarios
from sesion import Sesion 
from bitacora import bitacora
app = Flask("usuario")

usuario = Usuarios()
sesion = Sesion()
bita = bitacora()

@app.route('/crear_usuario',methods=['POST'])
def crear_usuariol():
	print "crear usuario"
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	ret =sesion.crear(usu,passwd)
	print "hola-"+ret
	bita.cargar(ret)
	return ret

@app.route('/login',methods=['POST'])
def login():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	ret= sesion.login(usu,passwd)
	bita.cargar(ret)
	return ret


@app.route('/listad',methods=['POST'])
def listad():
	url = str(request.form['user'])
	return sesion.mostrarArchivos(url)

@app.route('/add_folder',methods=['POST'])
def add_folder():
	url = str(request.form['url'])
	carpetas = str(request.form['folder'])
	return sesion.setFolder(url,carpetas)

















@app.route('/cargar',methods=['POST'])
def cargar():
	user = str(request.form['user'])
	archivo = str(request.form['arch'])
	ret = sesion.obtener_raiz(user)
	if ret==None:
		return "F"
	else:
		return ret.agregar(archivo)

@app.route('/crear_folder',methods=['POST'])
def crear_folder():
	folder = str(request.form['folder'])
	ruta = str(request.form['ruta'])
	sesion.crear_folder(folder,ruta)
	return "hoa"

@app.route('/carpeta',methods=['POST'])
def carpeta():
	ruta = str(request.form['user'])
	return sesion.obtener_raiz(ruta)






if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
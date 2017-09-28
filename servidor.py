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
	bita.cargar(ret)
	return ret

@app.route('/login',methods=['POST'])
def login():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	ret= sesion.login(usu,passwd)
	bita.cargar(ret)
	return ret

@app.route('/cargar',methods=['POST'])
def cargar():
	ruta = str(request.form['ruta'])
	



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
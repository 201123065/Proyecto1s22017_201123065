from flask import Flask,request

from usuarios import Usuarios
from sesion import Sesion 
app = Flask("usuario")

usuario = Usuarios()
sesion = Sesion()

@app.route('/crear_usuario',methods=['POST'])
def crear_usuariol():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	return sesion.crear(usu,passwd)

@app.route('/prueba')
def prueba():
	ret = "str(request.form['val1'])"
	return sesion.crearCarpeta(ret)

@app.route('/login',methods=['POST'])
def login():
	print "hola"
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	return sesion.login(usu,passwd)



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
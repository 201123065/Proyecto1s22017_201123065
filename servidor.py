from flask import Flask,request

from usuarios import Usuarios
app = Flask("usuario")

usuario = Usuarios()

@app.route('/crear_usuario',methods=['POST'])
def crear_usuariol():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	return usuario.crear(usu,passwd)


@app.route('/login',methods=['POST'])
def login():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	print "logea"
	return usuario.verificar(usu,passwd)



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
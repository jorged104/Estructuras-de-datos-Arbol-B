from flask import Flask, session 
from flask import request
from flask import make_response
import json
import ArbolBinario

import base64
class juego():
	"""docstring for juego"""
	def __init__(self):
		self.usuario1 = None
		self.usuario2 = None
		self.Ausuario1 = None
		self.Ausuario2 = None
		self.x = 0
		self.y = 0
		self.modalidad = 0
		self.tiempoM = 0
		self.tiempoS = 0
		self.disparo = 0
		self.rafagas = 0
		self.dips = 0
		self.turno = None
		self.registro =False
		self.cubo1 = None
		self.cubo2 = None
		self.iniciado = False
usuarios = ArbolBinario.ArbolBinario()
game = juego()

usuarios.insertarPro("Admin","admin","0")

app = Flask(__name__)
@app.route('/setgame',methods=['POST'])
def setgame():
	game.usuario1= str(request.form['usuario1'])
	game.usuario2= str(request.form['usuario2'])
	game.x= str(request.form['x'])
	game.y= str(request.form['y']) 
	game.modalidad= str(request.form['mod'])
	game.tiempoM= str(request.form['minutos'])
	game.tiempoS= str(request.form['segundos'])
	game.disparo= str(request.form['disparo'])
	game.rafagas= str(request.form['rafagas'])
	game.Ausuario1 = usuarios.buscar(game.usuario1,usuarios.raiz)
	game.Ausuario2 = usuarios.buscar(game.usuario2,usuarios.raiz)
	game.iniciado = False
	game.turno = game.usuario1
	game.dips = int(game.rafagas)
	game.registro = False
	return "ok"
@app.route('/login',methods=['POST'])
def login():
	usuario= str(request.form['usuario'])
	pas= str(request.form['contra'])
	nodo = usuarios.buscar(usuario,usuarios.raiz)
	if nodo != None:
		if nodo.usuario == usuario and nodo.pas == pas:
			nodo.on = "1"
			return "True"

		else:
			return "False"
	return "False"
@app.route('/registro',methods=['POST'])
def registro():
	usuario= str(request.form['usuario'])
	pas= str(request.form['contra'])
	usuarios.insertarPro(usuario,pas,0)
	#insertar(usuario,pas,usuarios.raiz)
	return "Registrado =) "	
@app.route('/',methods=['POST'])
def index():
	#empresa= str(request.form['empresa'])
	#departamento= str(request.form['departamento'])
	with open("Arbolito.png", "rb") as image:
		data = image.read()
	encoded_string = base64.b64encode(data)
	return  encoded_string
@app.route('/registroAutomatico',methods=['POST'])
def registroAutomatico():
	usuario= str(request.form['usuario'])
	pas= str(request.form['contra'])
	on = str(request.form['on'])
	usuarios.insertarPro(usuario,pas,0)
	return "Registrado =)"
@app.route('/registroDeJuegos',methods=['POST'])
def registroDeJuegos():
	usuario= str(request.form['usuarioBase'])
	oponente= str(request.form['oponente'])
	TirosR= str(request.form['TirosR'])
	TirosA= str(request.form['TirosA'])
	TirosF= str(request.form['TirosF'])
	Gano= str(request.form['Gano'])	
	TirosRecibidos= str(request.form['TirosRecibidos'])
	usuario = usuarios.buscar(usuario,usuarios.raiz)
	if usuario != None:
		nodo = usuario.lista.insertar(oponente)
		nodo.tirosR = TirosR
		nodo.tirosA = TirosA
		nodo.tirosF = TirosF
		nodo.ganada = Gano
		nodo.dano = TirosRecibidos
		return "ok"
	else:
		return "error"	
@app.route('/InsertarEnMatriz',methods=['POST'])
def InsertarEnMatriz():	
	x = str(request.form['x'])
	y = str(request.form['y'])
	z = str(request.form['z'])
	dato = str(request.form['dato'])
	usuario = str(request.form['usuario'])
	us = usuarios.buscar(usuario,usuarios.raiz)
	if us != None:
		us.cubo.Insertar(int(x),int(y),int(z),dato)
		print( " x : " + x + " y: " + y +"z : "+ z + "dato" + dato)
	return "ok";	
@app.route('/getTabla',methods=['POST'])
def getTabla():	
	x = str(request.form['z'])
	usuario = str(request.form['usuario'])
	us = usuarios.buscar(usuario,usuarios.raiz)
	#separador = str(request.form['separador'])
	try:
		separador = {'1': "avione", '2': "satelite", '0': "barco",'-1':"submarino"}[x]
	except KeyError:
		separador = "barco"
	if us != None:
		return us.cubo.buscarEnZ(int(x),separador)
	return "ok";
@app.route('/enjuego',methods=['POST'])
def enjuego():	
	usuario = str(request.form['usuario'])
	if game.usuario1 != None or game.usuario2 != None:
		if usuario == game.usuario1 or usuario == game.usuario2:
			return  "True"
	return "False"
@app.route('/enturno',methods=['POST'])
def enturno():	
	usuario = str(request.form['usuario'])
	if usuario == game.turno:
		return  "True"
	return "False"
@app.route('/tiro',methods=['POST'])
def tiro():
	usuario = str(request.form['usuario'])
	x = str(request.form['x'])
	y = str(request.form['y'])
	z = str(request.form['z'])
	tirarA = None
	dis = None
	if game.iniciado == False:
		game.iniciado = True
		game.cubo1 = game.Ausuario1.cubo
		game.cubo2 = game.Ausuario2.cubo
	if usuario == game.usuario1:
		tirarA = game.Ausuario2
		dis = game.Ausuario1
		game.dips = game.dips-1
		if ( game.disparo == 1 or game.dips ==0):
			game.turno = game.usuario2
			game.dips = int(game.rafagas)	
	if usuario == game.usuario2:
		tirarA = game.Ausuario1
		dis = game.Ausuario2
		game.dips = game.dips	-1
		if game.disparo	== 1 or game.dips==0:	
			game.turno = game.usuario1
			game.dips = int(game.rafagas)
	if tirarA != None:
		t = tirarA.cubo.tiro(x,y,z)
		if t == True:
			dis.disparosA.Insertar(int(x),int(y),int(z),"boom")

		else:
			dis.disparosF.Insertar(int(x),int(y),int(z),"boom")
			print("********************"+ str(t)+"*****")
		return "Tiro True"
	return "No Funciono"					
@app.route('/getGame',methods=['POST'])
def getGame():
	juego = game.tiempoM+','+game.tiempoS+','+game.modalidad+','+game.disparo+','+game.rafagas+','+game.x+','+game.y
	return juego
@app.route('/cuboNaves',methods=['POST'] )
def cuboNaves():
	usuario = str(request.form['usuario'])
	us = usuarios.buscar(usuario,usuarios.raiz)
	if us != None:
		us.cubo.Graficar(usuario)
		with open("cubos/"+usuario+"MatrizDispersa.png", "rb") as image:
			data = image.read()
		encoded_string = base64.b64encode(data)
		return  encoded_string
	else:
		return "Error Tonto!!"
@app.route('/cuboNavesInicial',methods=['POST'] )
def cuboNavesInicial():
	usuario = str(request.form['usuario'])
	tirarA = None
	dis = None
	res = "False"
	cubito = None
	if usuario == game.usuario1:
		tirarA = game.Ausuario2
		dis = game.Ausuario1
		cubito = game.cubo1
	
	if usuario == game.usuario2:
		tirarA = game.Ausuario1
		dis = game.Ausuario2
		cubito = game.cubo2
	#us = usuarios.buscar(usuario,usuarios.raiz)
	if cubito != None:
		cubito.Graficar(usuario+"Original")
		with open("cubos/"+usuario+"Original"+"MatrizDispersa.png", "rb") as image:
			data = image.read()
		encoded_string = base64.b64encode(data)
		return  encoded_string
	else:
		return "Error Tonto!!"		
@app.route('/cuboTirosF',methods=['POST'] )
def cuboTirosF():
	usuario = str(request.form['usuario'])
	us = usuarios.buscar(usuario,usuarios.raiz)
	if us != None:
		us.disparosF.Graficar(usuario+"DFallados")
		with open("cubos/"+usuario+"DFallados"+"MatrizDispersa.png", "rb") as image:
			data = image.read()
		encoded_string = base64.b64encode(data)
		return  encoded_string
	else:
		return "Error Tonto!!"	
@app.route('/cuboTirosA',methods=['POST'] )
def cuboTirosA():
	usuario = str(request.form['usuario'])
	us = usuarios.buscar(usuario,usuarios.raiz)
	if us != None:
		us.disparosA.Graficar(usuario+"DAcer")
		with open("cubos/"+usuario+"DAcer"+"MatrizDispersa.png", "rb") as image:
			data = image.read()
		encoded_string = base64.b64encode(data)
		return  encoded_string
	else:
		return "Error Tonto!!"	
@app.route('/getusuarios',methods=['POST'] )
def getusuarios():
	usuarios.graficar()
	with open("Arbolito.png", "rb") as image:
		data = image.read()
	encoded_string = base64.b64encode(data)
	return  encoded_string
@app.route('/getespejo',methods=['POST'] )
def getespejo():
	usuarios.graficarespejo()
	with open("ArbolEspejo.png", "rb") as image:
		data = image.read()
	encoded_string = base64.b64encode(data)
	return  encoded_string	
@app.route('/getEstadisticas',methods=['POST'] )
def getEstadisticas():
	usuarios.estadistica()
	return  json.dumps({'altura':str(usuarios.altura),'nivel':str(usuarios.nivel),'hojas':str(usuarios.hojas),'NodosRamas':str(usuarios.noditos)})		
	#json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
@app.route('/gane',methods=['POST'] )
def gane():
	usuario = str(request.form['usuario'])
	tirarA = None
	dis = None
	res = "False"
	if usuario == game.usuario1:
		tirarA = game.Ausuario2
		dis = game.Ausuario1
	
	if usuario == game.usuario2:
		tirarA = game.Ausuario1
		dis = game.Ausuario2
	
	if tirarA != None:
		res = tirarA.cubo.perdi()
		if res == "True":
			if game.registro == False:
				nodo = tirarA.lista.insertar(dis.usuario)
				nodo.tirosR = 0
				nodo.tirosA = 0
				nodo.tirosF = 0
				nodo.ganada = tirarA.usuario
				nodo.dano = 0
				nodo = dis.lista.insertar(tirarA.usuario)
				nodo.tirosR = 0
				nodo.tirosA = 0
				nodo.tirosF = 0
				nodo.ganada = dis.usuario
				nodo.dano = 0
				game.registro = True
		return res
    
	return "No Funciono"
@app.route('/listausuarios',methods=['POST'] )
def listausuarios():
	res = usuarios.listarUsuarios()
	return str(res)	
@app.route('/eliminarus',methods=['POST'] )
def eliminarus():
	usuario = str(request.form['usuario'])
	usuarios.eli(usuario)
	return "ok"	
@app.route('/editarus',methods=['POST'] )
def editarus():
	usuario = str(request.form['usuario'])
	contra = str(request.form['contra'])
	usuarios.editar(usuario,contra,False,usuarios.raiz)
	return "ok"				
#*****************------------------------METODOS GET ---------------------------------------*************-
@app.route('/graficarArbolUsuario')
def graficarArbolUsuario():
	usuarios.graficar()
	return "okis"

@app.route('/getjuego')
def getjuego():
	#usuarios.graficar()
	return game.usuario1 + " Vs " + game.usuario2 + "x :" + str(game.x) + "y: " + str(game.y) + "Tiempo: " + str(game.tiempoM)+":"+str(game.tiempoS)  + "Modalidad " + str(game.modalidad) + "disparo " + str(game.disparo) + "Rafaga " + str(game.rafagas) 
@app.route('/getcubousuario')
def getcubousuario():
	us = usuarios.buscar("Mord86",usuarios.raiz)
	if us != None:
		us.cubo.Graficar("Mord")
		return "ok"
	else:
		return "Error Tonto!!"
@app.route('/buscarSatelite', methods=['GET'])
def buscarSatelite():
	z = request.args.get('z')
	us = usuarios.buscar("Mord86",usuarios.raiz)
	if us != None:
		print (us.cubo.buscarEnZ(int(z)))
		return "ok"
	else:
		return "Error Tonto!!"			
app.secret_key = 'clave'
if __name__ == '__main__':
	app.run(debug = True )
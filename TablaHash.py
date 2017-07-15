class Nodo():
	def __init__(self):
		self.cont = []
	def addContenedor(self,usuario,id):
		con = contenedor(usuario,id)
		self.cont.append(con)
	def addContenedor(self,contenedor):
		self.cont.append(contenedor)		
class contenedor():
	def __init__(self,usuario,id):
		self.bandera = False
		self.id = id
		self.usuario = usuario
class TablaHash():
	def __init__(self):
		self.n = 0
		self.tabla = []
		self.factor = 0
		self.tam = 0
	def creartabla(self,tam):
		self.tam = tam
		i = 0
		while i < tam :
			self.tabla.append("Vacio")
	def Fhash(self,dato):
		acumulado = 0
		for Caracter in enumerate(Cadena):
			print (" " + Caracter[1], ord(Caracter[1]))
			acumulado =	acumulado + ord(Caracter[1])
		res = acumulado * acumulado
		i = int(len(res)/2)
		retorno = int(res[i]) + int(res[i+1])
		print( str(res) + " y el hash seria " + str(retorno))

	
a = TablaHash()
a.Fhash("jorge")		
       
				
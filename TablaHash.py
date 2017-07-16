from graphviz import Digraph
class Nodo():
	def __init__(self):
		self.cont = []
	def addContenedor(self,usuario):
		con = contenedor(usuario)
		self.cont.append(con)
			
class contenedor():
	def __init__(self,usuario):
		self.bandera = False
		self.usuario = usuario
class TablaHash():
	def __init__(self,n):
		self.n = 0
		self.tabla = []
		self.factor = 0
		self.tam = 0
		self.creartabla(n)
	def creartabla(self,tam):
		self.tam = tam
		i = 0
		while i < tam :
			self.tabla.append(Nodo())
			i = i +1
	def Fhash(self,dato):
		acumulado = 0
		for Caracter in enumerate(dato):
			acumulado =	acumulado + ord(Caracter[1])
		res = acumulado * acumulado
		i = int(len(str(res))/2)
		res = str(res)
		retorno = int(res[i-1]) + int(res[i])
		return retorno
		#print( str(res) + " y el hash seria " + str(retorno))
	def insertar(self,usuario):
		res = self.Fhash(usuario)
		self.tabla[res].addContenedor(usuario)
		self.n = self.n + 1
		if ( self.n/self.tam ) >  0.6:
			print("Rehasheando XD ")
			self.rehash()
	def rehash(self):
		temp = self.tabla
		self.tabla = []
		m = int(self.n / 0.30)
		self.n = 0
		self.tam = m
		self.creartabla(m)
		i = 0
		while i < len(temp):
			j = 0
			while j < len(temp[i].cont):
				if temp[i].cont[j].bandera == False:
					self.insertar(temp[i].cont[j].usuario)
				j = j +1
			i = i +1
						
	def graficar(self):
		dot = Digraph(node_attr={'shape': 'record'})
		i = 0
		st = ""
		while i < len(self.tabla):
			if len(self.tabla[i].cont) > 0:
				if self.tabla[i].cont[0].bandera == False:
					if i == len(self.tabla)-1:
						st = st +"<" +str(i)+"N"+"0" +"> "+str(i) +"."+str(self.tabla[i].cont[0].usuario)
					else:	
						st = st +"<" +str(i)+"N"+"0" +"> "+str(i) +"."+str(self.tabla[i].cont[0].usuario) + " |"
					
					if  len(self.tabla[i].cont) > 1:
						j = 1
						while( j < len(self.tabla[i].cont)):
							if self.tabla[i].cont[j].bandera == False:
								dot.node(str(i)+"N"+str(j),str(self.tabla[i].cont[j].usuario))
								if  j+1  <= len(self.tabla[i].cont)-1:
									dot.edge(str(i)+"N"+str(j),str(i)+"N"+str(j+1) )
							j = j +1
						dot.edge("tabla:"+str(i)+"N"+"0",str(i)+"N"+str(1))
				else:
					st = st +"<" +str(i)+"N"+"0" +"> "+str(i) +"."+str("Vacio") + " |"				
			else:
				st = st +"<" +str(i)+"N"+"0" +"> "+str(i) +"."+str("Vacio") + " |"		
			i = i +1
		dot.node("tabla",st)
		dot.format = 'png'
		dot.render("hashprro")		



	
  
				
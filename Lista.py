from graphviz import Digraph
import json
class Nodo():
	"""docstring for Nodo"""
	def __init__(self,oponente):
		self.nombre = None
		self.oponente = oponente
		self.tirosR = None
		self.tirosA = None
		self.tirosF = None
		self.ganada = False
		self.dano = False
		self.siguiente = None
		self.anterior = None
class Lista():
	def __init__(self):
		self.cabeza = None
		self.nombre = None
	def insertar(self,oponente):
		nuevo = Nodo(oponente)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			temp = self.cabeza
			while temp != None:
				if temp.siguiente == None:
					temp.siguiente = nuevo
					nuevo.anterior = temp 
					break
				else:
					temp = temp.siguiente
		return nuevo
	def buscarporEnemigo(self,oponente):
		temp = self.cabeza
		while temp != None:
			if temp.oponente == oponente:
				return   json.dumps({'nombre':str(temp.nombre),'oponente':str(temp.oponente),'Realizados':str(temp.tirosR),'Acertados':str(temp.tirosA),'Fallados':str(temp.tirosF),'ganada':str(temp.ganada),'Re':str(temp.dano)})	
			temp = temp.siguiente
		return " "				
	def listarEnemgos(self):
		temp = self.cabeza
		res = ""
		while temp != None:
			if temp.siguiente == None:
				res = res + temp.oponente
			else:
				res = res  + temp.oponente + ","
			temp = temp.siguiente
		return res 	
	def imprimir(self):
		temp = self.cabeza
		while temp != None:
			print(str(temp.oponente) + " XD ")
			temp = temp.siguiente
	def graficar(self,dot):
		#dot = Digraph()
		nodo = self.cabeza
		while nodo != None:	
			dot.node(str(nodo.oponente+"N#"+self.nombre),str(nodo.oponente)+" R: "+str(nodo.tirosR) + " A: " + str(nodo.tirosA) + " F: " + str(nodo.tirosF) + " G " +str(nodo.ganada) + " Re " + str(nodo.dano))
			if nodo.siguiente != None:
				dot.edge(str(nodo.oponente+"N#"+self.nombre),str(nodo.siguiente.oponente+"N#"+self.nombre))
			if nodo.anterior != None:
				dot.edge(str(nodo.oponente+"N#"+self.nombre),str(nodo.anterior.oponente+"N#"+self.nombre))
			nodo = nodo.siguiente		
		#dot.format = 'png' 
		#dot.render("Lista")
#caren = Lista()
#caren.nombre = "Caren"
#caren.insertar("Pablo")
#caren.insertar("Daniela")
#caren.insertar("valeria")
#caren.insertar("silvana")
#caren.insertar("meli")
#dot = Digraph()
#caren.graficar(dot)	
#dot.format = 'png'
#dot.render("Lista")				


	
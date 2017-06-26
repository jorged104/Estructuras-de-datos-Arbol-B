from graphviz import Digraph
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
	def imprimir(self):
		temp = self.cabeza
		while temp != None:
			print(str(temp.oponente) + " XD ")
			temp = temp.siguiente
	def graficar(self,dot):
		#dot = Digraph()
		nodo = self.cabeza
		while nodo != None:	
			dot.node(str(nodo.oponente+"N#"+self.nombre),str(nodo.oponente))
			if nodo.siguiente != None:
				dot.edge(str(nodo.oponente+"N#"+self.nombre),str(nodo.siguiente.oponente+"N#"+self.nombre))
			if nodo.anterior != None:
				dot.edge(str(nodo.oponente+"N#"+self.nombre),str(nodo.anterior.oponente+"N#"+self.nombre))
			nodo = nodo.siguiente		
		#dot.format = 'png' 
		#dot.render("Lista")
caren = Lista()
caren.nombre = "Caren"
caren.insertar("Pablo")
caren.insertar("Daniela")
caren.insertar("valeria")
caren.insertar("silvana")
caren.insertar("meliGuapisisisadm")
dot = Digraph()
caren.graficar(dot)	
dot.format = 'png'
dot.render("Lista")				

		
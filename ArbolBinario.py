from graphviz import Digraph
import Lista
class 	Nodo():
	"""docstring for 	Nodo"""
	def __init__(self, usuario,pas):
		self.usuario = usuario	
		self.pas = pas
		self.on = False
		self.lista	 = Lista.Lista()
		self.lista.nombre = "L#"+usuario
		self.cubo = None
		self.derecha = None
		self.izquierda = None
 
class 	ArbolBinario():
	def __init__(self):
		self.raiz = None
		self.altura = 0 
		self.nivel = 0 
		self.hojas = 0
		self.noditos = 0
	def insertar(self,usuario,pas,nodo):
		if self.raiz == None:
			self.raiz = Nodo(usuario,pas)
		else:	
			if  usuario > nodo.usuario: 						
				if nodo.derecha	== None:	
					nodo.derecha = Nodo(usuario,pas)
				else:	
					self.insertar(usuario,pas,nodo.derecha)						
			else:
				if nodo.izquierda == None:
					nodo.izquierda = Nodo(usuario,pas)
				else:
					self.insertar(usuario,pas,nodo.izquierda)
	def imprimir(self,nodo,dot):
		if nodo != None:
			#print( str(nodo.usuario))
			dot.node(str(nodo.usuario),str(nodo.usuario)+" "+str(nodo.pas))
			nodo.lista.graficar(dot)
			if nodo.lista.cabeza != None:
				dot.edge(str(nodo.usuario),str(nodo.lista.cabeza.oponente+"N#"+nodo.lista.nombre))
		else:
			return None	
		if nodo.izquierda != None:
			self.imprimir(nodo.izquierda,dot)
			dot.edge(str(nodo.usuario),str(nodo.izquierda.usuario))					
		if nodo.derecha	 != None:
			dot.edge(str(nodo.usuario),str(nodo.derecha.usuario))
			self.imprimir(nodo.derecha,dot)
	def espejo(self,nodo,dot):
		if nodo != None:
			dot.node(str(nodo.usuario),str(nodo.usuario)+" "+str(nodo.pas))
			nodo.lista.graficar(dot)
		else:
			return None	
		if nodo.derecha	 != None:
			dot.edge(str(nodo.usuario),str(nodo.derecha.usuario))
			self.imprimir(nodo.derecha,dot)	
		if nodo.izquierda != None:
			self.imprimir(nodo.izquierda,dot)
			dot.edge(str(nodo.usuario),str(nodo.izquierda.usuario))					

	def editar(self,usuario,pas,on,nodo):
		if nodo != None:
			if nodo.usuario == usuario:
				nodo.pas = pas 
				nodo.on = on
				return None
		else:
			return None
		if  usuario > nodo.usuario: 						
			if nodo.derecha	== None:	
				return None
			else:	
				self.editar(usuario,pas,on,nodo.derecha)						
		else:
			if nodo.izquierda == None:
				return None
			else:
				self.editar(usuario,pas,on,nodo.izquierda)
	def graficar(self):
		dot = Digraph()
		self.imprimir(self.raiz,dot)
		dot.format = 'png' 
		dot.render("Arbolito")
	def graficarespejo(self):
		dot = Digraph()
		self.espejo(self.raiz,dot)
		dot.format = 'png'
		dot.render("ArbolEspejo")
	def max(self,num1,num2):
		if num1 >= num2:
			return num1
		else:
			return num2	
	def ContarNodos(self,nodo):
		
		if nodo != None :
			if nodo.derecha == None and nodo.izquierda == None:
				self.hojas = self.hojas + 1
			else:
				self.noditos = self.noditos + 1	
		else:
			return None
		self.ContarNodos(nodo.derecha)
		self.ContarNodos(nodo.izquierda)
	def alto(self,nodo):
		if nodo == None:
			return 0
		else:
			return 1 + self.max(self.alto(nodo.derecha),self.alto(nodo.izquierda))		


	def estadistica(self):
		self.altura = 0 
		self.nivel = 0 
		self.hojas = 0
		self.noditos = 0
		self.ContarNodos(self.raiz)
		self.altura = self.alto(self.raiz)
		self.nivel = self.altura - 1
	def eliminar(self,usuario,nodo):
		if nodo != None:
			if nodo == self.raiz:
				if self.raiz.usuario == usuario:
					eliminado = self.raiz
					encontre = self.maspequeDerecha(nodo.derecha)
					if encontre == None:
						encontre = self.maspequeIzquierda(nodo.izquierda)
					if encontre != None:
						self.eliminarPunteroAnterior(self.raiz,encontre)
						if eliminado != encontre:	
							self.raiz= encontre
							self.raiz.derecha = eliminado.derecha
							self.raiz.izquierda = eliminado.izquierda	
					else:
						self.raiz = None

					#print("Nodo a la derecha + " + nodo.derecha.usuario )
					#print("Eliminado el nodo : " + eliminado.usuario + "Y encontre " + encontre.usuario)
			if nodo.derecha != None:
				if nodo.derecha.usuario == usuario:
					print("En derecah")
					eliminado = nodo.derecha
					encontre = self.maspequeDerecha(nodo.derecha)
					if encontre == None:
						encontre = self.maspequeIzquierda(nodo.izquierda)
					if encontre != None:
						self.eliminarPunteroAnterior(self.raiz,encontre)
					if eliminado != encontre:
						nodo.derecha = encontre
						nodo.derecha.derecha = eliminado.derecha
						nodo.derecha.izquierda = eliminado.izquierda
					else:
						nodo.derecha = None
					#print("Eliminado el nodo : " + eliminado.usuario + "Y encontre " + encontre.usuario)					
			if nodo.izquierda != None:
				if nodo.izquierda.usuario == usuario:
					eliminado = nodo.izquierda
					encontre = 	self.maspequeDerecha(nodo.derecha)
					if encontre == None:
						encontre = self.maspequeIzquierda(nodo.izquierda)
					if encontre != None:
						self.eliminarPunteroAnterior(self.raiz,encontre)
					if eliminado != encontre:
						nodo.izquierda = encontre
						nodo.izquierda.derecha = eliminado.derecha
						nodo.izquierda.izquierda = eliminado.izquierda
					else:
						nodo.izquierda = None
					#print("Eliminado el nodo : " + eliminado.usuario + "Y encontre " + encontre.usuario)
		else:
			return None
		if  usuario > nodo.usuario: 						
			if nodo.derecha	== None:	
				return None
			else:	
				self.eliminar(usuario,nodo.derecha)						
		else:
			if nodo.izquierda == None:
				return None
			else:
				self.eliminar(usuario,nodo.izquierda)
	def maspequeDerecha(self,nodo):
		if nodo != None:
			derecho = self.maspequeDerecha(nodo.derecha)
			izquierdo = self.maspequeDerecha(nodo.izquierda)
			if derecho != None and derecho.usuario < nodo.usuario:
				return derecho			
			if izquierdo != None:
				return izquierdo
			if izquierdo == None and derecho != None:
				return derecho 		
			return nodo
		else: 
			return None
	def maspequeIzquierda(self,nodo):
		if nodo != None:
			derecho = self.maspequeIzquierda(nodo.derecha)
			izquierdo = self.maspequeIzquierda(nodo.izquierda)
			if izquierdo != None and izquierdo.usuario > nodo.usuario:
				return izquierdo
			if derecho != None:
				return derecho
			return nodo						
	def eliminarPunteroAnterior(self,nodo,eliminar):
		if nodo != None:
			if nodo.derecha != None:
				if nodo.derecha == eliminar:
					nodo.derecha = None
			if nodo.izquierda != None:
				if nodo.izquierda == eliminar:
					nodo.izquierda = None
		else:
			return None
		if  eliminar.usuario > nodo.usuario: 						
			if nodo.derecha	== None:	
				return None
			else:	
				self.eliminarPunteroAnterior(nodo.derecha,eliminar)						
		else:
			if nodo.izquierda == None:
				return None
			else:
				self.eliminarPunteroAnterior(nodo.izquierda,eliminar)			
	
	def buscar(self,usuario,nodo):
		if nodo != None:
			if nodo.usuario == usuario:
				return nodo
		if usuario > nodo.usuario:
			if nodo.derecha == None:
				return None
			else:
				return self.buscar(usuario,nodo.derecha)
		else:
			if nodo.izquierda == None:
				return None
			else:
				return self.buscar(usuario,nodo.izquierda)				


ArbolNavideno = ArbolBinario()
ArbolNavideno.insertar("f","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("d","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("x","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("a","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("e","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("g","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("z","saber",ArbolNavideno.raiz)
#ArbolNavideno.insertar("z2","saber",ArbolNavideno.raiz)
ArbolNavideno.editar("a","perro2",True,ArbolNavideno.raiz)

usuario = ArbolNavideno.buscar("g",ArbolNavideno.raiz)
usuario.lista.insertar("Listadeg")
usuario.lista.insertar("Listadeg2")
usuario.lista.insertar("Listadeg3")
usuario.lista.insertar("Listadeg4")
usuario = ArbolNavideno.buscar("f",ArbolNavideno.raiz)
usuario.lista.insertar("ListadeF")
usuario.lista.insertar("ListadeF2")
usuario.lista.insertar("ListadeF3")
usuario.lista.insertar("ListadeF4")
ArbolNavideno.graficar()
#ArbolNavideno.graficarespejo()
ArbolNavideno.estadistica()
print("Hojas :" + str(ArbolNavideno.hojas) + "Nodos :" + str(ArbolNavideno.noditos) + "Altura : " + str(ArbolNavideno.altura)+ "Nivel : " + str(ArbolNavideno.nivel))


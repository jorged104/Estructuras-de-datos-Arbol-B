from graphviz import Digraph
import Lista
import MatrizDispersa
class 	Nodo():
	"""docstring for 	Nodo"""
	def __init__(self, usuario,pas):
		self.usuario = usuario	
		self.pas = pas
		self.on = False
		self.lista	 = Lista.Lista()
		self.lista.nombre = "L#"+usuario
		self.cubo = MatrizDispersa.Matriz()
		self.disparosA = MatrizDispersa.Matriz()
		self.disparosF = MatrizDispersa.Matriz()
		self.derecha = None
		self.izquierda = None
 
class 	ArbolBinario():
	def __init__(self):
		self.raiz = None
		self.altura = 0 
		self.nivel = 0 
		self.hojas = 0
		self.noditos = 0
		self.listaNodos = ""
		self.espejo = None
	def insertar(self,usuario,pas,nodo,insert):
		if self.raiz == None:
			self.raiz = insert
		else:	
			if  usuario > nodo.usuario: 						
				if nodo.derecha	== None:	
					nodo.derecha = insert
				else:	
					self.insertar(usuario,pas,nodo.derecha,insert)						
			else:
				if nodo.izquierda == None:
					nodo.izquierda = insert
				else:
					self.insertar(usuario,pas,nodo.izquierda,insert)
	def insertarEspejo(self,usuario,nodo,insert):
		if self.raiz == None:
			self.raiz = insert
		else:	
			if  usuario < nodo.usuario: 						
				if nodo.derecha	== None:	
					nodo.derecha = insert
				else:	
					self.insertarEspejo(usuario,nodo.derecha,insert)						
			else:
				if nodo.izquierda == None:
					nodo.izquierda = insert
				else:
					self.insertarEspejo(usuario,nodo.izquierda,insert)			
	def imprimir(self,nodo,dot):
		if nodo != None:
			#print( str(nodo.usuario))
			dot.node(str(nodo.usuario),str(nodo.usuario)+" , "+str(nodo.pas) + " , " + str(nodo.on) )
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
		return None
	def hacerespejo(self,nodo,espejito):
		if nodo != None:
			nuevo = Nodo(nodo.usuario,nodo.pas)
			espejito.insertarEspejo(nodo.usuario,espejito.raiz,nuevo)
		else:
			return None	
		if nodo.izquierda != None:
			self.hacerespejo(nodo.izquierda,espejito)
		if nodo.derecha	 != None:
			self.hacerespejo(nodo.derecha,espejito)
	def graficarespejo(self):
		espejito = ArbolBinario()
		self.hacerespejo(self.raiz,espejito)
		dot = Digraph()
		espejito.imprimir(espejito.raiz,dot)
		dot.format = 'png'
		dot.render("ArbolEspejo")
		return None
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
	def insertarPro(self,usuario,pas,on):
		nuevo = Nodo(usuario,pas)
		nuevo.on = on
		self.insertar(usuario,pas,self.raiz,nuevo)
		#elf.insertar(usuario,pas,nodo.derecha,insert)
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
	def maxi(self,nodo):
		if (nodo.derecha == None):
			return nodo
		else:
			return self.maxi(nodo.derecha)
	def maximo(self):
		if self.raiz == None:
			return None
		return self.maxi(self.raiz)
	
	def subIz(self):
		arbol = ArbolBinario()
		arbol.raiz = self.raiz.izquierda
		return arbol
	def subDer(self):
		arbol = ArbolBinario()
		arbol.raiz = self.raiz.derecha
		return arbol				
	def eli(self,val):
		if self.raiz == None:
			return None
		if self.raiz.usuario == val:
			if self.raiz.izquierda == None:
				self.raiz = self.raiz.derecha
			else:
				if self.raiz.derecha == None:
					self.raiz = self.raiz.izquierda
				else:
					h = self.subDer()	
					self.raiz = self.raiz.izquierda
					maxi = self.maximo()
					maxi.derecha = h.raiz 
		else:
			if self.raiz.usuario > val:
				hIzq = self.subIz();
				hIzq.eli(val)
				self.raiz.izquierda = hIzq.raiz
			else:
				hDer = self.subDer()
				hDer.eli(val)
				self.raiz.derecha = hDer.raiz	

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
	def listar(self,nodo):
		if nodo != None:
			self.listaNodos	 = self.listaNodos	+ ","+nodo.usuario
		else:
			return None
		if nodo.derecha	 != None:
			self.listar(nodo.derecha)
		if nodo.izquierda != None:
			self.listar(nodo.izquierda)			
	def listarUsuarios(self):
		self.listaNodos	 = ""
		self.listar(self.raiz)
		return self.listaNodos	
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


#ArbolNavideno = ArbolBinario()

#ArbolNavideno.insertarPro("f","saber",0)
#ArbolNavideno.insertarPro("d","saber",0)
#ArbolNavideno.insertarPro("x","saber",0)
#ArbolNavideno.insertarPro("a","saber",0)
#ArbolNavideno.insertarPro("e","saber",0)
#ArbolNavideno.insertarPro("g","saber",0)
#ArbolNavideno.insertarPro("z","saber",0)
#ArbolNavideno.insertarPro("z2","saber",0)
#ArbolNavideno.graficarespejo()
#ArbolNavideno.eli("f")
#ArbolNavideno.graficar()

#ArbolNavideno.editar("a","perro2",True,ArbolNavideno.raiz)

#usuario = ArbolNavideno.buscar("g",ArbolNavideno.raiz)
#usuario.lista.insertar("Listadeg")
#usuario.lista.insertar("Listadeg2")
#usuario.lista.insertar("Listadeg3")
#usuario.lista.insertar("Listadeg4")
#usuario = ArbolNavideno.buscar("f",ArbolNavideno.raiz)
#usuario.lista.insertar("ListadeF")
#usuario.lista.insertar("ListadeF2")
#usuario.lista.insertar("ListadeF3")
#usuario.lista.insertar("ListadeF4")
#ArbolNavideno.graficar()
#ArbolNavideno.graficarespejo()
#ArbolNavideno.estadistica()
#print("Hojas :" + str(ArbolNavideno.hojas) + "Nodos :" + str(ArbolNavideno.noditos) + "Altura : " + str(ArbolNavideno.altura)+ "Nivel : " + str(ArbolNavideno.nivel))


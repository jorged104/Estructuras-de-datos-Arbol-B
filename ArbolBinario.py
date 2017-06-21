class 	Nodo():
	"""docstring for 	Nodo"""
	def __init__(self, usuario,pas):
		self.usuario = usuario	
		self.pas = pas
		self.on = False
		self.lista	 = None
		self.derecha = None
		self.izquierda = None
class 	ArbolBinario():
	def __init__(self):
		self.raiz = None
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
	def imprimir(self,nodo):
		if nodo != None:
			print( str(nodo.usuario))
		else:
			return None	
		if nodo.derecha	 != None:
			self.imprimir(nodo.derecha)
		if nodo.izquierda != None:
			self.imprimir(nodo.izquierda)		

ArbolNavideno = ArbolBinario()
ArbolNavideno.insertar("c","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("a","saber",ArbolNavideno.raiz)
ArbolNavideno.insertar("c","saber",ArbolNavideno.raiz)
ArbolNavideno.imprimir(ArbolNavideno.raiz)
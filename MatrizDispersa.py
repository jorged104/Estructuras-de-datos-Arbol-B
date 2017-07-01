from graphviz import Digraph
class Nodo():
	#Nodo de una Matriz dispersa
	def __init__(self,data):
		self.dato = data
		self.x = 0
		self.y = 0
		self.z = 0
		self.derecha = None
		self.izquierda = None
		self.arriba = None
		self.abajo = None
		self.frente = None
		self.atras = None
		self.disparo = 0
#-------------------------------MATRIS DISPERSA ----------------------------------
class Matriz():
	"""docstring for matriz"""
	def __init__(self):
		self.cabeza = Nodo(None)
								
	#------------------------Busquedas en cabezeras
	def BuscarX(self,x):
		nodotemp = self.cabeza
		while nodotemp != None:
			if nodotemp.x == x:
				return nodotemp
			nodotemp = nodotemp.derecha
	
	def BuscarY(self,y):
		nodotemp = self.cabeza
		while nodotemp != None:
			if nodotemp.y == y:
				return nodotemp
			nodotemp = nodotemp.abajo			
	#METODO Insertar-------------------------------------------------------------------
	def Insertar(self,x,y,z,data):
		nuevoz = Nodo(data)
		if z == 0:
			nuevo = Nodo(data)
		else:
			nuevo = Nodo("Null")
			nuevoz.x = x 
			nuevoz.y = y 
			nuevoz.z = z 	
		busqueda = self.Buscar(x,y,z)
		if busqueda == None:
			nuevo.x = x
			nuevo.y = y
			cabezeraX = self.BuscarX(x)
			cabezeraY = self.BuscarY(y)
			# Si no existen las cabezeras se crean 

			if cabezeraX == None:  # Cabezera en x 
				
				buscador = self.cabeza
				cabezeraX = Nodo(x)
				cabezeraX.x = x
				cabezeraX.y = 0
				while int(buscador.x)  < int(x) and buscador.derecha != None :
					if buscador.derecha.x < x:
						buscador = buscador.derecha
					else:
						break	
				
				if buscador.derecha != None:   #Si la cabezara va en medio 				
					buscador.derecha.izquierda = cabezeraX
					cabezeraX.derecha = buscador.derecha

				buscador.derecha = cabezeraX
				cabezeraX.izquierda = buscador
			
			if cabezeraY == None: # Cabezera en y 
				buscador = self.cabeza
				cabezeraY = Nodo(y)
				cabezeraY.y = y
				cabezeraY.x = 0
				while buscador.y < y and buscador.abajo != None :
					if buscador.abajo.y < y: 
						buscador = buscador.abajo
					else:
						break	
				if buscador.abajo != None:		
					buscador.abajo.arriba = cabezeraY
					cabezeraY.abajo = buscador.abajo
				buscador.abajo = cabezeraY
				cabezeraY.arriba = buscador	
			# Casos de Insercion
			#Busqueda de nodoanterior
			while cabezeraX.y < y and cabezeraX.abajo != None:
					if cabezeraX.abajo.y < y: 
						cabezeraX = cabezeraX.abajo
					else:
						break	
			while cabezeraY.x < x and cabezeraY.derecha != None:
					if cabezeraY.derecha.x < x:
						cabezeraY = cabezeraY.derecha
					else:
						break	
			#Caso insercion en medio
			if cabezeraX.abajo != None:
				cabezeraX.abajo.arriba = nuevo
				nuevo.abajo = cabezeraX.abajo
			if cabezeraY.derecha != None:
				cabezeraY.derecha.izquierda = nuevo 
				nuevo.derecha = cabezeraY.derecha
			cabezeraX.abajo = nuevo
			nuevo.arriba = cabezeraX
			cabezeraY.derecha = nuevo
			nuevo.izquierda = cabezeraY
			busqueda = nuevo
			#Comprobar busquedas en Z =) 
		if busqueda.dato == "Null" and z==0:
			busqueda.dato = data
		busqueda2 = self.busquedaFull(x,y,z)
		if busqueda2 == None : 
			if z > 0:
				profundidad = busqueda
				while profundidad.z < z and profundidad.frente != None:
					if profundidad.frente.z < z:
						profundidad = profundidad.frente
					else:
						break
				if profundidad.frente != None:
					profundidad.frente.atras = nuevoz
					nuevoz.frente = profundidad.frente
				profundidad.frente = nuevoz
				nuevoz.atras = profundidad

			if z < 0 :
				profundidad = busqueda
				while profundidad.z > z and profundidad.atras != None:
					if profundidad.atras.z > z :
						profundidad = profundidad.atras
					else:
						break
				if profundidad.atras != None:
					profundidad.atras.frente = nuevoz
					nuevoz.atras = profundidad.atras
				profundidad.atras = nuevoz
				nuevoz.frente = profundidad	



	# Imprimir En planp -------------------------------------------------------
	def Imprimir(self):
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:		 
				print("Estoy en el nodo y : " + str(auxt.y) + " x: " + str(auxt.x) + "Con :" + str(auxt.dato))
				auxt = auxt.derecha
			aux = aux.abajo
	def Buscar(self,x,y,z):
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:
				if ( auxt.x == x and auxt.y == y):
					return auxt
				auxt = auxt.derecha
			aux = aux.abajo 
	def Graficar(self,nombre):
		dot = Digraph()		
		aux = self.cabeza
		
		while aux != None:
			auxt = aux
			rank = "{ rank = same; "	
			while auxt != None:
				#dot.attr("graph",style='filled')
				aux3 = auxt 
				dot.node(str(self.GetNombre(auxt)),str(auxt.dato)+","+str(auxt.disparo))
				while aux3 != None:
					dot.node(str(self.GetNombre(aux3)),str(aux3.dato)+","+str(auxt.disparo))
					if aux3.frente != None:
						dot.edge(str(self.GetNombre(aux3)),str(self.GetNombre(aux3.frente)))
					if aux3.atras != None:
						dot.edge(str(self.GetNombre(aux3)),str(self.GetNombre(aux3.atras)))	
					aux3 = aux3.frente
				aux3 = auxt.atras
				while aux3 != None:
					dot.node(str(self.GetNombre(aux3)),str(aux3.dato)+","+str(auxt.disparo))
					if aux3.frente != None:
						dot.edge(str(self.GetNombre(aux3)),str(self.GetNombre(aux3.frente)))
					if aux3.atras != None:
						dot.edge(str(self.GetNombre(aux3)),str(self.GetNombre(aux3.atras)))	
					aux3 = aux3.atras					
				if auxt.derecha != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.derecha)))
				if auxt.izquierda != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.izquierda)))
				if auxt.arriba != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.arriba)))
				if auxt.abajo != None:
					dot.edge(str(self.GetNombre(auxt)),str(self.GetNombre(auxt.abajo)))			
				rank = rank + " "+str(self.GetNombre(auxt))
				auxt = auxt.derecha
			rank = rank + "}"
			dot.body.append(rank)
			aux = aux.abajo 
		dot.format = 'png' 
		dot.render('cubos/'+nombre+'MatrizDispersa')	
		#print ( dot.source)			
	def GetNombre(sef,nodo):
		nombre = str("X"+str(nodo.x)+"Y"+str(nodo.y)+"Z"+str(nodo.z))
		return nombre
	def busquedaFull(self,x,y,z):
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:
				if ( auxt.x == x and auxt.y == y):
					if auxt.z == z:
						return auxt
					else:
						tempz = auxt
						while tempz != None:
							if tempz.z == z:
								return tempz
							tempz = tempz.frente
						tempz = auxt
						while tempz != None:
							if tempz.z == z :
								return tempz
							tempz = tempz.atras				
				auxt = auxt.derecha
			aux = aux.abajo 
		return None		
	def buscarEnZ(self,z,sepador):
		retorno = ""
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:
				if(auxt.z == z and (auxt.x != 0 and auxt.y != 0 ) and auxt.dato != "Null"):
					retorno = retorno + str(auxt.x) +sepador+str(auxt.y)+"#"+str(auxt.disparo)+"$" 

				tempz = auxt.frente
				
				while tempz != None:
					if tempz.z == z :
						retorno  = retorno +str(tempz.x) +sepador+str(tempz.y)+"#"+str(tempz.disparo)+"$"
					tempz = tempz.frente

					
				tempz = auxt.atras
				while tempz != None:
					if tempz.z == z :
						retorno  = retorno + str(tempz.x) +sepador+str(tempz.y)+"#"+str(tempz.disparo)+"$"					
					tempz = tempz.atras				
				auxt = auxt.derecha
			aux = aux.abajo
		return retorno	 		
	def tiro(self,x,y,z):
		nodo = self.busquedaFull(int(x),int(y),int(z))
		if nodo != None:
			nodo.disparo = 1
			return True
		return False	
	def perdi(self):
		retorno = ""
		aux = self.cabeza
		while aux != None:
			auxt = aux
			while auxt != None:
				if( (auxt.x != 0 and auxt.y != 0 ) and auxt.dato != "Null"):
					if auxt.disparo == 1 and retorno != "False":
						retorno = "True" 
					else:
						retorno = "False"
				tempz = auxt.frente
				
				while tempz != None:
					
					if tempz.disparo == 1 and retorno != "False":
						retorno = "True" 
					else:
						retorno = "False"
					tempz = tempz.frente

					
				tempz = auxt.atras
				while tempz != None:
					if tempz.disparo == 1 and retorno != "False":
						retorno = "True" 
					else:
						retorno = "False"				
					tempz = tempz.atras				
				auxt = auxt.derecha
			aux = aux.abajo
		return retorno			
#MatrizPruebas = Matriz()
#MatrizPruebas.Insertar(3,6,0,"popito")
#MatrizPruebas.Insertar(1,1,0,"holitas")
#MatrizPruebas.Insertar(5,1,0,"holitas")
#MatrizPruebas.Insertar(2,1,0,"repetidosssakjdhsakjdaksj")	
#MatrizPruebas.Insertar(2,3,0,"holitas")
#MatrizPruebas.Insertar(2,1,0,"adios")	
#MatrizPruebas.Insertar(2,1,1,"satelite")
#MatrizPruebas.Insertar(2,1,2,"SuperSatelite")
#MatrizPruebas.Insertar(2,1,-2,"submarido")
#MatrizPruebas.Insertar(2,1,-3,"SuperSubmarino")
#MatrizPruebas.Graficar()
#SuperSubmarino = MatrizPruebas.busquedaFull(1,1,0)
#if SuperSubmarino != None:
#	print ( SuperSubmarino.dato)

from enum import Enum
from graphviz import Digraph
import six
class Pagina():
	"""docstring for Nodo"""
	def __init__(self):
		self.n = 0
		self.clave = []
	def insertar(self,id):
		self.n = self.n  + 1 
		self.clave.append(id)
		i = 0 
		while i < len(self.clave): #Ordenamiento burbuja XD 
			j = 0
			while j < len(self.clave)-1:
				if self.clave[j].clave > self.clave[j+1].clave:
					temp = self.clave[j]
					self.clave[j] = self.clave[j+1]
					self.clave[j+1] = temp
				j = j + 1
			i = i + 1
	def corregir(self):
		i = 0 
		while i < len(self.clave)-1:
			if self.clave[i].der != self.clave[i+1].iz:
				self.clave[i+1].iz = self.clave[i].der
			i = i + 1
	def getName(self):
		return hash(self)
	def buscar(self,clave):
		i = 0 
		while i < len(self.clave):
			if self.clave[i].clave == clave:
				return self.clave[i]
			i = i + 1	
		return None								
class Clave():
	def __init__(self,clave):
		self.clave = clave
		self.iz = None
		self.der = None	
		self.x = None
		self.y = None
		self.tiro = None
		self.res = None
		self.emisor = None
		self.receptor = None
		self.fecha = None
		self.tiempo = None
		self.NoTiro	= None
		self.tipo = None
class contenedor():
	def __init__(self,nodocalve,paginaiz,paginader):
		self.nodoClave = nodocalve
		self.paginaIz = paginaiz
		self.paginaDer = paginader
class ArbolB():
	def __init__(self):
		self.raiz = None
	def insertar(self,clave):
		NuevaClave = Clave(clave)
		if self.raiz == None:
			self.raiz = Pagina()
			self.raiz.insertar(NuevaClave)
		else:
			value = self.ins(self.raiz,NuevaClave)
			if value != None:
				pagina3 = Pagina()
				pagina3.insertar(value)
				self.raiz = pagina3
		return NuevaClave		
	#def busquedaPagina(self,pagina,clave):
						
	def insertar_pro(self,clave,x,y,tiro,res,emisor,receptor,fecha,tiempo,NoTiro,tipo):
		b = self.busqueda(clave)
		if b == None:
			temp = self.insertar(clave)
		else:
			if isinstance(clave, six.string_types):
				temp = self.insertar(str(NoTiro))
			else:
				temp = self.insertar(NoTiro)	
		temp.x = x
		temp.y = x 
		temp.tiro = tiro 
		temp.res = res 
		temp.emisor = emisor
		temp.receptor = receptor
		temp.fecha = fecha 
		temp.tiempo = tiempo
		temp.NoTiro = NoTiro
		temp.tipo = tipo
	def busqueda(self,clave):
		if self.raiz != None:
			return self.bus(self.raiz,clave)
		return None	
	def bus(self,pagina,d):
		if pagina == None:
			return None
		b = pagina.buscar(d)
		if  b != None:
			return b
		i = 0
		while i < len(pagina.clave)-1:
			if i == 0:
				if d < pagina.clave[i].clave:
					return self.bus(pagina.clave[i].iz,d)
			if 	d > pagina.clave[i].clave  and d < pagina.clave[i+1].clave:
				return self.bus(pagina.clave[i].der,d)
			if i == len(pagina.clave)-1:
				if d > pagina.clave[i].clave:
					return self.bus(pagina.clave[i].der,d)
			i = i + 1		
		return None			

			
	def ins(self,pagina,id):
		if pagina.clave[0].iz == None:
			#print("insertando en hoja " + str(id.clave))
			pagina.insertar(id)
			if len(pagina.clave) > 4:
				return self.dividirPag(pagina)
			return None
		if id.der != None and id.iz != None:
			pagina.insertar(id)
			if len(pagina.clave) > 4 :
				return self.dividirPag(pagina)
			return None

		if  id.clave < pagina.clave[0].clave :
			#print ( "comparando " + str(pagina.clave[0].clave) + " Y " + str(id.clave) )
			val = self.ins(pagina.clave[0].iz,id)
			if val != None:
				pagina.clave[0].iz = val.der
				pagina.corregir()
				val = self.ins(pagina,val)
				
				return val 
			return val
		i = 0

		while i < len(pagina.clave)-1:
			if id.clave > pagina.clave[i].clave  and id.clave < pagina.clave[i+1].clave:
				val = self.ins(pagina.clave[i].der,id)
				if val != None:
					pagina.clave[i].der  = val.iz
					pagina.corregir()
					val = self.ins(pagina,val)
					
					return val 
				return val 
			i = i +1	
		if id.clave > pagina.clave[len(pagina.clave)-1].clave:
			val = self.ins(pagina.clave[i].der,id)
			if val != None:
				pagina.clave[len(pagina.clave)-1].der = val.iz 
				pagina.corregir()
				val = self.ins(pagina,val)
				
				return val 
			return val 	 		

	def dividirPag(self,pagina):
		pagina1 = Pagina()
		pagina1.clave.append(pagina.clave[0])
		pagina1.clave.append(pagina.clave[1])
		pagina2 = Pagina()
		pagina2.clave.append(pagina.clave[3])
		pagina2.clave.append(pagina.clave[4])
		medio = pagina.clave[2]
		medio.der = pagina2
		medio.iz = pagina1		
		return medio
	def imprimir(self):
		if self.raiz != None:
			self.impri(self.raiz)
	def impri(self,pagina):
		i = 0
		print ("***PAGINA***")
		print(pagina.getName())
		while i < len(pagina.clave):
			print(str(pagina.clave[i].clave))
			i  = i +1
		print ("*** FIN PAGINA ***")	
		if pagina.clave[0].iz !=  None:
			self.impri(pagina.clave[0].iz)
		i = 0
		while i < len(pagina.clave):
			if pagina.clave[i].der != None:
				self.impri(pagina.clave[i].der)
			i  = i +1	
	def graficar(self):
		#dot = Digraph()
		dot = Digraph('dot', node_attr={'shape': 'record', 'height': '.1'})
		if self.raiz != None:
			self.graf(self.raiz,dot)
		dot.format = 'png'
		dot.render("ArbolBPrro")
	def graf(self,pagina,dot):
		i = 0
		s = ""
		while i < len(pagina.clave):
			if (i == len(pagina.clave)-1):
				s = s + "<" + str(hash(pagina.clave[i]))+"> " + str(pagina.clave[i].clave)
			else:
				s = s + "<" + str(hash(pagina.clave[i]))+"> " + str(pagina.clave[i].clave) + " | "		
			
			i = i + 1

		dot.node(str(pagina.getName()),s)
		i = 0
		if pagina.clave[0].iz !=  None:
			self.graf(pagina.clave[0].iz,dot)
			dot.edge(str(pagina.getName())+":"+str(hash(pagina.clave[0])),str(pagina.clave[0].iz.getName())+":"+str(hash(pagina.clave[0].iz.clave[1])))
		while i < len(pagina.clave):
			if pagina.clave[i].der != None:
				self.graf(pagina.clave[i].der,dot)
				dot.edge(str(pagina.getName())+":"+str(hash(pagina.clave[i])),str(pagina.clave[i].der.getName())+":"+str(hash(pagina.clave[i].der.clave[1])))
			i  = i +1
	def graficarC(self):
		#dot = Digraph()
		dot = Digraph('dot', node_attr={'shape': 'record', 'height': '.1'})
		if self.raiz != None:
			self.grafC(self.raiz,dot)
		dot.format = 'png'
		dot.render("ArbolBPrroC")
	def grafC(self,pagina,dot):
	
		i = 0
		s = ""
		while i < len(pagina.clave):
			if (i == len(pagina.clave)-1):
				s = s + "<" + str(hash(pagina.clave[i]))+"> " + str(pagina.clave[i].clave) +" x " +str(pagina.clave[i].x)+" y " +str(pagina.clave[i].y)+" tiro " +str(pagina.clave[i].tiro)  +" Resp " +str(pagina.clave[i].res) +" emisor " +str(pagina.clave[i].emisor) +" receptor " +str(pagina.clave[i].receptor) +" NoTiro " +str(pagina.clave[i].NoTiro) 
			else:
				s = s + "<" + str(hash(pagina.clave[i]))+"> " + str(pagina.clave[i].clave) +" x " +str(pagina.clave[i].x)+" y " +str(pagina.clave[i].y)+" tiro " +str(pagina.clave[i].tiro)  +" Resp " +str(pagina.clave[i].res) +" emisor " +str(pagina.clave[i].emisor) +" receptor " +str(pagina.clave[i].receptor) +" NoTiro " +str(pagina.clave[i].NoTiro) + " | "		
			
			i = i + 1

		dot.node(str(pagina.getName()),s)
		i = 0
		if pagina.clave[0].iz !=  None:
			self.grafC(pagina.clave[0].iz,dot)
			dot.edge(str(pagina.getName())+":"+str(hash(pagina.clave[0])),str(pagina.clave[0].iz.getName())+":"+str(hash(pagina.clave[0].iz.clave[1])))
		while i < len(pagina.clave):
			if pagina.clave[i].der != None:
				self.grafC(pagina.clave[i].der,dot)
				dot.edge(str(pagina.getName())+":"+str(hash(pagina.clave[i])),str(pagina.clave[i].der.getName())+":"+str(hash(pagina.clave[i].der.clave[1])))
			i  = i +1		

#A  = ArbolB()
#insertar_pro(self,clave,x,y,tiro,res,emisor,receptor,fecha,tiempo,NoTiro)
#A.insertar_pro(10,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(20,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(30,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(40,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(1,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(2,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(3,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(4,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(5,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar_pro(2,56,89,"a","res","emisor","resepto","f","tiempo",5893)
#A.insertar(60)
#A.insertar(40)
#A.insertar(30)
#A.insertar(50)
#A.insertar(80)
#A.insertar(20)
#A.insertar(19)
#A.insertar(17)
#A.insertar(16)
#A.insertar(25)
#A.insertar(31)
#A.insertar(35)
#A.insertar(90)
#A.insertar(150)
#A.insertar(180)
#A.insertar(2)
#A.insertar(3)
#A.insertar(39)
#A.insertar(36)
#A.insertar(34)
#A.insertar(34)
#A.insertar(34)
#A.insertar(34)
#A.insertar(34)
#A.insertar(34)
#A.insertar(33)
#A.insertar(33)
#A.insertar(33)
#A.insertar(-1)
#A.graficar()
		




						


						   




				





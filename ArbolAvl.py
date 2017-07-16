from graphviz import Digraph

class NodoAvl:

    def __init__(self, ramaIzdo, valor, ramaDcho):
        self.dato=valor
        self.apuntador = None
        self.pas = None
        self.izdo=ramaIzdo
        self.dcho=ramaDcho
        self.fe = 0

    def __init__(self, valor):
        # super(Nodo, self).__init__()
        self.dato = valor
        self.apuntador = None
        self.pas = None
        self.izdo=None
        self.dcho=None
        self.fe = 0

    def valorNodo(self):
        return self.dato

    def setValor(self, dato):
        self.dato=dato

    def subarbolIzdo(self):
        return self.izdo

    def subarbolDcho(self):
        return self.dcho

    def nuevoValor(self, d):
        self.dato=d

    def ramaIzdo(self, n):
        self.izdo=n

    def ramaDcho(self, n):
        self.dcho=n

    def visitar(self):
        r= self.dato
        return r
      


class Avl:
    global raiz
    global listaAct
    cadena=""
    
    def __init__(self):
        self.raiz=None
        self.cadena=""

    def raizArbol(self):
        return self.raiz
    
    def obtenerRaiz(self):
        return self.raizArbol().visitar()

    def rotacionII(self, n, n1):
        n.ramaIzdo(n1.subarbolDcho())
        n1.ramaDcho(n)
        if n1.fe==-1:
            n.fe=0
            n1.fe=0
        else:
            n.fe=-1
            n1.fe=1
        return n1
    
    def rotacionDD(self, n, n1):
        n.ramaDcho(n1.subarbolIzdo())
        n1.ramaIzdo(n)
        if n1.fe==+1:
            n.fe=0
            n1.fe=0
        else:
            n.fe=+1
            n1.fe=-1
        return n1
    
    def rotacionID(self, n, n1):
        n2=n1.subarbolDcho()
        n.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n)
        n1.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n1)
        if n2.fe == +1:
            n1.fe = -1
        else:
            n1.fe = 0
        if n2.fe == -1:
            n.fe = 1
        else:
            n.fe = 0
        n2.fe = 0
        return n2
    
    def rotacionDI(self, n, n1):
        n2=n1.subarbolIzdo()
        n.ramaDcho(n2.subarbolIzdo())
        n2.ramaIzdo(n)
        n1.ramaIzdo(n2.subarbolDcho())
        n2.ramaDcho(n1)
        if n2.fe == +1: 
            n.fe = -1 
        else:
            n.fe = 0 
        if n2.fe == -1:
            n1.fe = 1 
        else:
            n1.fe = 0 
        n2.fe = 0
        return n2
    
    def insertarAvl(self, raiz, dt, h):
        n1=None
        if raiz is None:
            raiz = NodoAvl(dt)
            h.setLogical(True)
            pass
        elif dt > raiz.valorNodo():
            iz=None
            iz = self.insertarAvl(raiz.subarbolIzdo(), dt, h)
            raiz.ramaIzdo(iz)  
            if h.booleanValue():
                if raiz.fe==1:       
                    raiz.fe = 0
                    h.setLogical(False)     
                    pass      
                elif raiz.fe == 0:
                    raiz.fe = -1    
                    pass
                elif raiz.fe == -1:
                    n1 = raiz.subarbolIzdo()    
                    if n1.fe == -1:
                        raiz = self.rotacionII(raiz, n1)
                    else:     
                        raiz = self.rotacionID(raiz, n1)
                        pass
                    h.setLogical(False)

        elif dt < raiz.valorNodo():
            dr=None
            dr = self.insertarAvl(raiz.subarbolDcho(), dt, h) 
            raiz.ramaDcho(dr)
            if h.booleanValue():
                if raiz.fe==1:        
                    n1 = raiz.subarbolDcho()    
                    if n1.fe == +1:
                        raiz = self.rotacionDD(raiz, n1)
                    else:      
                        raiz = self.rotacionDI(raiz,n1)     
                    h.setLogical(False)
                    pass
                elif raiz.fe==0:      
                    raiz.fe = +1
                    pass
                elif raiz.fe==-1:      
                    raiz.fe = 0
                    h.setLogical(False)
                    pass
        else:
            print("No puede haber claves repetidas " ) 
            pass
        return raiz
    
    def insertar(self, valor):
        h=Logical(False)
        dato=valor
        self.raiz=self.insertarAvl(self.raiz, dato, h)
        

    def eliminar (self, valor):
        dato=None
        dato = valor
        flag = Logical(False) 
        self.raiz = self.borrarAvl(self.raiz, dato, flag)

    
        
    def borrarAvl(self, r, clave, cambiaAltura):
        if r is None:
            print(" Nodo no encontrado ")
        elif clave > r.valorNodo():
            iz = None
            iz = self.borrarAvl(r.subarbolIzdo(),clave,cambiaAltura)  
            r.ramaIzdo(iz)
            if cambiaAltura.booleanValue():
                r = self.equilibrar1(r, cambiaAltura) 
        elif clave < r.valorNodo():
            dr=None   
            dr = self.borrarAvl(r.subarbolDcho(), clave, cambiaAltura)  
            r.ramaDcho(dr)  
            if cambiaAltura.booleanValue():
                r = self.equilibrar2(r, cambiaAltura) 
        else:  # Nodo encontrado    
            q=None
            q = r   # nodo a quitar del arbol
            if q.subarbolIzdo()is None:
                r = q.subarbolDcho()  
                cambiaAltura.setLogical(True)  
            elif q.subarbolDcho() is None:
                r = q.subarbolIzdo()
                cambiaAltura.setLogical(True)
            else:  
              # tiene rama izquierda y derecha 
                iz=None   
                iz = self.reemplazar(r, r.subarbolIzdo(),cambiaAltura)   
                r.ramaIzdo(iz)  
                if cambiaAltura.booleanValue():
                    r = self.equilibrar1(r, cambiaAltura)  
            q = None    
        return r
    
    def reemplazar(self, n, act, cambiaAltura): 
        if act.subarbolDcho() is not None:
            d=None
            d = self.reemplazar(n, act.subarbolDcho(), cambiaAltura) 
            act.ramaDcho(d)  
            if cambiaAltura.booleanValue():
                act = self.equilibrar2(act, cambiaAltura)
        else:
            n.nuevoValor(act.valorNodo())
            n = act 
            act = act.subarbolIzdo()
            n = None  
            cambiaAltura.setLogical(True) 
        return act
        
    def equilibrar1(self, n, cambiaAltura):
        n1=None
        if n.fe==-1:
            n.fe = 0
            pass
        elif n.fe==0:
            n.fe = 1      
            cambiaAltura.setLogical(False)      
            pass
        elif n.fe==+1:  #se aplicar un tipo de rotacin derecha
            n1 = n.subarbolDcho()      
            if n1.fe >= 0:
                if n1.fe == 0:  # la altura no vuelve a disminuir
                    cambiaAltura.setLogical(False)      
                n = self.rotacionDD(n, n1)            
            else:
                n = self.rotacionDI(n, n1)    
            pass
        return n 
    def equilibrar2(self, n, cambiaAltura):
        n1=None
        if n.fe==-1:
            n1 = n.subarbolIzdo()      
            if n1.fe <= 0:
                if n1.fe == 0:
                    cambiaAltura.setLogical(False)
                n = self.rotacionII(n, n1)        
            else:
                n = self.rotacionID(n,n1)
            pass  
        elif n.fe==0:
            n.fe = -1      
            cambiaAltura.setLogical(False)      
            pass
        elif n.fe==+1:
            n.fe = 0 
            pass 
        return n
    
    def agregar(self, codigo):
        #prueba=archivo(codigo)
        self.insertar(codigo)


    def graficar(self,nombre):
        dot = Digraph()
        if self.raiz != None:
            self.grafi(self.raiz,dot)
        dot.format = 'png'
        dot.render("avls/"+nombre+"ArbolAvl")    
    def grafi (self , nodo, dot):
        if nodo != None:
            if nodo.apuntador == None:
                dot.node(str(hash(nodo)),str(nodo.dato) + " " + str(nodo.pas))
            else:
                dot.node(str(hash(nodo)),str(nodo.dato) + " " +str(nodo.apuntador.pas))
        if nodo.dcho != None:
            self.grafi(nodo.dcho,dot)  
            dot.edge(str(hash(nodo)) , str (hash(nodo.dcho)) )        
        if nodo.izdo != None:
            
            self.grafi(nodo.izdo,dot)
            dot.edge(str(hash(nodo)) , str (hash(nodo.izdo)) )

    def insertar_Pro(self,dato,pas,nodo):
        if nodo != None:
            self.insertar(dato)
            temp = self.busqueda(self.raiz,dato)
            temp.apuntador = nodo
        else:
            self.insertar(dato)
            temp = self.busqueda(self.raiz,dato)
            temp.pas = pas
    def busqueda(self,nodo,dato):
        if nodo != None:
            if nodo.dato == dato:
                return nodo

        if nodo.dato < dato:
            return self.busqueda(nodo.izdo,dato)
        else:
            return self.busqueda(nodo.dcho,dato)

class Logical:
    def __init__(self, f):
        self.v = f

    def setLogical(self, f):
        self.v = f

    def booleanValue(self):
        return self.v

avl = Avl()
#nombre, descripcion, clave
#nodoBinario = ArbolBinario.Nodo("jorge","daniel")
avl.insertar_Pro("juan","akjsd",None)
#avl.insertar_Pro("mart","akjsd",None)
#avl.insertar_Pro("abi","akjsd",None)
#avl.insertar_Pro("jesu","akjsd",None)
avl.insertar_Pro("perr","akjsd",None)
#avl.insertar_Pro("ext","akjsd",None)
#avl.insertar_Pro("mous","akjsd",None)
#avl.insertar_Pro("jorge","akjsd",nodoBinario)

avl.graficar("marta")

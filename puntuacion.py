from wx import *
import sqlite3

class MyApp(App):
  def listapuntaje(self,puntaje):
    self.listanombres = []
    self.listapuntaje = []
    ventana = Frame(None,-1,"FIN DEL JUEGO")
    sizer = GridBagSizer()

    #creo el un texto estatico para mostrar la puntuacion
    self.punt = str(puntaje)
    puntaje=StaticText(ventana,-1, label = self.punt)
    sizer.Add(puntaje, pos = (1,4))
    
    #CASILLERO NOMBRES
    nombre = "NOMBRE"
    puntaje=StaticText(ventana,-1, label =nombre)
    sizer.Add(puntaje, pos = (0,2))
    
    #CASILLERO PUNTUACION
    puntuacion = "PUNTUACION"
    puntaje=StaticText(ventana,-1, label = puntuacion)
    sizer.Add(puntaje, pos = (0,4))
    
    #PRIMERA FILA se crean la caja de texto, ventana principal
    self.cajaTexto = TextCtrl(ventana)
    sizer.Add(self.cajaTexto, pos = (1,2))
   
    #SEGUNDA FILA // se agrega el boton guardar
    self.boton = Button(ventana,-1,"GUARDAR")
    self.boton.Bind(EVT_BUTTON,self.guardarPuntuacion)
    sizer.Add(self.boton,pos = (5,7))
    ventana.SetSizer(sizer)
    ventana.Show()

# HAMBLET BOTON DE CARGA  // es el metodo para cargar los nombres en una lista
  def guardarPuntuacion(self, evt):
    nombre = self.cajaTexto.GetValue()
    puntuacion = int(self.punt)
    self.listanombres.append(nombre)
    self.listapuntaje.append(self.punt)
    self.cajaTexto.Clear()
    
    #conexion con base de datos
    conect = sqlite3.connect ("BASE2.db")
    cur = conect.cursor( )
    try:
      cur.execute("CREATE TABLE JUGADOR(id INTEGER NOT NULL PRIMARY KEY, nombre TEXT, puntaje INTEGER)")
    except:
      pass
    cur.execute("INSERT INTO JUGADOR(nombre,puntaje) VALUES (?,?)",[nombre,puntuacion])

    
    
    #pasarle los valores 
  
    
    #se agregan los cambios
    
    conect.commit()
    #cerramos la conexion
    conect.close()
    
ap = MyApp()    
ap.MainLoop()
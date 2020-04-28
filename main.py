import pygame
import random
from opciones import *
from char import *
from os import path 
from puntuacion import *
from basedatos import  *

class Juego():
  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    self.ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("navesita")
    self.clock = pygame.time.Clock()  
    self.correr = True
    self.gamedir = path.dirname(__file__)
    self.spritedir = path.join (self.gamedir, "sprites")
    self.fondo = pygame.image.load(os.path.join(self.spritedir, "fondo3.png")).convert_alpha()

  
  def mostrarPuntaje(self,ventana, texto, tamanio, x , y):
    fuente = pygame.font.Font(None, tamanio)
    texto = fuente.render(texto, True, (255, 255, 255))
    textorect = texto.get_rect()
    textorect.midtop = (x,y)
    ventana.blit(texto, textorect)


  
  def generarMeteoro(self, dificultad):
    for i in range (dificultad):
      self.meteoro = Meteoro(self)
      self.spriteMeteoro.add(self.meteoro)
      self.sprites.add(self.meteoro) 
  
  def generarCargador(self):
    self.cargador = Cargador(self)
    self.spritecargador.add(self.cargador)
    self.sprites.add(self.cargador)
    
  def reset(self):
    #nuevo juego
    self.sprites = pygame.sprite.Group()
    self.balas = pygame.sprite.Group()
    self.spriteMeteoro = pygame.sprite.Group()
    self.spritecargador = pygame.sprite.Group()
    self.jugador = Jugador(self)
    self.cargador = Cargador(self) 
    self.generarMeteoro(DIFICULTAD)
    self.generarCargador()
    self.sprites.add(self.cargador)
    self.sprites.add(self.jugador)
    self.spritecargador.add(self.cargador)
    self.corriendo()

  def corriendo (self): 
    self.correr = True
    while self.correr: # necesario para que la ventana entre en bucle y no se cierre
      self.clock.tick(FPS)
      self.evento()
      self.update()
      self.dibujar()

  def update (self): 
    self.sprites.update()
  
  def evento(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        if self.correr:
          self.correr = False
  
  def dibujar(self):
    ##self.ventana.fill((0,0,0))
    self.ventana.blit(self.fondo,(0,0))
    self.sprites.draw(self.ventana)
    self.mostrarPuntaje(self.ventana,"puntaje: " + str(self.jugador.puntaje), 25, ANCHO-70, 25)
    self.mostrarPuntaje(self.ventana,"vidas: " + str(self.jugador.vidas), 25, ANCHO/2, 25)
    self.mostrarPuntaje(self.ventana,"balas: " + str(self.jugador.balas), 25, ANCHO//6, 25)
    self.mostrarPuntaje(self.ventana,"high score: " + str(tupla[0]) ,25, ANCHO//4, 5)
    pygame.display.flip()


a=Juego()

while a.correr:
  a.reset()
  a.corriendo()
  pygame.quit()
if a.correr == False:
  ap=MyApp()
  ap.listapuntaje(a.jugador.puntaje)
  ap.MainLoop()
  


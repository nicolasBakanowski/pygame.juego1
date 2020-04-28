import pygame
from opciones import *
import random
import os

class Jugador(pygame.sprite.Sprite):
  def __init__(self, juego):
    pygame.sprite.Sprite.__init__(self)
    self.juego = juego
    self.image = pygame.image.load(os.path.join(self.juego.spritedir, "nabe2.png")).convert_alpha()
    self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/4) ,int(self.image.get_height()/4)))
    self.rect = self.image.get_rect()
    self.jx = ANCHO / 2 - self.rect.width / 2
    self.jy = ALTO - 90
    self.vel = 5
    self.puntaje = 0
    self.vidas = 3
    self.balas = 50
    self.delaytiro = 250
    self.ultimotiro = pygame.time.get_ticks()
    self.meteorodestruido = 0
    self.delaycargador = 6000
    self.ultimocargador = pygame.time.get_ticks()
    

  def update (self):
    #movimiento del personake
    presiona = pygame.key.get_pressed()
    if presiona[pygame.K_RIGHT] and self.rect.right < ANCHO:
      self.jx += self.vel
    if presiona[pygame.K_LEFT] and self.rect.left > 0:
      self.jx -= self.vel
    
    #activar disparo
    if presiona[pygame.K_SPACE]:
      self.disparar()
    self.rect.x = self.jx
    self.rect.y = self.jy
    
    #colision meteoro nabe
    self.hits = pygame.sprite.spritecollide(self, self.juego.spriteMeteoro,True)
    if self.hits :
      self.juego.generarMeteoro(1)
      self.vidas -= 1       
    if self.vidas <= 0 :
      self.juego.correr = False
    
    #colision bala meteoro 

    self.balamete = pygame.sprite.groupcollide(self.juego.balas, self.juego.spriteMeteoro, True, True)
    if self.balamete:
      self.juego.generarMeteoro(1)
      self.meteorodestruido += 1
      if self.meteorodestruido == 10: #condicion para agregar mas meteoros 
        self.meteorodestruido = 0
        self.juego.generarMeteoro(2)
        self.puntaje +=100   

    #colision cargador nave
    self.cargarbalas = pygame.sprite.spritecollide(self, self.juego.spritecargador,True)
    cargadorahora = pygame.time.get_ticks()
    cargadorrecarga = Cargador(self.juego)
    if cargadorahora - self.ultimocargador > self.delaycargador:
      self.ultimocargador = cargadorahora
      cargadorrecarga.update()
      self.juego.generarCargador()
      self.puntaje -50
    if self.cargarbalas:
      self.balas += 5
     
    

  def disparar(self):
    tiroahora = pygame.time.get_ticks() #guarda el ticks del disparo 
    bala = Bullet(self.juego)
    if tiroahora - self.ultimotiro > self.delaytiro and self.balas > 0 :
      self.balas -= 1 
      self.ultimotiro = tiroahora #remplaza el valor del ultimo tiro 
      bala.update()
      self.juego.sprites.add(bala)
      self.juego.balas.add(bala)

     

class Bullet(pygame.sprite.Sprite):
  def __init__(self, juego):
    pygame.sprite.Sprite.__init__(self)
    self.juego = juego
    self.image = pygame.image.load(os.path.join(self.juego.spritedir, "tiros.png")).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = self.juego.jugador.rect.x 
    self.rect.midbottom = self.juego.jugador.rect.midtop
   
  def update(self):
    self.rect.y -= 5
    if self.rect.bottom < 0 :
      self.kill()

class Cargador(pygame.sprite.Sprite):
  def __init__(self,juego):
    pygame.sprite.Sprite.__init__(self)
    self.juego = juego
    self.image = pygame.image.load(os.path.join(self.juego.spritedir, "cargador.png")).convert_alpha()
    self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/2) ,int(self.image.get_height()/2)))
    self.rect = self.image.get_rect()  
    self.rect.x = random.randrange(10,ANCHO-5)
    self.rect.y = 0
    self.vely = 8
  
  def update(self):
    self.rect.y += self.vely

class Meteoro(pygame.sprite.Sprite):
  def __init__(self,juego):
    pygame.sprite.Sprite.__init__(self)
    self.juego = juego
    self.image = pygame.Surface((20, 30))
    self.image.fill((0,120,0))
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(10,ANCHO-5)
    self.rect.y = 0
    self.vely = random.randrange(3,9)
    if self.vely == 1 or self.vely == 2 or self.vely == 3:
      self.image = pygame.image.load(os.path.join(self.juego.spritedir, "meteorogris.png")).convert_alpha()
      self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/2) ,int(self.image.get_height()/2)))
    if self.vely == 4 or self.vely == 5 or self.vely == 6:
      self.image = pygame.image.load(os.path.join(self.juego.spritedir, "meteoroazul.png")).convert_alpha()
      self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/2) ,int(self.image.get_height()/2)))
    if self.vely == 7 or self.vely == 8 or self.vely == 9:
      self.image = pygame.image.load(os.path.join(self.juego.spritedir, "meteororojo.png")).convert_alpha()
      self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/2) ,int(self.image.get_height()/2)))
   
  
  def update (self):
    self.rect.y += self.vely
    if self.rect.top > ALTO + 10:
      self.juego.jugador.puntaje +=10 
      self.rect.x = random.randrange(ANCHO - self.rect.width)
      self.rect.y = random.randrange(-100, -40)
      self.vely = random.randrange(1, 8)
      self.hits = pygame.sprite.groupcollide(self.juego.balas, self.juego.spriteMeteoro, True, True)
      
  
    
        
  
        
        

    



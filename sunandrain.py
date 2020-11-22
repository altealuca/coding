from sense_hat import SenseHat
from time import sleep

s = SenseHat()    #variabile
s.low_light = True

#variabili per definire i vari colori
y = (255, 255, 0)     #giallo
yt= (140, 22, 2)      #arancione
b = (0, 0, 255)       #blu
o = (0, 0, 0)         #nero/niente    #tutti questi colori sono variaili
#va da 0 a 255, ovvero 256 colori, ovvero 2 (0 e 1) alla potenze di 8

#riempimento matrice per Sole
sun = [       #definizione di ua funzione
  y, o, o, o, o, o, o, y,
  o, y, o, o, o, o, y, o,
  o, o, y, y, y, y, o, o,
  y, y, y, y, y, y, y, y, 
  o, o, y, y, y, y, o, o,
  o, o, y, y, y, y, o, o,
  o, y, o, o, o, o, y, o,
  y, o, o, o, o, o, o, y
  ]   #quando c'è aperta quadra e chiusa quadra, quello che c'è in mezzo è un elenco
  
sun1 = [
  yt, o, o, o, o, o, o, yt,
  o, yt, o, o, o, o, yt, o,
  o, o, yt, yt, yt, yt, o, o,
  yt, yt, yt, yt, yt, yt, yt,yt, 
  o, o, yt, yt, yt, yt, o, o,
  o, o, yt, yt, yt, yt, o, o,
  o, yt, o, o, o, o, yt, o,
  yt, o, o, o, o, o, o, yt
  ]

#riempimento matrice per pioggia  
rain = [
  o,b,o,b,o,b,o,b,
  o,b,o,b,o,b,o,b,
  b,o,o,o,o,o,o,o,
  b,o,o,b,o,o,o,b,
  o,b,o,b,o,b,o,b,
  o,b,o,o,o,b,o,o,
  b,o,o,b,o,o,o,b,
  o,b,o,b,o,b,o,b
  ]
  
rain1=[
  o,b,o,b,o,b,o,b,
  o,b,o,b,o,b,o,b,
  o,o,o,b,o,b,o,b,
  b,o,o,o,o,o,o,o,
  b,o,o,b,o,o,o,b,
  o,b,o,b,o,b,o,b,
  o,b,o,o,o,b,o,o,
  b,o,o,b,o,o,o,b
  ]
  
rain2=[
  o,o,o,b,o,o,o,o,
  o,b,o,b,o,b,o,b,
  o,b,o,b,o,b,o,b,
  o,o,o,b,o,b,o,b,
  b,o,o,o,o,o,o,o,
  b,o,o,b,o,o,o,b,
  o,b,o,b,o,b,o,b,
  o,b,o,o,o,b,o,o
  ]

#ciclo per controllo valore umidità
while (1):    #oppure "while True:" #"while" ripete delle istruzioni finchè queste sono vere
  v=s.get_humidity()
  if v<50:    # "if" è una struttura, un insieme di istruzioni
      s.set_pixels(sun)     #significa "dai un valore ai pixel di sun"
      sleep(0.1)
      s.set_pixels(sun1)
      sleep(0.1)
  else:
    s.set_pixels(rain)
    sleep(0.1)
    s.set_pixels(rain1)
    sleep(0.1)
    s.set_pixels(rain2)
    
  
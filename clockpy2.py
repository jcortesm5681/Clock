import time
import datetime as dt
import pygame
import sys
import pygame.mixer
import math


pygame.init()

#screen = pygame.display.set_mode((window_width, window_height))
screen= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#window_width = 800
#window_height = 600
info = pygame.display.Info()
window_width = info.current_w
window_height = info.current_h

pygame.display.set_caption("Clock")
global alarm_sound 
global alarm_played 
global vibration_amplitude 
global vibration_frequency



def clockjac(font_size, color):
    #font_size = 100
    
    
    #font = pygame.font.SysFont("Tippa", font_size)
    clock = pygame.time.Clock()
    terminado = False
    while not terminado:
        font = pygame.font.SysFont("Impact", font_size) #
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:
                    # Si se presiona la tecla "q"; terminar programa
                    terminado = True
                if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                    font_size=font_size+50
                if font_size >= 600: font_size= 600
                if evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                    font_size=font_size-50
                if font_size <= 300: font_size= 300
        
        min = dt.datetime.now().minute
        hou=dt.datetime.now().strftime("%I") # Hora en formato 12h con ceros a la izquierda
        
        #screen.fill((0, 0, 0))  # Limpia la pantalla con color negro
        s = pygame.Surface((window_width,window_height))  # tamano del cuadro
        s.set_alpha(50)                # nivel alpha
        s.fill((0,0,0))           # llena el cuadrado de color negro RGB(0,0,0)
        screen.blit(s, (0,0))  

        # Muestra el tiempo en la ventana 
        #time_text =str(hou).zfill(2)  +"  "+str(min).zfill(2)
        text1 = font.render(hou, True, color)  
        text2 = font.render(str(min).zfill(2), True, color)
        screen.blit(text1, (window_width/2 -(font_size + 100), window_height/2 - font_size/1.5))
        screen.blit(text2, (window_width/4 +font_size, window_height/2 - font_size/1.5))
        #print(window_width/4 - font_size, window_height/2 - font_size/1.5 )
        # Dibujar el cuadro
        pygame.draw.rect(screen, (0,0,0), (0, window_height/2 -font_size/10, window_width, 10))  # El ?ltimo argumento es el grosor del borde
    
     
        pygame.display.flip()
        clock.tick(20)  # Actualiza la pantalla 






#--------------------------------------------------------------
# INICIO DEL PROGRAMA
#--------------------------------------------------------------

#leer parametros:

lossegundos = 0
tamanio = 0
font_size = 450
color=(183,183,183) #
titulovent="CLOCK OF LIFE"
#variables de hora anterior para comparar, se inician vacio.
hou_ant='h'
min_ant='m'
sec_ant='s'  
sec_ant2 ='a'
sec_real ='a'


y = 1
if len(sys.argv) == 1:
    clockjac(font_size, color)
else:
    for n in sys.argv:
        #print('n'+ n)
        #print(sys.argv[y])
        if n=="-s":
            lossegundos=lossegundos+ int(sys.argv[y])
        elif  n=="-m":
            lossegundos=lossegundos+(int(sys.argv[y])*60)
        elif  n=="-h":
            lossegundos=lossegundos+(int(sys.argv[y])*3600)
        elif  n=="-f":
              tamanio=int(sys.argv[y]) # parametro para tameno de fuente, por defecto 100
        elif  n=="-c":
              #col=sys.argv[y] # parametro para tameno de fuente, por defecto color red
              col= (sys.argv[y]).lstrip('#')
            #print('h =',h)
              color=tuple(int(col[i:i+2], 16) for i in (0, 2, 4))
        elif  n=="-t":
              titulovent=sys.argv[y] # parametro para nombre. por defecto "CLOCK"
              pygame.display.set_caption(titulovent)

        elif  n=="--help" :
            print("Modo de empleo: Clock [opciones]...")
            print("")           
            print("Programa de consola que genera una cuenta regresiva o un reloj digital, simulando display de 7 segmentos, Para eso utiliza la fuente \"Digital-7\"; la cual hay que instalar en el sistema.")
            print("")
            print("Las siguientes opciones activan una cuenta regresiva:")
            print("-s   Segundos a contar hacia atras")
            print("-m   Minutos a contar hacia atras")
            print("-h   Horas a contar hacia atras")
            print("")
            print("Ejemplo:")
            print("")
            print("clock -m 5 -s 10")
            print("Crea una cuenta regresiva de 5 minutos y 10 segundos")
            print("")
            print("Si no se encuentran esas opciones se activa un reloj digital que marca la hora del sistema")
            print("")
            print("OTRAS OPCIONES")
            print("-f   Cambia el tamano de la fuente del texto, por defecto es 100")
            print("-c   Cambia color del texto, por defecto es ROJO, acepta colores en RGB ejemplo: #e2943a ")
            print("-t   Cambia titulo de la ventana")
            print("")
            print("Ejemplo:")
            print("")
            print("clock -c \"#e2943a\" -f 150 -h 3 -t Detonador")
            print("")
            print("clock -c \"#e2943a\" -f 150 -t HoraActual")
            print("")
            print("El primero crea una cuenta hacia atras de tres horas con fuente tamano 150, color ambar, y titulo de la ventana \"Detonador\"")
            print("")
            print("El segundo crea un reloj con hora de sistema, fuente tamano 150, color ambar, y titulo de la ventana \"HoraActual\"")

            exit();

        y=y+1
    
 # asigne parametro tamano fuente
    if tamanio == 0 :
        font_size = 1   
    else:
        font_size = tamanio


    if lossegundos == 0:
        clockjac(font_size, color)
    else:
        Countdown(lossegundos + 1, font_size, color)





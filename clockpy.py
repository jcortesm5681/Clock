import time
import datetime as dt
import pygame
import sys
import pygame.mixer
import math



#--------------------------------------------------------------
#     Globales     #
#--------------------------------------------------------------
 
# Constante para la pantalla completa
pantalla_completa= False
window_width = 800
window_height = 600
#Parametros por defecto
lossegundos = 0
font_size = 150
tipo = 'D' #digital 'D' o flip 'O'
color=(255,0,0) #"red" por defecto
titulovent="CLOCK OF LIFE"


#--------------------------------------------------------------
#     FUNCIONES     #
#--------------------------------------------------------------
def Countdown(p, font_size2, color2):
    clock = pygame.time.Clock()
    info = pygame.display.Info()
    global window_width 
    global window_height 
    global pantalla_completa
    global titulovent
    vibration_amplitude = 10  # Amplitud de la vibracion en pixeles
    vibration_frequency = 10  # Frecuencia de vibracion en Hz
    alarm_sound= pygame.mixer.Sound("sonido/Bach.ogg")
    alarm_played= False
    sec_ant  = 61


    if pantalla_completa:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        info = pygame.display.Info()
        window_width = info.current_w
        window_height = info.current_h
        pygame.display.set_caption(titulovent)
    else:
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(titulovent)

    terminado = False
    while not terminado:
        font = pygame.font.SysFont("Digital-7 Mono", font_size2) 
        s = pygame.Surface((window_width,window_height))  # tamano del cuadro
        s.set_alpha(50)           # nivel alpha
        s.fill((0,0,0))           # llena el cuadrado de color negro RGB(0,0,0)
        screen.blit(s, (0,0)) 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:
                    # Si se presiona la tecla "q"; terminar programa
                    terminado = True
                if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                        font_size2=font_size2+25
                if font_size2 >= 600: font_size2= 600
                if evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                    font_size2=font_size2-25
                if font_size2 <= 100: font_size2= 100
                if evento.key == pygame.K_f:
                    # Si se presiona la tecla "f", alternamos entre pantalla completa y ventana
                    pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    info = pygame.display.Info()
                    window_width = info.current_w
                    window_height = info.current_h
                    pygame.display.set_caption(titulovent)
                else: 
                    window_width = 800
                    window_height = 600
                    screen = pygame.display.set_mode((window_width, window_height))
                    pygame.display.set_caption(titulovent)

        if p!=0 :
            sec = dt.datetime.now().second   
            if(sec!=sec_ant):
                p -= 1
                houInt = int(p / 3600)
                minInt = (int(p / 60)) % 60
                secInt = p % 60
                sec_ant = sec   
                sec = dt.datetime.now().second   
 
            time_text =str(houInt).zfill(2)  +":"+str(minInt).zfill(2)+":" +str(secInt).zfill(2) #str(hou).zfill(2)  +":"+str(min).zfill(2)+":" +str(sec).zfill(2)  #f"{str(hou).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}"
            text = font.render(time_text, True, color2)  
            screen.blit(text, (window_width/2 - text.get_width()/2, window_height/2 - font_size2/2 ))           
        else:
            text = font.render("00:00:00", True, color)  
            screen.blit(text, (window_width/2 - text.get_width()/2, window_height/2 - font_size2/2 ))
            #font2 = pygame.font.SysFont("Tippa", 30) 
            font2 = pygame.font.SysFont("Punktype", 50) 
            text = font2.render("Time's up!", True, (255,0,0))  
            #screen.blit(text, (window_width/2- text.get_width()/2, window_height/2 + font_size/2 )) 

            # Calcular el desplazamiento horizontal y vertical basado en el tiempo
            vibration_offset_x = vibration_amplitude * math.sin(pygame.time.get_ticks() * 2 * math.pi * vibration_frequency / 1000)
            vibration_offset_y = vibration_amplitude * math.cos(pygame.time.get_ticks() * 2 * math.pi * vibration_frequency / 1000)
            
            # Calcular la posicion actual del texto
            text_position = (window_width/2 - text.get_width()/2 + vibration_offset_x, window_height/2 + font_size/2 + vibration_offset_y)
            
            # Dibujar el texto en la pantalla
            screen.blit(text, text_position)
    
            #alarm_sound.play()
            if not alarm_played:  # Verifica si el sonido aun no se ha reproducido
                alarm_sound.play()  # Reproduce el sonido de la alarma
                alarm_played = True  # Cambia la variable para que no se reproduzca nuevamente
        pygame.display.flip()
        clock.tick(20)



def Clock(font_size2, color2,tipo2):
    clock = pygame.time.Clock()
    info = pygame.display.Info()
    global window_width 
    global window_height 
    global pantalla_completa
    global titulovent
    if pantalla_completa:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        info = pygame.display.Info()
        window_width = info.current_w
        window_height = info.current_h
        pygame.display.set_caption(titulovent)
    else:
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(titulovent)

    if tipo2 == 'O':
        #FLIP FLOP!            
        color2=(183,183,183) ## si es flip, ignoro el color enviado
        clock = pygame.time.Clock()
        terminado = False
        while not terminado:
            font = pygame.font.SysFont("Impact", font_size2) #
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    terminado = True
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:
                        # Si se presiona la tecla "q"; terminar programa
                        terminado = True
                    if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                        font_size2=font_size2+50
                    if font_size2 >= 600: font_size2= 600
                    if evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                        font_size2=font_size2-50
                    if font_size2 <= 300: font_size2= 300
                    if evento.key == pygame.K_f:
                        # Si se presiona la tecla "f", alternamos entre pantalla completa y ventana
                        pantalla_completa = not pantalla_completa
                    if pantalla_completa:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        info = pygame.display.Info()
                        window_width = info.current_w
                        window_height = info.current_h
                        pygame.display.set_caption(titulovent)
                    else: 
                        window_width = 800
                        window_height = 600
                        screen = pygame.display.set_mode((window_width, window_height))
                        pygame.display.set_caption(titulovent)
                
            min = dt.datetime.now().minute
            hou = dt.datetime.now().strftime("%I") # Hora en formato 12h con ceros a la izquierda
            
            #screen.fill((0, 0, 0))  # Limpia la pantalla con color negro
            s = pygame.Surface((window_width,window_height))  # tamano del cuadro
            s.set_alpha(50)                # nivel alpha
            s.fill((0,0,0))           # llena el cuadrado de color negro RGB(0,0,0)
            screen.blit(s, (0,0))  

            # Muestra el tiempo en la ventana 
            #time_text =str(hou).zfill(2)  +"  "+str(min).zfill(2)
            text1 = font.render(hou, True, color2)  
            text2 = font.render(str(min).zfill(2), True, color2)
            screen.blit(text1, (window_width/2 -(font_size2 + 100), window_height/2 - font_size2/1.5))
            screen.blit(text2, (window_width/4 +font_size2, window_height/2 - font_size2/1.5))
            #print(window_width/4 - font_size, window_height/2 - font_size/1.5 )
            # Dibujar el cuadro
            pygame.draw.rect(screen, (0,0,0), (0, window_height/2 -font_size2/10, window_width, 10))  # El ?ltimo argumento es el grosor del borde
        
        
            pygame.display.flip()
            clock.tick(20)  # Actualiza la pantalla 
    elif tipo2 == 'D':
        #DIGITAL
        clock = pygame.time.Clock()
        terminado = False
        while not terminado:
            font = pygame.font.SysFont("Digital-7 Mono", font_size2) #
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    terminado = True
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:
                        # Si se presiona la tecla "q"; terminar programa
                        terminado = True
                    if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                        font_size2=font_size2+25
                    if font_size2 >= 600: font_size2= 600
                    if evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                        font_size2=font_size2-25
                    if font_size2 <= 100: font_size2= 100
                    if evento.key == pygame.K_f:
                        # Si se presiona la tecla "f", alternamos entre pantalla completa y ventana
                        pantalla_completa = not pantalla_completa
                    if pantalla_completa:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        info = pygame.display.Info()
                        window_width = info.current_w
                        window_height = info.current_h
                        pygame.display.set_caption(titulovent)
                    else:
                        window_width = 800
                        window_height = 600
                        screen = pygame.display.set_mode((window_width, window_height))
                        pygame.display.set_caption(titulovent)
            
            sec = dt.datetime.now().second
            min = dt.datetime.now().minute
            hou = dt.datetime.now().hour
            s = pygame.Surface((window_width,window_height))  # tamano del cuadro
            s.set_alpha(50)                # nivel alpha
            s.fill((0,0,0))           # llena el cuadrado de color negro RGB(0,0,0)
            screen.blit(s, (0,0))  

            # Muestra el tiempo en la ventana 
            time_text =str(hou).zfill(2)  +":"+str(min).zfill(2)+":" +str(sec).zfill(2)  
            text = font.render(time_text, True, color)  
            screen.blit(text, (window_width/2 - text.get_width()/2, window_height/2 - font_size2/2 ))
            pygame.display.flip()
            clock.tick(20)  # Actualiza la pantalla una vez por segundo
            
    else:
        #tipo no soportado
        a=3
    exit();

 




#--------------------------------------------------------------
# INICIO DEL PROGRAMA          #
#--------------------------------------------------------------



#leer parametros:
y = 1
if len(sys.argv) == 1:
    #Clock(font_size, color, tipo) # digital por defecto
    lossegundos=0
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
        elif  n=="-t":
            font_size=int(sys.argv[y]) # parametro para tameno de fuente, por defecto 150
        elif  n=="-c":
            #col=sys.argv[y] # parametro para tameno de fuente, por defecto color red
            col= (sys.argv[y]).lstrip('#')
            #print('h =',h)
            color=tuple(int(col[i:i+2], 16) for i in (0, 2, 4))
        elif  n=="-ti":
              titulovent=sys.argv[y] # parametro para nombre. por defecto "CLOCK"
              
        elif  n=="-f":
            pantalla_completa = True
        elif n=="-o":
            #clockjac2(450, (183,183,183))
            #clock(font_size, color, 'O') # FlipFlop, se envía color pero no lo usará
            tipo = 'O'
            pantalla_completa = True # siempre lo mando a pantalla completa!
            font_size= 600 # siempre lo mando tamaño minimo
        elif n=="-d":
            #clockjac2(450, (183,183,183))
            #clock(font_size, color, 'D') # Digital con opciones
            tipo = 'D'
        elif  n=="--help" :  
            print("Modo de empleo: Clock [opciones]...")
            print("")           
            print("Programa de consola que genera un reloj (digital o flipflop) y también una cuenta regresiva, simulando display de 7 segmentos, Para eso utiliza la fuente \"Digital-7\"; la cual hay que instalar en el sistema.")
            print("")            
            print("OPCIONES DE RELOJ")
            print("")
            print("clock -d")
            print("Crea un reloj digital, opción por defecto si no se especifica otra cosa")
            print("clock -o")
            print("Crea un reloj flipflop, ")
            print("")
            print("Ejemplo:")
            print("")
            print("clock -o -t 400 -f ")
            print("Crea reloj flip flop,  tamaño de fuente 400 y a pantalla completa ")
            print("")
            print("clock -c \"#e2943a\" -f -t 200 -ti HoraActual")
            print("Crea un reloj color ambar, a pantalla completa con hora de sistema, fuente tamano 200,  y titulo de la ventana \"HoraActual\"")

            print("OPCIONES DE CUENTA REGRESIVA")
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
            print("Ejemplo 2:")
            print("")
            print("clock -h 3 -c \"#e2943a\" -t 150  -ti Detonador")
            print("Crea una cuenta regresiva de tres horas, color ambar, con fuente tamano 150, y titulo de la ventana \"Detonador\"")    
            print("")
            print("")
            print("DURANTE LA EJECUCION")
            print("presionar") 
            print(" f   para alternar entre pantalla completa o ventana")
            print(" q   para salir")
            print(" +   para aumentar tamaño de la fuente")
            print(" -   para disminuir tamaño de la fuente")
            print("")
            
            print("")
            
            print("")
            
            print("")
            

            exit();

        y=y+1
    # Fin lectura de parámetros
 
##############################
# Configuracin de la pantalla#
##############################
        

pygame.init() 



if lossegundos == 0:
    Clock(font_size, color, tipo)
else:
    Countdown(lossegundos + 1, font_size, color)
    # si entra por acá es que es una cuenta regresiva, se envían las opciones.

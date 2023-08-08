# Programa de Reloj y Temporizador

El programa es una aplicación desarrollada en Python utilizando la biblioteca Pygame, diseñada para funcionar como un reloj digital y un temporizador de cuenta regresiva. Ofrece opciones para personalizar el tamaño de la fuente, el color del texto y el título de la ventana.

### Características Principales:

1. **Reloj Digital en Pantalla:**
   - El programa muestra en tiempo real la hora actual en formato de reloj digital.
   - Utiliza una fuente personalizada para simular un reloj de 7 segmentos.
   - ![Descripción de la imagen](img/imgR.png)

2. **Temporizador de Cuenta Regresiva:**
   - El usuario puede establecer un tiempo en horas, minutos o segundos para una cuenta regresiva.
   - La cuenta regresiva se muestra en pantalla en formato de reloj digital.
   - La cuenta regresiva disminuye cada segundo hasta llegar a cero.
   - - ![Descripción de la imagen](img/imgT.png)

3. **Personalización:**
   - El usuario puede personalizar el tamaño de la fuente y el color del texto del reloj y la cuenta regresiva.
   - También se puede cambiar el título de la ventana de la aplicación.

  Ejemplo:

    clock -c "#e2943a" -f 150 -h 3 -t Detonador
    
    clock -c "#e2943a" -f 150 -t HoraActual

   - El primero crea una cuenta hacia atras de tres horas con fuente tamano 150, color ambar, y titulo de la ventana "Detonador"
   - El segundo crea un reloj con hora de sistema, fuente tamano 150, color ambar, y titulo de la ventana "HoraActual"
     

4. **Efectos Visuales:**
   - Cuando la cuenta regresiva llega a cero, se muestra el mensaje "Time's up!" en rojo.
   - El mensaje también vibra rápidamente en su lugar.
   - - ![Descripción de la imagen](img/imgT2.png)

5. **Notificación de Sonido:**
   - Cuando la cuenta regresiva llega a cero, se reproduce un sonido de alarma.

6. **Interfaz de Usuario Amigable:**
   - La interfaz de usuario se ejecuta en una ventana visual.
   - El programa acepta argumentos de línea de comandos para configurar el temporizador y otras opciones.

### Uso y Aplicaciones:

Este programa es adecuado para diversas situaciones donde se requiera un reloj digital o un temporizador de cuenta regresiva. Puede ser útil en la gestión del tiempo, medición de intervalos, tareas temporizadas y recordatorios.

### Beneficios:

- Ofrece una solución visualmente atractiva y funcional para ver la hora actual y establecer temporizadores.
- Permite personalizar la apariencia y el comportamiento según las preferencias del usuario.
- Facilita la gestión del tiempo y las actividades con notificaciones visuales y sonoras.

En resumen, este programa es una herramienta versátil y personalizable para visualizar la hora actual y establecer temporizadores de cuenta regresiva, con opciones de personalización y efectos visuales que lo hacen práctico y entretenido de usar.

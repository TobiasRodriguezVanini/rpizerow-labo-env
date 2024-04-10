from gpiozero import LED, Button
#asigna las funciones LED y Button desde gpiozero
from signal import pause
#asigna la funcion pausa desde la libreria signal

led = LED(17)
button = Button(3)
#asigna el led al pin 17 y el boton al pin 3

button.when_pressed = led.on
#declara que el led debe encenderse cuando el boton este siendo presionado
button.when_released = led.off
#declara que el led debe estar apagado cuando el boton no este siendo presionado
 pause()
 

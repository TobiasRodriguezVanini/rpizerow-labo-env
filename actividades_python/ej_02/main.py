from gpiozero import LED
from time import sleep
#Variables de los LEDs a usar
rojo = LED(13)
azul = LED(19)
verde = LED(26)
#Contadores a usar y su valor inicial
cverde = 0
crojo = 0
cazul = 0
#Inicio un bucle
while True:
#Determino en que valor el LED verde debera estar encendido o apagado
	if cverde == 0:
		verde.on()
	if cverde == 1:
		verde.off()
#Determino que el contador verde debe sumar 1 a su valor constantemente y que debe reiniciarse cuando valga 2
		cverde=cverde+1
	if cverde==2:
		cverde==0
#Determino en que valor el LED verde debera estar encendido o apagado.
	if cazul < 2:
		azul.on()
	if cazul > 2:
		azul.off()
#Determino que el contador azul debe sumar 1 a su valor constantemente y que debe reiniciarse cuando valga 4
		cazul=cazul+1
	if cazul==4:
		cazul==0
#Determino los valores en los que el LED rojo debera estar encendido o apagado
	if crojo < 4:
		rojo.on()
	if crojo > 4:
		rojo.off()
#Determino que el contador rojo debera sumar 1 a su valor constantemente y que debe reiniciarse cuando valga 8
		crojo=crojo+1
	if crojo==8:
		crojo=0

sleep(0.25)

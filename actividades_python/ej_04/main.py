from gpiozero import PWMLED
import ADS1x15
import time
import math

# Indico el pin a usar para el I2C y el registro
ADS = ADS1x15.ADS1115(1,0x48)
ADS.setMode(ADS.MODE_SINGLE)

# Declaro que la ganancia ADC es de +-6,144V.
ADS.setGain(ADS.PGA_4_096V)

#Convierto el valor del ADC en un valor de tension. 
factor = ADS.toVoltage()

# Indico los pines 19 y 26 para el LED rojo y el LED azul, y los permito varias su intensidad en PWM.
LEDAzul = PWMLED(26)
LEDRojo = PWMLED(19)

# Determino valores para el calculo de temperatura
vcc = 3.3  
r = 10000  
to = 298.15
t= 0
rt = 0
# Constante del termistor
beta = 3900

while True:
    # Valores analógicos del potenciómetro y termistor
    ValorPote = ADS.readADC(3)
    ValorTerm = ADS.readADC(1)

    # Las convierto a sus valores de tension.
    TensionPote = ValarPote * factor
    TensionTerm = ValorTerm * factor

    # Cálculo de la resistencia del termistor
    rt = (r * VoltajeTerm) / (vcc - VoltajeTerm)

    # Conversión temperatura 
    t = beta / (math.log(rt / r) + (beta / t0))
    # Conversión grados Celsius
    t = t - 273.15  

    # Reduzco la escala de voltaje del potenciometro para trabajar solo entre los 0 y 30 °C
    TempPoten = (TensionPote / 3.3) * 30

    # Calculo la diferencia entre la temperatura deseada y la medida
    diff = abs(TempPote - t)

    # Limitor la diferencia de temperatura a un máximo de 5 grados
    if diff > 5:
        diff = 5

    # Control de los LEDs según la diferencia de temperatura
    if TempPote > t:
        LEDRojo.value = diff / 5  # Brillo proporcional a la diferencia
        LEDAzul.value = 0         # Apaga el LED Azul
    elif TempPote < t:
        LEDAzul.value = diff / 5  
        LEDRojo.value = 0         # Apago el LED Rojo
    else:
        LEDAzul.value = 0         # Apago ambos LEDs si no hay diferencia
        LEDRojo.value = 0

    # Enseño los valores conseguidos en la consola
    print("Termistor: {0:.3f} V, {1:.3f} °C".format(LecturaTermVoltaje, t))
    print("Potenciómetro: {0:.2f} °C".format(TempPote))

    time.sleep(1) 

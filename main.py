from machine import Pin
import time

led_verde = Pin(23, Pin.OUT)
led_amarelo = Pin(22, Pin.OUT)
led_vermelho = Pin(TX, Pin.OUT)


def desligar_todos():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)


while True:

    desligar_todos()
    led_vermelho.value(1)
    time.sleep(2)

    desligar_todos()
    led_verde.value(1)
    time.sleep(2)

    desligar_todos()
    led_amarelo.value(1)
    time.sleep(2)

#Wokwi simulator link: https://wokwi.com/projects/481615445291334657

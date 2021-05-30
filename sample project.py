from gpiozero import LED
from time import sleep


# bled = LED(5)
# Lled = LED(7)
# Lled = LED(11)
def toggle(pinNo):
    led = LED(pinNo)
    sleep(.8)
    led.off()
    sleep(.4)

forward  = 2
backward = 3
left     = 4
right    = 17


while True:
    a = input("Enter the Direction")
    
    if a == 'fw':
        for i in range(3):
            toggle(forward)
        print("forward")
    if a == 'bk':
        for i in range(3):
            toggle(backward)
        print("backward")
    if a == 'lt':
        for i in range(3):
            toggle(left)
        print("left")
    if a == 'rt':
        for i in range(3):
            toggle(right)
        print("right")            
    if a == 'q':
        break
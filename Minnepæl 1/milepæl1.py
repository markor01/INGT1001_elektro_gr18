from sense_hat import sense_hat
from time import sleep

senseHat = SenseHAt()


# Konstanter
a = 0.0065
R = 287.06
g_0 = 9.81 
N = 200 

# Variabler
T_1 = 16 + 273.15 
p_1 = 100000    # Trykket målt i høyden h_1
h_1 = 0         # Vi gjør målingene relative dersom vi ønsker, ved å sette h_1 = 0

def calc_pressure_Pa():
    p = 0 
    for _ in range(N):
        p += senseHat.pressure 
        sleep(0.001)
    return p*100/N # Vi vil ha p i Pa, og multipliserer derfor med 100 etter vi deler på N


def stick_down():
    for e in senseHat.stick.get_events():
        if e.direction=='down':
            return 1

while True:

    senseHat.show_message("Venstre: mål - Høyre: Kalibrer - Ned: Avbryt", 0.05)

    event = senseHat.stick.wait_for_event()

    if event.direction == 'left':
        while stick_down()!=1:
            p = calc_pressure_Pa()
            h = (T_1 / a) * ( (p/p_1)**(-a*R/g_0) -1 ) + h_1
            senseHat.show_message(str(round(h,2))+"m",0.07)

    if event.direction == 'right':
        while stick_down()!=1:
            T_1 = senseHat.temp + 273.15
            p_1 = calc_pressure_Pa()
            senseHat.show_message(str(int(p_1))+" Pa "+str(T_1)+" K ", 0.07)



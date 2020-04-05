# Project 2 Python Code

from Force_Functions import air_form, air_friction, water_form, water_friction
from math import pi

dt = 60 * 60  # time step of 1 hour
T = 21 * 24 * 60 * 60  # total time of 30 days

# motion values
v_0 = 0
x_0 = 0

dist = 4500000

water_needed = 10000000

p_air = 1.225
p_water = 1030
p_ice = 920

a = 2 * dist / (T ** 2)

print(a)
print(a * 10000000000)

melting_rate = 0.002  # m/s

# tabular
tab_w = 10
tab_h = 10
tab_l = 10


def tab_mass(t):
    V = (tab_w - melting_rate * t) * \
        (tab_h - melting_rate * t) * (tab_l - melting_rate * t)
    return(p_ice * V)


# dome
dome_r = 10
dome_h = 10


def dome_mass(t):
    V = (4 / 3 * pi * ((dome_r - melting_rate * t) ** 3))
    V += (pi * ((dome_r - melting_rate * t) ** 2) * (dome_h - melting_rate * t))
    return(p_ice * V)


# wedged
wedge_ha = 10
wedge_hb = 10
wedge_l = 10
wedge_w = 10


def wedge_mass(t):
    loss = melting_rate * t
    V = (1 / 2 * (wedge_l - loss) * (wedge_ha - loss))
    V += (wedge_hb - loss) * (wedge_l - loss) * (wedge_w - loss)
    return(V)


# pinnacle
pin_ha = 10
pin_hb = 10
pin_lw = 10


def pin_mass(t):
    loss = melting_rate * t
    V = (1 / 3 * (pin_ha - loss) * (pin_lw - loss) * (pin_lw - loss))
    V += (1 / 3 * (pin_hb - loss) * (pin_lw - loss) * (pin_lw - loss))


for i in range(0, T, dt):
    pass

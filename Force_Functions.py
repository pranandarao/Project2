
p_air = 1.225
p_water = 1030

c_air = 0.1
c_water = 0.5

v_c = 4

def air_friction(A_wetted, v_app):
    return(-1 / 2 * p_air * A_wetted * c_air * (v_app ** 2))


def water_friction(A_wetted, v_app):
    return(-1 / 2 * p_water * A_wetted * c_water * (v_app ** 2))


def air_form(A_frontal, v_app):
    return(-1 / 2 * p_air * A_frontal * c_air * (v_app ** 2))


def water_form(A_frontal, v_app):
    return(-1 / 2 * p_water * A_frontal * c_water * (v_app ** 2))


def tow_force(A_wetted_air, A_wetted_water, A_frontal_air, A_frontal_water, v):
    tow = air_friction(p_air, A_wetted_air, c_air, v) + water_friction(p_water, A_wetted_water, c_water, v - v_c) + \
        air_form(p_air, A_frontal_air, c_air, v) + \
        water_friction(p_water, A_frontal_water, c_water, v - v_c)
    return(tow)






a = 2 * dist / (T ** 2)

print(a)

# tabular
init_mass = (((water_needed / p_ice) ** (1 / 3) + melting_rate * T) ** 3) * p_ice
tab_w = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T)
tab_h = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T)
tab_l = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T)

print(tab_w)

def tab_mass(t):
    V = (tab_w - melting_rate * t) * \
        (tab_h - melting_rate * t) * (tab_l - melting_rate * t)
    return(p_ice * V)

def tab_SA(t):
    loss = melting_rate * t
    wetted_air = 2 * 0.1 * (tab_h - loss) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
    frontal_air = 0.1 * (tab_h - loss) * (tab_w - loss)
    wetted_water = 2 * 0.9 * (tab_h - loss) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
    frontal_water = 0.9 * (tab_h - loss) * (tab_w - loss)
    return([wetted_air, frontal_air, wetted_water, frontal_water])

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

def pin_mass(t):
    loss = melting_rate * t
    V = (1 / 3 * (pin_ha - loss) * (pin_lw - loss) * (pin_lw - loss))
    V += (1 / 3 * (pin_hb - loss) * (pin_lw - loss) * (pin_lw - loss))


# pinnacle
pin_ha = 1000
pin_hb = 1000
pin_lw = 1000

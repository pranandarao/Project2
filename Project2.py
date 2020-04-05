# Project 2 Python Code

import matplotlib.pyplot as plt
#import seaborn as sns

#sns.set()

dt = 30 * 60  # time step of 1 hour

p_air = 1.225
p_water = 1030
p_ice = 920

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


def tow_force(A_wetted_air, A_wetted_water, A_frontal_air, A_frontal_water, v, mass, acc):
    tow = mass * acc - air_friction(A_wetted_air, v) - water_friction(A_wetted_water, v - v_c) - \
        air_form(A_frontal_air, v) - \
        water_friction(A_frontal_water, v - v_c)
    return(tow)


# motion values

dist = 3750000

water_needed = 1.25 * (10 ** 6) # in kL

water_needed *= 1000 # coverting to kg

melting_rate = 0.00002  # m/s

def tow_force_time(T):
    time = [i for i in range(0, T * 24 * 60 * 60, dt)]

    T_curr = T * 24 * 60 * 60
    a = 2 * dist / ((T_curr) ** 2)

    init_mass = (((water_needed / p_ice) ** (1 / 3) + melting_rate * T_curr) ** 3) * p_ice
    
    tab_w = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T_curr)
    tab_h = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T_curr)
    tab_l = ((water_needed / p_ice) ** (1 / 3) + melting_rate * T_curr)
    
    t_force = []
    v = 0

    print(tab_w)

    def tab_mass(t):
        V = (tab_w - melting_rate * t) * (tab_h - melting_rate * t) * (tab_l - melting_rate * t)
        return(p_ice * V)

    def tab_SA(t):
        loss = melting_rate * t
        wetted_air = 2 * 0.1 * (tab_h - loss) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
        frontal_air = 0.1 * (tab_h - loss) * (tab_w - loss)
        wetted_water = 2 * 0.9 * (tab_h - loss) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
        frontal_water = 0.9 * (tab_h - loss) * (tab_w - loss)
        return([wetted_air, frontal_air, wetted_water, frontal_water])

    for i in time:
        SA = tab_SA(i)
        mass = tab_mass(i)

        t_force.append(tow_force(SA[0], SA[2], SA[1], SA[3], v, mass, a))

        v += a * dt
        # print(v)

    plt.figure(T)
    plt.plot(time, t_force)
    plt.title('Time: ' + str(T) + ' days')

if __name__ == '__main__':
    T_poss = [i for i in range(1, 102, 10)]
    for i in T_poss:
        tow_force_time(i)
    plt.show()

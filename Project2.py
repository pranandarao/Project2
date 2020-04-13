# Project 2 Python Code

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

dt = 30 * 60  # time step of 1 hour

p_air = 1.225
p_water = 1030
p_ice = 920

c_air = 0.1
c_water = 0.5

v_c = 1


def air_friction(A_wetted, v_app):
    return (-1 / 2 * p_air * A_wetted * (4.55 * 10 ** (-3)) * (v_app ** 2))


def water_friction(A_wetted, v_app):
    return (-1 / 2 * p_water * A_wetted * (2 * 10 ** (-3)) * (v_app ** 2))


def air_form(A_frontal, v_app):
    return (-1 / 2 * p_air * A_frontal * (0.9) * (v_app ** 2))


def water_form(A_frontal, v_app):
    return (-1 / 2 * p_water * A_frontal * (0.9) * (v_app ** 2))


def tow_force(A_wetted_air, A_wetted_water, A_frontal_air, A_frontal_water, v, mass, acc):
    tow = mass * acc - air_friction(A_wetted_air, v) - water_friction(A_wetted_water, v - v_c) - \
          air_form(A_frontal_air, v) - \
          water_friction(A_frontal_water, v - v_c)
    return (tow)


# motion values

# water_needed = 3.74 * (10 ** 12) / 1000 * 0.2 * 0.12 # in kL
# water_needed = 89760000 # in kL (1/5 of CapeTown's Domestic Usage per year)

water_needed = float(input('What is the volume of water needed in Cape Town (in kL)? '))

#dist = 3300000 in meters (1 way)
dist = float(input('What is the distance to Cape Town (in m)? '))

water_needed *= 1000  # converting to kg

melting_rate = 0.000002  # m/s


def tow_force_time(T):
    time = [i for i in range(0, T * 24 * 60 * 60, dt)]

    T_curr = T * 24 * 60 * 60
    a = 2 * dist / ((T_curr) ** 2)

    init_mass = (((water_needed / p_ice) ** (1 / 3) + melting_rate * T_curr) ** 3) * p_ice

    tab_w = ((water_needed / p_ice) ** (1 / 3) + 0.000009872 * T_curr) * 10
    tab_h = ((water_needed / p_ice) ** (1 / 3) + 0.0000006886 * T_curr) / 10
    tab_l = ((water_needed / p_ice) ** (1 / 3) + 0.000009872 * T_curr)



    t_force = []
    v = 0

    print('Days: ' + str(T) + ', dimension: ' + str(tab_l) + ', ' + str(tab_w) + ', ' + str(tab_h))

    def tab_mass(t):
        loss = 0.000009872 * t
        V = (tab_w - loss) * (tab_h - 0.0000006886 * t) * (tab_l - loss)
        return (p_ice * V)

    def tab_SA(t):
        loss = 0.000009872 * t
        wetted_air = 2 * 0.1 * (tab_h - 0.0000006886 * t) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
        frontal_air = 0.1 * (tab_h - 0.0000006886 * t) * (tab_w - loss)
        wetted_water = 2 * 0.9 * (tab_h - 0.0000006886 * t) * (tab_l - loss) + (tab_l - loss) * (tab_w - loss)
        frontal_water = 0.9 * (tab_h - 0.0000006886 * t) * (tab_w - loss)
        return ([wetted_air, frontal_air, wetted_water, frontal_water])
    
    def totCost(T, t_force, tab_l, tab_w, tab_h):
        numShips = (1 + int( max(t_force) / (309 * 9.8 * 1000 ) )) # Number of Ships needed
        shipCost = ( (40000 * T) * numShips )                      # Cost of ALP Striker Usage
        fuelCost = 1083806.4 * (int(T/45) + 1) * numShips          # Fuel cost (assumes complete fill for 45 days and that refill transport cost = $0)
        netMeters = (16 * (.25 * tab_h)) + 2 * (( tab_w + 2*tab_l) + 2*(((tab_w / 2)**2 + 2000**2)**(0.5))) # Boat will tow 2km in front of iceberg
        netCost = 112.53 * netMeters                               # Dyneema rope net design
        laborCost = (13.91 * 12 * 35) * numShips * T               # Assumes full 35 mates working 12 hr / day @ $13.91 / hr  
        cost = shipCost + fuelCost + netCost + laborCost
        return(cost)

    for i in time:
        SA = tab_SA(i)
        mass = tab_mass(i)

        t_force.append(tow_force(SA[0], SA[2], SA[1], SA[3], v, mass, a))

        v += a * dt
        
    
    print('Days: ' + str(T) + ', final velocity: ' + str(v))

    print('Days: ' + str(T) + ', max tow force: ' + str(max(t_force)) + ' N')
    
    totalCost = totCost(T, t_force, tab_l, tab_w, tab_h)
    
    print('Days:'  + str(T) + ', total cost: $'  + str(totalCost) + '\n')
    

    

    plt.figure(T)
    plt.plot(time, t_force)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Towing Force (Newtons)')
    plt.title('Travel Time: ' + str(T) + ' days')


if __name__ == '__main__':
    T_poss = [i for i in range(10, 102, 10)]
    # T_poss = [50]
    for i in T_poss:
        tow_force_time(i)
    plt.show()

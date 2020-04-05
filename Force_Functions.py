
def air_friction(p_air, A_wetted, c_air, v_app):
    return(1 / 2 * p_air * A_wetted * c_air * (v_app ** 2))


def water_friction(p_water, A_wetted, c_water, v_app):
    return(-1 / 2 * p_water * A_wetted * c_water * (v_app ** 2))


def air_form(p_air, A_frontal, c_air, v_app):
    return(1 / 2 * p_air * A_frontal * c_air * (v_app ** 2))


def water_form(p_water, A_frontal, c_water, v_app):
    return(-1 / 2 * p_water * A_frontal * c_water * (v_app ** 2))


def tow_force(p_air, p_water, A_wetted_air, A_wetted_water, A_frontal_air, A_frontal_water, c_air, c_water, v_app):
    tow = air_friction(p_air, A_wetted_air, c_air, v_app) + water_friction(p_water, A_wetted_water, c_water, v_app) + \
        air_form(p_air, A_frontal_air, c_air, v_app) + \
        water_friction(p_water, A_frontal_water, c_water, v_app)
    return(tow)

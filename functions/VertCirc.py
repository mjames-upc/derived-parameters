def execute(wind, pvv):
    """ Combine wind with PVV to prepare the data for Cross Section to do Vertical Circulation Calculations
    
    """
    return (wind[0], wind[1], pvv )

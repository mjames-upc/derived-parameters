from LyrQvec import calculate as lyrQvec

def execute(height_up, height_lo, pressure_up, pressure_lo, dx, dy, coriolis):
    qx, qy, dtdx, dtdy  = lyrQvec(height_up, height_lo, pressure_up, pressure_lo, dx, dy, coriolis)
    
    fgen = qx * dtdx
    fgen -= qy * dtdy
    fgen *= 2
    
    return fgen

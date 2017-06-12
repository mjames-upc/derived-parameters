def execute(uStk, vStk, RM5):

    umot,vmot = RM5
    u1 = uStk[0]
    v1 = vStk[0]
    u2 = uStk[-1]
    v2 = vStk[-1]
    # First do our motion, lower bulk shear computation.
    hptr = (v2-v1)*umot+(u1-u2)*vmot
    for i in range(1, len(uStk)):
        u1 = uStk[i-1]
        v1 = vStk[i-1]
        u2 = uStk[i]
        v2 = vStk[i]
        hptr += u2*v1-u1*v2
    return hptr

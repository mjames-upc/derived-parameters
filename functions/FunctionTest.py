def execute(*args):
    """Test all derived functions for proper operation
    
    """
    
    import Vector
    reload(Vector)
    Vector.test()
    
    import Add
    reload(Add)
    Add.test()
    
    import Multiply
    reload(Multiply)
    Multiply.test()
    
    import Divide
    reload(Divide)
    Divide.test()
    
    import Difference
    reload(Difference)
    Difference.test()
    
    import Poly
    reload(Poly)
    Poly.test()
    
    import Average
    reload(Average)
    Average.test()
    
    import LinTrans
    reload(LinTrans)
    LinTrans.test()
    
    import Test
    reload(Test)
    Test.test()
    
    import Rotate
    reload(Rotate)
    Rotate.test()
    
    import Magnitude
    reload(Magnitude)
    Magnitude.test()
    
    import Cape
    reload(Cape)
    Cape.test()
    
    print "-"*60
    print "Function Test Complete"
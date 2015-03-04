import myLogger

def TestLogger():
    test = myLogger.myLogger()
    test.LogDebug('Some Random Debug message!', 2)
    test.LogWarning('Some Random warning message!', 2)
    test.LogInfo('Some Random Info message!', 2, 'kscavitt')
    
TestLogger()  

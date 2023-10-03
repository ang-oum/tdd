import unittest
#_________________________________________________________________________________
#  Classes & functions
#_________________________________________________________________________________
# return is only used here for convenient representation



'''
class unittest.TestCase(methodName='runTest'):
'''
class myTestCase(unittest.Testcase):
    def setUp():
        return
    def tearDown():
        return
    def setUpClass():
        return
    def run():
        return
    def skipTest():
        return
    def subTest():
        return
    def debug():
        return
    
    def assertEqual(self, Testcase):
        return
    def assertNotEqual(self, Testcase):
        return
    
    def assertTrue():
        return
    def assertFalse():
        return
    
    def assertIs():
        return
    def assertIsNone():
        return
    
    def assertIn():
        return
    def assertNotIn():
        return
    
    def assertIsInstance():
        return
    def assertNotIsInstance():
        return

    def assertRaises():
        return
    def assertRaisesRegex():
        return
    
    def assertWarns():
        return
    def assertWarnsRegex():
        return
    
    def assertLogs():
        return
    def assertNoLogs():
        return
    
    def assertAlmostEqual(self, Testcase):
        return
    def assertNotAlmostEqual(self, Testcase):
        return
        
    def assertGreater():
        return
    def assertGreaterEqual():
        return
    def assertLess():
        return
    def assertLessEqual():
        return
    
    def assertRegex():
        return
    def assertNotRegex():
        return

    def assertCountEqual():
        return
    def assertMultiLineEqual():
        return
    def assertSequenceEqual():
        return
    def assertListEqual():
        return
    def assertTupleEqual():
        return
    def assertSetEqual():
        return
    def assertDictEqual():
        return

    def fail():
        return
    # attributes
        '''
        failureException
        longMessage
        maxDiff
        '''
    
    #collect-test-data
    def countTestCases():
      return
    def defaultTestResult():
        return
    def id():
        return
    def shortDescription():
        return
    def addCleanup():
        return
    def enterContext():
        return
    def doCleanups():
        return
    
    #classmethod
    def addClassCleanup():
        return
    def enterClassContext():
        return
    def doClassCleanups():
        return
    

'''
class unittest.IsolatedAsyncioTestCase(methodName='runTest'):
'''
class myIsoAsyncCase(unittest.IsolatedAsyncioTestCase):

    #coroutine
    def asyncSetup():
        return
    def asyncTearDown():
        return
    def enterAsyncContext():
        return
    
    def addAsyncCleanup():
        return
    def run():
        return



#____________________________________________________________________
# grouping tests
'''
class unittest.TestSuite(tests=())
'''
class mySuite(unittest.TestSuite):
    def addTest():
        return
    def addTests():
        return
    def run():
        return
    def debug():
        return
    def countTestCases():
        return
    def __iter__():
        return


#____________________________________________________________________
# loading & running tests
'''
unittest.defaultTestLoader
'''
class myInstanceOfTestLoader(unittest.defaultTestLoader):
    def discover():
        return
'''
class unittest.TestLoader
'''
class myLoader(unittest.TestLoader):
    # attributes
    '''
    errors
    '''
    def loadTestsFromTestCase():
         return
    def loadTEstsFromModule():
        return
    def loadTestsFromName():
        return
    def loadtestsFromNames():
        return
    def getTestCaseNames():
        return
    def discover():
        return
    # The following attributes of a TestLoader 
    # can be configured either by subclassing 
    # or assignment on an instance:
    '''
    testmethodPrefix
    sortTestMethodUsing
    suiteClass
    testNamePatterns
    '''


'''
class unittest.TestResult
'''
class myResults(unittest.TestResult):
    # attributes
    '''
    errors
    failures
    skipped
    expectedFailures
    unexpectedSuccesses
    shouldStop
    testsRun
    buffer
    failfast
    tb_locals
    '''
    def wasSuccessful():
        return
    def stop():
        return
    def startTest():
        return
    def stopTest():
        return
    def startTestRun():
        return
    def stopTestRun():
        return
    def addError():
        return
    def addFailure():
        return
    def addSuccess():
        return
    def addSkip():
        return
    def addExpectedFailure():
        return
    def addUnexpectedSuccess():
        return
    def addSubTest():
        return
    

'''
class unittest.TextTestResult(stream, descriptions, verbosity)
'''
class myTextResults(unittest.TextTestResult):
    def addSkip():
        return
    
'''
class unittest.TextTestRunner(stream=None, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None, warnings=None, *, tb_locals=False)
'''
class myTextRunner(unittest.TextTestRunner):
    def _makeResult():
        return
    def run():
        return
    
'''
unittest.main(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=unittest.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None)
'''
#_____________________________________________________
#              Basic example
#_____________________________________________________
import unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#_________________________________________________________
#      IsoAsyncCase Example
#_________________________________________________________
from unittest import IsolatedAsyncioTestCase

events = []


class Test(IsolatedAsyncioTestCase):


    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        '''
        self._async_connection = await AsyncConnection()
        '''
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")

if __name__ == "__main__":
    unittest.main()

#  After running the test
#  events = ["setUp", "asyncSetUp", "test_response", "asyncTearDown", "tearDown", "cleanup"].






#_____________________________________________________
#              ORGANIZING TEST CODE
#_____________________________________________________

#_____________________________________________________
#              Test case:
#_____________________________________________________


import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        '''
        self.widget = Widget('The widget')
        '''

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
    def tearDown(self):
        self.widget.dispose()


#_____________________________________________________
#              Test suite:
# collection of test cases, test suites, or both.
# Uused to aggregate tests that should be executed together.
#_____________________________________________________


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


#_____________________________________________________
#              Reusing old test code
#_____________________________________________________

#_____________________________________________________
#        Skipping tests & expected failures
#_____________________________________________________


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")
    '''
    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass
    

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
    '''
#output:
'''
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)

'''

#_________________________________________________________
#       Classes can be skipped just like methods:

@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
#_________________________________________________________
#       Expected failures use the expectedFailure() decorator.

class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

#_________________________________________________________
# It’s easy to roll your own skipping decorators 
# by making a decorator that calls skip() on the test 
# when it wants it to be skipped. 
# This decorator skips the test unless the passed object has a certain attribute:

def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))



'''
@unittest.skip(reason)
Unconditionally skip the decorated test. reason should describe why the test is being skipped.

@unittest.skipIf(condition, reason)
Skip the decorated test if condition is true.

@unittest.skipUnless(condition, reason)
Skip the decorated test unless condition is true.

@unittest.expectedFailure
Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in one of the test fixture methods) then it will be considered a success. If the test passes, it will be considered a failure.

exception unittest.SkipTest(reason)
This exception is raised to skip a test.

Usually you can use TestCase.skipTest() or one of the skipping decorators instead of raising this directly.

'''

#_________________________________________________________
# Distinguishing test iterations using subtests
#_________________________________________________________

# subTest()
class myTestCase(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)





#_________________________________________________________________________________
#  Classes & functions
#_________________________________________________________________________________
# return is only used here for convenient representation



'''
class unittest.TestCase(methodName='runTest'):
'''
class myTestCaset(unittest.Testcase):
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
#_________________________________________________________________________________
#  Load_tests(loader, standard_tests, pattern)                   # protocol
#_________________________________________________________________________________


#_________________________________________________________________________________
#  Class & module fixtures
#_________________________________________________________________________________

#________________________________________
# setUpClass & tearDownClass

#________________________________________
# setUpModule & tearDownModule

#_________________________________________________________________________________
#  Signal handling
#_________________________________________________________________________________




    





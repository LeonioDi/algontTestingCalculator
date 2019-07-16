import unittest
import calculations_tests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(calculations_tests)
testResult = unittest.TestResult()
runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(suites)
print('Всего{} Ошибки: {} Неудачи:{} Пропущено{}'.format(testResult.testsRun, len(testResult.errors),
                                                         len(testResult.failures), len(testResult.skipped)))

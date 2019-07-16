import configparser, os,time
import unittest

import datetime
from selenium import webdriver
from webCalculator import WebCalculator
from logger import MyLogger


class CalcucatorPositiveTestcase(unittest.TestCase, MyLogger):
    def __parse_config(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        self.config = config

    @property
    def __app_link(self):
        return self.config['TEST_LINK'].get('AppLink')

    @property
    def __screenshot_dirpath(self):
        return self.config['LOGGER'].get('ScreenshotDirPath', 'screenshots')

    def setUp(self):  # Данный метод выполняется перед каждым тестом
        self.__parse_config('./config.ini')
        self.driver = webdriver.Chrome()
        self.driver.get(self.__app_link)
        self.calculator = WebCalculator(self.driver)
        self.log = MyLogger('TestCaseLog').logger()

    def log_fail(self, error_msg, step_name):
        dt = datetime.datetime.today()
        curr_time_format = dt.strftime("%Y-%m-%d-%H.%M.%S")
        screenshot_path = os.path.join(
            self.__screenshot_dirpath, '{}{}.png'.format(step_name, curr_time_format))
        self.driver.save_screenshot(screenshot_path)
        self.log.error(error_msg)
        self.fail()

    # Основные сценарии

    def test_bruteforce(self):  # Проверка нажатия всех кнопок
        commands = [self.calculator.key_1_XPath, self.calculator.key_2_XPath, self.calculator.key_3_XPath,
                    self.calculator.key_4_XPath, self.calculator.key_5_XPath,
                    self.calculator.key_6_XPath, self.calculator.key_7_XPath, self.calculator.key_8_XPath,
                    self.calculator.key_9_XPath, self.calculator.key_0_XPath]
        try:
            self.calculator.execute_commands(commands)
        except Exception as e:
            self.log_fail('Тест: test_bruteforce не пройден {}'.format(e), 'test_bruteforce_FAIL_')

    def test_addition(self):  # Проверка операции сложения на примере 1 + 5 = 6
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '6'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_addition не пройден {}'.format(e), 'test_addition_FAIL_')

    def test_subtraction(self):  # Проверка операции вычетанеия на примере 9 - 5 = 4
        commands = [
            self.calculator.key_9_XPath,
            self.calculator.key_subtraction_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '4'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_subtraction не пройден {}'.format(e), 'test_subtraction_FAIL_')

    def test_multiplication(self):  # Проверка операции умножения на примере 3 х 4 = 12

        commands = [
            self.calculator.key_3_XPath,
            self.calculator.key_multiplication_XPath,
            self.calculator.key_4_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '12'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_multiplication не пройден {}'.format(e), 'test_multiplication_FAIL_')

    def test_division(self):  # Проверка операции деления на примере 8 / 4 = 2
        commands = [
            self.calculator.key_8_XPath,
            self.calculator.key_division_XPath,
            self.calculator.key_4_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '2'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_division не пройден {}'.format(e), 'test_division_FAIL_')

    def test_clear(self):  # Проверка операции очистки AC
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_2_XPath,
            self.calculator.key_3_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_clear_XPath
        ]
        expected_res = '0'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_clear не пройден {}'.format(e), 'test_clear_FAIL_')

    def test_point(self):  # Проверка простановки точки для дробных чисел(.)
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_2_XPath,
            self.calculator.key_3_XPath,
            self.calculator.key_point_XPath,
            self.calculator.key_3_XPath,
            self.calculator.key_2_XPath,
            self.calculator.key_1_XPath
        ]
        expected_res = '123.321'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_point не пройден {}'.format(e), 'test_point_FAIL_')

    def test_change_sign(self):  # Проверка изменения знака числа (+/-)
        commands = [
            self.calculator.key_5_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_change_sign_XPath,
        ]
        expected_res = '-555'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_change_sign не пройден {}'.format(e), 'test_change_sign_FAIL_')

    def test_percent(self):  # Проверка расчета процента для числа 100 % от 100 = 1
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_0_XPath,
            self.calculator.key_0_XPath,
            self.calculator.key_percent_XPath,
        ]
        expected_res = '1'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_percent не пройден {}'.format(e), 'test_percent_FAIL_')

    # Комбинаторика основных сценариев сценарии (в данном случае кейсы расписываются из условия, что после первого действия автоматом считается резщультат )

    def test_addition_combination(
            self):  # Проверка операции сложения, после другого математического действия, например 3 - 1 + 5 = 7
        commands = [
            self.calculator.key_3_XPath,
            self.calculator.key_subtraction_XPath,
            self.calculator.key_1_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '7'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_addition_combination не пройден {}'.format(e), 'test_addition_combination_FAIL_')

    def test_subtraction_combination(
            self):  # Проверка операции вычетанеия, после другого математического действия, например 9 + 9 - 7 = 11
        commands = [
            self.calculator.key_9_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_9_XPath,
            self.calculator.key_subtraction_XPath,
            self.calculator.key_7_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '11'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_subtraction_combination не пройден {}'.format(e),
                          'test_subtraction_combination_FAIL_')

    def test_multiplication_combination(
            self):  # Проверка операции умножения, после другого математического действия, например (3 + 4) х 2 = 14

        commands = [
            self.calculator.key_3_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_4_XPath,
            self.calculator.key_multiplication_XPath,
            self.calculator.key_2_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '14'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_multiplication_combination не пройден {}'.format(e),
                          'test_multiplication_combination_FAIL_')

    def test_division_combination(
            self):  # Проверка операции деления, после другого математического действия, например (6 + 6) / 4 = 3
        commands = [
            self.calculator.key_6_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_6_XPath,
            self.calculator.key_division_XPath,
            self.calculator.key_4_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '3'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_division_combination не пройден {}'.format(e), 'test_division_combination_FAIL_')

    def test_clear_combination(
            self):  # Проверка операции очистки AC, после математического действия, например (1 + 1) AC 4 = 4
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_1_XPath,
            self.calculator.key_clear_XPath,
            self.calculator.key_4_XPath
        ]
        expected_res = '4'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_clear_combination не пройден {}'.format(e), 'test_clear_combination_FAIL_')

    def test_point_combination(
            self):  # Проверка простановки точки для дробных чисел(.), после математического действия, например 1 + 1.5 = 2.5
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_1_XPath,
            self.calculator.key_point_XPath,
            self.calculator.key_5_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '2.5'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_point_combination не пройден {}'.format(e), 'test_point_combination_FAIL_')

    def test_change_sign_combination(
            self):  # Проверка изменения знака числа (+/-), после математического действия, например 5 + (-1) = 4
        commands = [
            self.calculator.key_5_XPath,
            self.calculator.key_addition_XPath,
            self.calculator.key_1_XPath,
            self.calculator.key_change_sign_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '4'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_change_sign_combination не пройден {}'.format(e),
                          'test_change_sign_combination_FAIL_')

    def test_percent_combination(self):  # Проверка расчета процента в математическом действии, например 100 - 30% = 70
        commands = [
            self.calculator.key_1_XPath,
            self.calculator.key_0_XPath,
            self.calculator.key_0_XPath,
            self.calculator.key_subtraction_XPath,
            self.calculator.key_3_XPath,
            self.calculator.key_0_XPath,
            self.calculator.key_percent_XPath,
            self.calculator.key_equality_XPath
        ]
        expected_res = '70'
        try:
            self.calculator.execute_commands(commands)
            assert self.calculator.find_node(self.calculator.key_result_XPath).text == expected_res
        except Exception as e:
            self.log_fail('Тест: test_percent_combination не пройден {}'.format(e), 'test_percent_combination_FAIL_')

    def tearDown(self):  # После каждого теста закрываем окно браузера
        self.driver.quit()

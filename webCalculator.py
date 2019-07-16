class WebCalculator:
    def __init__(self, driver):
        self.key_1_XPath = '//*[@id="root"]/div/div[2]/div[4]/div[1]'
        self.key_2_XPath = '//*[@id="root"]/div/div[2]/div[4]/div[2]'
        self.key_3_XPath = '//*[@id="root"]/div/div[2]/div[4]/div[3]'
        self.key_4_XPath = '//*[@id="root"]/div/div[2]/div[3]/div[1]'
        self.key_5_XPath = '//*[@id="root"]/div/div[2]/div[3]/div[2]'
        self.key_6_XPath = '//*[@id="root"]/div/div[2]/div[3]/div[3]'
        self.key_7_XPath = '//*[@id="root"]/div/div[2]/div[2]/div[1]'
        self.key_8_XPath = '//*[@id="root"]/div/div[2]/div[2]/div[2]'
        self.key_9_XPath = '//*[@id="root"]/div/div[2]/div[2]/div[3]'
        self.key_0_XPath = '//*[@id="root"]/div/div[2]/div[5]/div[1]'
        self.key_point_XPath = '//*[@id="root"]/div/div[2]/div[5]/div[2]'
        self.key_equality_XPath = '//*[@id="root"]/div/div[2]/div[5]/div[3]'
        self.key_addition_XPath = '//*[@id="root"]/div/div[2]/div[4]/div[4]'
        self.key_subtraction_XPath = '//*[@id="root"]/div/div[2]/div[3]/div[4]'
        self.key_multiplication_XPath = '//*[@id="root"]/div/div[2]/div[2]/div[4]'
        self.key_clear_XPath = '//*[@id="root"]/div/div[2]/div[1]/div[1]'
        self.key_change_sign_XPath = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.key_percent_XPath = '//*[@id="root"]/div/div[2]/div[1]/div[3]'
        self.key_division_XPath = '//*[@id="root"]/div/div[2]/div[1]/div[4]'
        self.key_result_XPath = '//*[@id="root"]/div/div[1]/div'
        self.driver = driver

    def click_key(self, node):
        node.click()

    def find_node(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def execute_commands(self, commands=[]):
        for command in commands:
            self.click_key(self.find_node(command))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import logging
import utilities.custom_logger as cl
import time
import os

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        :param resultMessage:
        :return:
        """

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotFolder = "../screenshots/"
        relativeFilePath = screenshotFolder + fileName
        currentFolder = os.path.dirname(__file__)
        destinationFilePath = os.path.join(currentFolder, relativeFilePath)
        destinationFolder = os.path.join(currentFolder, screenshotFolder)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            self.driver.save_screenshot(destinationFilePath)
            self.log.info("Screenshot saved to: " + destinationFilePath)
        except:
            self.log.error("### Exception Occured")
            print_stack()

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'tag':
            return By.TAG_NAME
        else:
            self.log.info('Locator type: {0} not correct/supported'.format(locatorType))
            return ''

    def getUrl(self, url = None):
        try:
            self.driver.get(url)
            self.log.info('Get page with URL :: {0}'.format(url))
        except:
            self.log.error('Can not get page with URL :: {0}'.format(url))
            print_stack()

    def getElement(self, locator, locatorType = 'id'):
        element = None
        try:
            element = self.driver.find_element(self.getByType(locatorType), locator)
            self.log.info('Element found with locator :: {0} and locator type :: {1}'.format(locator, locatorType))
        except:
            self.log.error('No element found with locator :: {0} and locator type :: {1}'.format(locator, locatorType))
            print_stack()
        return element

    def getElementList(self, locator, locatorType = 'id'):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Found :: {0} with locator :: {1} and locator type :: {2}".format(len(elements), locator, locatorType))
        except:
            self.log.error('No elements found with locator :: {0} and locator type :: {1}\''.format(locator, locatorType))
            print_stack()
        return elements

    def getTitle(self):
        try:
            title = self.driver.title
            self.log.info('Found page title :: ' + title)
            return title
        except:
            self.log.error('Exception occured while getting the page title :: ' + title)
            print_stack()

    def elementClick(self, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info('Clicked on element with locator :: {0} locator type:: {1}'.format(locator, locatorType))
        except:
            self.log.error('Cannot click on element with locator: {0} locator type: {1}'.format(locator, locatorType))
            print_stack()

    def elementSendKeys(self, data, locator='', locatorType = 'id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info('Send data to element with locator :: {0} locator type :: {1}'.format(locator, locatorType))
        except:
            self.log.error('Cannot send data to element with locator :: {0} locator type :: {1}'.format(locator, locatorType))
            print_stack()

    def getText(self, element=None, info=''):
        try:
            if element is not None:
                self.log.debug("element was provided")

            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: {0}".format(info))
                self.log.info("The text is :: '{0}'".format(text))
                text = text.strip()
        except:
            self.log.error("Failed to get text on element {0}".format(info))
            print_stack()
            text = None
        return text

    def elementClear(self, locator, locatorType = 'id'):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info('Cleared data from element with locator :: {0} locator type: {1}'.format(locator, locatorType))
        except:
            self.log.error('Cannot clear data from element with locator :: {0} locator type: {1}'.format(locator, locatorType))
            print_stack()

    def elementPresenceCheck(self, locator, locatorType = 'id'):
        try:
            elementList = self.getElementList(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Found " + str(len(elementList)) + " elements")
                return True
            else:
                self.log.info('No elements found with locator :: {0} and locator type :: {1}'.format(locator, locatorType))
                return False
        except:
            self.log.error('Elements not found due to exception!')
            print_stack()
            return False

    def isElementPresent(self, locator='', locatorType = 'id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator :: {0} and locator type :: {1}".format(locator,locatorType))
                return True
            else:
                self.log.info(
                    "Element not present with locator :: {0} and locator type :: {1}".format(locator, locatorType))
                return False
        except:
            self.log.error("Element not found due to exception!")
            print_stack()
            return False

    def isElementDisplayed(self, locator='', locatorType = 'id', element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator :: {0} and locator type :: {1}".format(locator,locatorType))
            else:
                self.log.info(
                    "Element is not displayed with locator :: {0} and locator type :: {1}".format(locator, locatorType))
            return isDisplayed
        except:
            self.log.error("Element not found due to exception!")
            print_stack()
            return False


    def inspectElementProperties(self, locator, locatorType = 'id'):
        try:
            elements = self.getElementList(locator, locatorType)
            if (len(elements) > 0):
                for element in elements:
                    properties = "[ ElementText = {0} | isVisible = {1} | isEnabled = {2} ]"
                    self.log.info(properties.format(element.text, element.is_displayed(), element.is_enabled()))
                return True
            else:
                return False
        except:
            self.log.info("Element not found due to exception!")
            print_stack()
            return False

    def waitForElement(self, locator, locatorType = 'id', timeout=10, pool_frequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info('Waiting for maximum ::  {0} seconds for element to be clickable'.format(timeout))
            wait = WebDriverWait(self.driver, timeout, pool_frequency, ignored_exceptions=
                        [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info('Element appeared on the web page')
        except:
            self.log.info('Element not found due to exception!')
            print_stack()
        return element

    def webScroll(self, direction='up'):
        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0, 1000);")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.options import Options as IeOptions
import os.path as path
import os
from ui import ui_config as uc


class WebDriverFactory():
    def __init__(self):
        self.browser = uc.BROWSER

    def getWebDriverInstance(self):
        baseURL = uc.BASE_URL
        if self.browser == "ie":
            driver_full_path = self.getWebDriverExecutableFullPath("IEDriverServer.exe")
            os.environ["webdriver.ie.driver"] = driver_full_path
            options = IeOptions()
            options.binary_location = uc.LOCAL_IE_PATH
            driver = webdriver.Ie(executable_path=driver_full_path, options=options, service_log_path=self.getWebDriverLoggingFullPath('iedriver.log'))

        elif self.browser == 'firefox':
            driver_full_path = self.getWebDriverExecutableFullPath("geckodriver.exe")
            profile = webdriver.FirefoxProfile()
            profile.set_preference('network.http.phishy-userpass-length', 255)

            driver = webdriver.Firefox(firefox_profile=profile, executable_path=driver_full_path, service_log_path=self.getWebDriverLoggingFullPath('geckodriver.log'))

        elif self.browser == 'chrome':
            driver_full_path = self.getWebDriverExecutableFullPath("chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = driver_full_path
            options = Options()
            options.binary_location = uc.LOCAL_CHROME_PATH
            driver = webdriver.Chrome(executable_path=driver_full_path, options=options, service_log_path=self.getWebDriverLoggingFullPath('chromedriver.log'))
        else:
            driver_full_path = self.getWebDriverExecutableFullPath("geckodriver.exe")
            driver = webdriver.Firefox(executable_path=driver_full_path, service_log_path=self.getWebDriverLoggingFullPath('geckodriver.log'))

        driver.implicitly_wait(uc.IMPLICIT_WAIT)
        driver.maximize_window()
        driver.get(baseURL)
        return driver

    def getWebDriverExecutableFullPath(self, driver_filename):
        driver_folder = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', 'webdrivers'))
        return path.normpath(path.join(driver_folder, driver_filename))

    def getWebDriverLoggingFullPath(self, log_filename):
        log_folder = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', '..', 'log'))

        try:
            os.makedirs(log_folder)
        except FileExistsError:
            pass

        return path.normpath(path.join(log_folder, log_filename))

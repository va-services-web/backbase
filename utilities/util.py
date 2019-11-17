import utilities.custom_logger as cl
import random
import string
import collections


class Util(object):
    log = cl.customLogger()

    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text from application UI --> :: " + actualText)
        self.log.info("Expected text from application UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAIN !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text from API response --> :: {}".format(actualText))
        self.log.info("Expected text from API response --> :: {}".format(expectedText))
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHES !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyNumbersMatch(self, actualNumber, expectedNumber):
        self.log.info("Actual number from API response --> :: {}".format(actualNumber))
        self.log.info("Expected number from API response --> :: {}".format(expectedNumber))
        if actualNumber == expectedNumber:
            self.log.info("### VERIFICATION MATCHES !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyDictionariesMatch(self, actualDict, expectedDict):
        self.log.info("Actual dictionary from API response --> :: {}".format(actualDict))
        self.log.info("Expected dictionary from API response --> :: {}".format(expectedDict))
        if actualDict == expectedDict:
            self.log.info("### VERIFICATION MATCHES !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def dictionaryToListOfStrings(self, dict):
        list_of_strings = []
        for key, value in dict.items():
            list_of_strings.append('{} {}'.format(key, value))
        return list_of_strings

    def verifyListsMatch(self, actual, expected):
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        return compare(actual, expected)

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def randomUsername(self):
        return 'Username{}'.format(self.randomString())

    def randomPassword(self):
        return 'Password{}'.format(self.randomString())

    def randomEmail(self):
        """Generate a random email """
        return "Email{}@{}.{}".format(self.randomString(), self.randomString(), self.randomString())

    def randomEmail_noAt(self):
        return "Email{}.{}".format(self.randomString(), self.randomString())

    def randomEmail_noDot(self):
        return "Email{}@{}".format(self.randomString(), self.randomString())

    def randomEmail_noAt_noDot(self):
        return "Email{}".format(self.randomString())

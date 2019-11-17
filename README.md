# backbase

Test automation framework using Selenium WebDriver, Python3, Requests and PyTest. **To be run only on Windows 10 machine.**

Solution was developed and tested on Windows 10.

The Test Cases & Test Report docs are in docs folder

For API tests the relevant folders are: api/, tests/api/ and utilities/
For UI tests the relevant folders are: ui/, tests/e2e/ and utilities/

## How to run automation

### Install steps for Windows 10

> install Python 3.7 (including pip)

> git clone https://github.com/va-services-web/backbase.git

> cd backbase

> pip install -r requirements.txt** will install all dependencies

### Run tests locally on Windows 10

> open **Command Prompt** navigate to **backbase** folder and run
>
**pytest tests/api/signup/ tests/api/login tests/e2e/ --html=report.html --self-contained-html**

By default UI tests are running on Firefox local browser. To run on local Chrome or InternetExplorer update

BROWSER
LOCAL_IE_PATH
LOCAL_CHROME_PATH

in ui/ui_config.py file.
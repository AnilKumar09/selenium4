

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def lanuch():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("proxy-server=")
        service_obj = Service("/Users/sk/Repos/chromedriver.exe'")
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://google.com")
    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lanuch()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

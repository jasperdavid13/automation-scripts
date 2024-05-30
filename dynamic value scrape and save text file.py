from selenium import webdriver
import time
from datetime import datetime as dt



def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features = AutomationControlled")

    driver = webdriver.Chrome(options = options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """extract only temp from the text"""
    output = str(text.split(": ")[1])
    return output


def write_file(text):
    """write input into text file"""

    filename = f".{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(text)


#    """for 10 times"""
#    """if want indefinetely use while True"""
def main():
    driver = get_driver()

    for i in range(0,10):
        time.sleep(2)
        element = driver.find_element(by= "xpath", value= "/html/body/div[1]/div/h1[2]")
        text = clean_text(element.text)
        write_file(text)


print(main())
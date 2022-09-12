from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"
    browser = webdriver.Chrome()
    browser.get(url)

    for i in range(16):
        xPath = f'//*[@id="main"]/div[1]/table/tbody/tr[{i+1}]/td[4]'
        xPathLand = f'//*[@id="main"]/div[1]/table/tbody/tr[{i+1}]/td[1]'
        num = browser.find_element(By.XPATH, xPath).get_attribute("textContent")
        name = browser.find_element(By.XPATH, xPathLand).get_attribute("textContent")

        print(f"{name} 7 day: {num}")

if __name__ == '__main__':
    main()

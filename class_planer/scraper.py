from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def getData():
    pwFile = open("pw.txt")
    urlFile = open("link.txt")
    pw = pwFile.readlines()[0]
    url = urlFile.readlines()[0]

    return pw, url

def getTableData(browser):
    """
    can't get it to work now the website where i'm
    trying to scrape is down :(

    :return:
    """

    # f = '//*[@id="DATA"]/tbody/tr[12]'
    xPath = '//*[@id="DATA"]/tbody/tr[14]/td[4]'
    # xPathTwo = '//*[@id="DATA"]/tbody/tr[19]/td[4]'

    for i in range(200):
        try:
            xPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/td[3]'
            descriptionPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/td[4]'
            fach = browser.find_element(By.XPATH, xPath).get_attribute("textContent")
            description = browser.find_element(By.XPATH, descriptionPath).get_attribute("textContent")

            print([fach, description])
        except:
            pass

    pass


def main():
    pw, url = getData()
    # print(pw)
    # print(url)

    browser = webdriver.Chrome()
    browser.get(url)
    xPath = '//*[@id="Password"]'
    inputElement = browser.find_element(By.XPATH, xPath)

    for i in pw:
        inputElement.send_keys(i)
    inputElement.send_keys(Keys.ENTER)

    xPath = '//*[@id="MenuL"]/table/tbody/tr[2]/td/a'
    browser.find_element(By.XPATH, xPath).click()

    getTableData(browser)

    close = input("ENTER:")


if __name__ == '__main__':
    main()

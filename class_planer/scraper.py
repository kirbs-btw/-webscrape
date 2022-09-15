from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def getData():
    pwFile = open("pw.txt")
    urlFile = open("link.txt")
    pw = pwFile.readlines()[0]
    url = urlFile.readlines()[0]

    return pw, url

def getTableData():
    """
    can't get it to work now the website where i'm
    trying to scrape is down :(

    :return:
    """
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

    close = input("ENTER:")


if __name__ == '__main__':
    main()

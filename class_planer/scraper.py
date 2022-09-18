from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class data():
    def __init__(self):
        self.data = []
        self.levelSave = ""
        self.classSave = []

    def print(self):
        for i in self.data:
            print(i)

    def saveDataSet(self):
        set = []
        set.append(self.levelSave)
        for i in self.classSave:
            set.append(i)
        self.levelSave = ""
        self.classSave = []
        self.data.append(set)





"""
    [
        [Sk2]
        [SK2, 23, 31],
        [2, 31, 31],
        [31, 21, 2],
    ]
"""

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
            xPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/th'
            schoolClass = browser.find_element(By.XPATH, xPath).get_attribute("textContent")
            if schoolClass != "":
                data.saveDataSet()
                data.levelSave = schoolClass
        except:
            pass

        try:
            xPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/td[3]'
            descriptionPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/td[4]'
            lessonPath = f'//*[@id="DATA"]/tbody/tr[{i + 1}]/td[1]'
            fach = browser.find_element(By.XPATH, xPath).get_attribute("textContent")
            description = browser.find_element(By.XPATH, descriptionPath).get_attribute("textContent")
            lesson = browser.find_element(By.XPATH, lessonPath).get_attribute("textContent")
            # print(description.lower())

            if fach != "" or description != "":
                data.classSave.append([lesson, fach, description])

        except:
            pass

    # 
    data.saveDataSet()

    data.print()

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

    # xPath = '//*[@id="MenuL"]/table/tbody/tr[2]/td/a'
    xPath = '//*[@id="MenuL"]/table/tbody/tr[3]/td/a'
    browser.find_element(By.XPATH, xPath).click()

    getTableData(browser)

    close = input("ENTER:")


if __name__ == '__main__':
    data = data()
    main()

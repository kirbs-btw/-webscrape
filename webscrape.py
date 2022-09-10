from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    url = "https://www.youtube.com/results?search_query=never+gonna+give+you+up"
    browser = webdriver.Chrome()
    browser.get(url)


    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/a').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="thumbnail"]').click()


if __name__ == '__main__':
    main()
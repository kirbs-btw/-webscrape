from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""

def main():
    url = "https://www.youtube.com/results?search_query=never+gonna+give+you+up"
    browser = webdriver.Chrome()
    browser.get(url)

    # accepts cookies
    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/a').click()

    # clicks on video
    browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
"""

def main():
    url = "https://www.wetter.com/deutschland/maxdorf/DE0006786.html"
    browser = webdriver.Chrome()
    browser.get(url)

    # accepts cookies
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="cmp-btn-accept"]').click()

    # prints temp
    temp = browser.find_element(By.XPATH, '//*[@id="content-main"]/div[2]/a[1]/div[2]/span[1]').get_attribute("textContent")
    print(f"Today it's: {temp}")
    # f = input("ENTER TO CLOSE: ")


if __name__ == '__main__':
    main()
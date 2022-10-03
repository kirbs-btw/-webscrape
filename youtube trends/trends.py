from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    vids = []

    url = "https://www.youtube.com/feed/trending"
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button').click()


    for i in range(3):
        xPath = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[{i+1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'
        title = browser.find_element(By.XPATH, xPath).get_attribute("textContent")

        xPath = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[{i+1}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/div/yt-formatted-string/a'
        creator = browser.find_element(By.XPATH, xPath).get_attribute("textContent")

        vids.append([title, creator])


    print(vids)

    f = input(":")

if __name__ == '__main__':
    main()
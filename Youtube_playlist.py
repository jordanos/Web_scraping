from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

import time

# Link of the playlist example[https://www.youtube.com/watch?v=-AzGZ_CHzJk&list=PLzMcBGfZo4-mBungzp4GO4fswxO8wTEFx&index=1]

playlist_link = 'YOUR-LINK'



driver = webdriver.Firefox()

driver.get(playlist_link)
time.sleep(3)
playlist = driver.find_elements_by_xpath('//a[@class="yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer"]')

list = []
Download_list = []
for i in range(len(playlist)):
    video_link = playlist[i].get_attribute('href')
    ss_link = video_link[0:12] + 'ss' + video_link[12:]
    list.append(ss_link)

for j in range(len(list)):
    driver.get(list[j])
    time.sleep(15)
    # x = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_partial_link_text('Download').get_attribute('href'))
    # print(x)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Download'))
        )
        print(j+1)
        print(element.get_attribute('href'))
    except Exception as e:
        print(e)
    #print(driver.find_element_by_partial_link_text('Download').get_attribute('href'))
    # print(WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_partial_link_text('Download')).get_attribute('href'))

# for k in range(len(Download_list)):
#     print(Download_list[k])

driver.close()

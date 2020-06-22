import os.path
from os import path
from selenium.webdriver.common.action_chains import ActionChains

if not(path.exists('googleDrivers.zip')):
    import urllib.request

    print('Downloading Chrome Web Drivers')

    url = 'https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip'
    urllib.request.urlretrieve(url, './googleDrivers.zip')
    print("Done downloading web drivers!")
    import zipfile
    with zipfile.ZipFile('./googleDrivers.zip', 'r') as zip_ref:
        zip_ref.extractall('./')

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
print("Enter your credentials in the new window")
driver.get('https://web.facebook.com/groups/1956981687902499')


from selenium.common.exceptions import NoSuchElementException        
import time
try:
    while('Email' in driver.find_element_by_class_name('loggedout_menubar').text or 'class="fb_logo img sp_PtoC_M4ckZu sx_a6eeb2"' in driver.find_element_by_class_name('loggedout_menubar').text):
        time.sleep(1)
except NoSuchElementException:
    print('Logged in!')


while(True):
    time.sleep(10)
    driver.get('https://web.facebook.com/groups/1956981687902499')
    driver.implicitly_wait(5)
    driver.execute_script("document.body.style.zoom='20%'")
    posts = driver.find_elements_by_css_selector(".du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0")
    commentBoxes = driver.find_elements_by_css_selector("._1mf._1mj")

    posts = posts[:8]
    commentBoxes = commentBoxes[:8]
    driver.implicitly_wait(5)

    if(len(posts)>3):
        for i in range(len(posts)-2):
            if 'Vilniuje' in (posts[i].get_attribute('innerHTML')):
                driver.execute_script("arguments[0].click();", commentBoxes[i])
                actions = ActionChains(driver)
                actions.send_keys('+')
                actions.send_keys(u'\ue007')
                actions.perform()
                # commentBoxes[i].send_keys("Nice")
                # commentBoxes[i].send_keys(u'\ue007')
                print("Commented on a post")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def download_twitter_video(link_from_user):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    twitter_link = "https://tweeload.com/"
    driver.get(twitter_link)

    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located([By.ID, "url"]))
    elem.clear()
    try:
        elem.send_keys(link_from_user)
        elem.send_keys(Keys.ENTER)

        time.sleep(15)

        download_button = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/a")

        download_link = download_button.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return




def download_ig_media(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    ig_link = "https://iqsaved.com/"
    driver.get(ig_link)
    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.NAME, "url"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        time.sleep(15)

        new_download_button = driver.find_element(By.LINK_TEXT, "Download video")

        download_link = new_download_button.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return





def download_linkedin_media(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    linkedin_link = "https://www.expertsphp.com/linkedin-video-downloader/"

    driver.get(linkedin_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.NAME, "url"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        time.sleep(20)

        link_button = driver.find_element(By.XPATH, "//*[@id='showdata']/div[4]/table/tbody/tr/td[1]/a")

        download_link = link_button.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return




def download_tiktok_video(link):
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    tiktok_link = "https://snaptik.app/en2"
    driver.get(tiktok_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.ID, "url"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        time.sleep(15)

        link_button = driver.find_element(By.XPATH, "//*[@id='download']/div/div[2]/a[1]")

        download_link = link_button.get_attribute("href")
        driver.quit()
        
        return download_link
    except:
        driver.quit()
        return





def download_tiktok_audio(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    tiktok_link = "https://ssstik.io/"
    driver.get(tiktok_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.ID, "main_page_text"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        time.sleep(15)

        link_button = driver.find_element(By.XPATH, "//*[@id='dl_btns']/a[4]")

        download_link = link_button.get_attribute("href")
        driver.quit()
        
        return download_link
    except:
        driver.quit()
        return




def download_pinterest_video(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    
    pinterest_link = "https://pinterestdownloader.com/"
    driver.get(pinterest_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.NAME, "url"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        time.sleep(20)

        download_button = driver.find_element(By.XPATH, "//*[@id='video_down']")

        download_link = download_button.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return




def download_facebook_video(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    facebook_link = "https://fdownloader.net/en"
    driver.get(facebook_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.NAME, "q"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)
        
        time.sleep(20)

        download_button = driver.find_element(By.XPATH, "//*[@id='fbdownloader']/div[1]/div[1]/table/tbody/tr[1]/td[3]/a")

        download_link = download_button.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return



def download_youtube_video(link):
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    youtube_link = "https://ssyoutube.online/"
    driver.get(youtube_link)

    elem = WebDriverWait(driver,10).until(EC.presence_of_element_located([By.ID, "videoURL"]))
    elem.clear()
    try:
        elem.send_keys(link)

        elem.send_keys(Keys.ENTER)

        main_tab = driver.current_window_handle

        time.sleep(10)

        driver.switch_to.window(main_tab)

        button = driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/div[4]/table/tbody/tr[4]/td[3]/span/button")

        action = ActionChains(driver)
        action.click(button).perform()

        driver.switch_to.window(main_tab)

        time.sleep(35)

        download_button2 = driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/div[2]/a")

        download_link = download_button2.get_attribute("href")
        driver.quit()

        return download_link
    except:
        driver.quit()
        return
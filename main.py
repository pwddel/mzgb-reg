from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

browser = webdriver.Chrome('chromedriver',desired_capabilities=caps, chrome_options=options)

browser.get('https://bar.mzgb.net')
browser.maximize_window()

FIO = "Вася Пупкин" 
PHONE = "+37529754351"
EMAIL = "test@test.com"
TEAM_NAME = "super team"
COMMENT = "comment"

try:
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "games-section-link")))
    button.click()
finally:
    print("First button pressed")

try:
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "h-10")))
    button.click()
finally:
    print("Second button pressed")

try:
    wait = WebDriverWait(browser, 2)
    fio = wait.until(
        EC.visibility_of_element_located((By.ID, "fio")))
    phone = wait.until(
        EC.visibility_of_element_located((By.ID, "phone")))
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email")))
    fio.send_keys(FIO)
    phone.send_keys(PHONE)
    email.send_keys(EMAIL)
    
finally:
    print(fio)    
    print(phone)
    print(email)

try:
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div/div[2]/div/div[5]/button')))
    button.click()
finally:
    print("Third button pressed")

try:
    wait = WebDriverWait(browser, 10)
    team_name = wait.until(
        EC.visibility_of_element_located((By.ID, "team-name")))
    comment = wait.until(
        EC.visibility_of_element_located((By.ID, "comment")))
    team_name.send_keys(TEAM_NAME)
    comment.send_keys(COMMENT)
    
finally:
    print("Test")    
    print("comment")

try:
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div/div[2]/div/div[7]/button')))
    button.click()
finally:
    print("Fourth button pressed")

try:
    wait = WebDriverWait(browser, 10)
    button = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div/div[2]/div/div[5]/button')))
    button.click()
finally:
    print("Fourth button pressed")


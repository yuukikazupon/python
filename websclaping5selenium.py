from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME='yukikazupon'
PASSWORD='8136abcd'

URL='https://www.instagram.com/accounts/login/?source=auth_switcher'

driver=webdriver.Chrome()
driver.get(URL)

driver.implicitly_wait(5)

username_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label')
username_field.send_keys(USERNAME)

password_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label')
password_field.send_keys(PASSWORD)

# login_button=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
# login_button.click()
password_field.send_keys(Keys.RETURN)

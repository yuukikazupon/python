from selenium import webdriver
# import chromedriver_binary


USERNAME='yukinumari'
PASSWORD='8136abcD'

URL='https://hive-member.net/'

# chrome_path='/Users/yukinumari/Library/Caches/pip/wheels/f6/22/5d/338e8e95b362391fea098baee8ed4bfcec5c6a64c23fd53e55'
# driver=webdriver.Chrome(executable_path=chrome_path)
# driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver=webdriver.Chrome()
driver.get(URL)

driver.implicitly_wait(10)

login_page=driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/nav/ul[2]/li/a')
login_page.click()

driver.implicitly_wait(10)

username_field=driver.find_element_by_xpath('//*[@id="username-14"]')
username_field.send_keys(USERNAME)

password_field=driver.find_element_by_xpath('//*[@id="user_password-14"]')
password_field.send_keys(PASSWORD)

login_button=driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div[1]/div/form/div[2]/div[3]/input')

login_button.click()

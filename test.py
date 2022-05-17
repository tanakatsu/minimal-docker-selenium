from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options, executable_path='/opt/chrome/chromedriver')
# driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')  # when you install chromium and chromium-driver

driver.get('https://qiita.com')
print(driver.current_url)
driver.save_screenshot('test.png')
print('OK')

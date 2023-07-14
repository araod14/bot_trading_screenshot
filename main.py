from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


path = '/home/danel149/chromedriver'
# Replace with the path to your chromedriver executable
driver = webdriver.Chrome(path)

# Replace with the URL of the TradingView website
driver.get('https://www.tradingview.com/')

# Click on buttom menu
buttom = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[3]/div[2]/div[1]/button')))
buttom.click() 

# Click on markets menu
markets = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="overlap-manager-root"]/div[2]/span/div[1]/div/div/div/div/button[3]/span[1]/span/span/span[2]/span[1]')))
markets.click() 

# Click on resume
resume = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="overlap-manager-root"]/div[2]/span/div[1]/div/div/div[3]/div/a/span/span/span/span[2]/span[1]')))
resume.click()

# Click on find menu
findmenu = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[3]/div[2]/div[2]/div/div/button[1]')))
findmenu.click()

# find pair
pair='btc'
findmenupair = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input')))
findmenupair.send_keys(pair)

# Click on the first result
firstresult = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div[3]')))
firstresult.click()

# Wait for the chart 
time.sleep(5)

# Take a screenshot of the chart and save it to a file
driver.save_screenshot('chart.png')

# Close the browser
driver.quit()
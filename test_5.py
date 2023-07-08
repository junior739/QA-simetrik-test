from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

h2_web_element = driver.find_element(By.CSS_SELECTOR, "main.container h2")
print(h2_web_element.text)
p_web_element = driver.find_element(By.CSS_SELECTOR, "main.container p")
print(p_web_element.text)
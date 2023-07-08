from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com.co")

web_element = driver.find_element(By.CSS_SELECTOR, ".o3j99.LLD4me")
result_web_element = web_element.find_element(By.CSS_SELECTOR, "img")
print(result_web_element.get_attribute("src"))

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import requests

browser = "Chrome"
driver = None

if browser != "Chrome":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com.co")

# get all links
all_links = driver.find_elements(By.CSS_SELECTOR, "a")

url_results = []

for link in all_links:
    url = link.get_attribute('href')

    response = requests.head(url)
    if response.status_code != 200:
        result = {
            "url": url,
            "status": response.status_code
        }
        url_results.append(result)

print(url_results)
for result in url_results:
    assert result.get("status") != 200

if browser == "Firefox":
    driver.quit()

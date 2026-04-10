from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument("--headless")
print("Launching Chrome in headless mode...")
driver = webdriver.Chrome(options=options)
driver.get("https://yahoo.com")
print("Page title:", driver.title)
search_button = driver.find_element(By.NAME, "p")
search_button.send_keys("Hello, World!")
hotkeys = [Keys.ENTER]
for hotkey in hotkeys:
    search_button.send_keys(hotkey)
print("Page title:", driver.title)
driver.quit()
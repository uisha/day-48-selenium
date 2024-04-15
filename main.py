from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
upcoming_events_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li time")

events = {}

for n in range(len(upcoming_events_dates)):
    events[n] = {
        "time": upcoming_events_dates[n].text,
        "name": upcoming_events[n].text,
    }

print(events)

# driver.close()
driver.quit()
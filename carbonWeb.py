from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time

# Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'https://www.trec.org.tw/certification?year=2024' # change/ to get 2023, 2022, etc
driver.get(url)

wait = WebDriverWait(driver, 30)

# Wait for the dropdown menu to become visible
select_element = wait.until(EC.visibility_of_element_located((By.NAME, 'certificationTable_length')))
select = Select(select_element)

# Show All option (-1) from the dropdown menu
select.select_by_value('-1')

# Wait for the table to reload with all rows
table = wait.until(EC.visibility_of_element_located((By.ID, 'certificationTable')))

# Scroll down the page multiple times to load all data
scroll_attempts = 5
for _ in range(scroll_attempts):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load

# Get the table after scrolling
table = wait.until(EC.visibility_of_element_located((By.ID, 'certificationTable')))

# Write data to CSV
with open('certificate_2024.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Source', 'Type', 'Year', 'Trans_num', 'Remaining_num', 'Details'])
    
    # Extract data from the table
    rows = table.find_elements(By.XPATH, './/tr')
    for row in rows:
        cells = row.find_elements(By.XPATH, './/td')
        if cells:
            Name = cells[0].text.strip()
            Source = cells[1].text.strip()
            Type = cells[2].text.strip()
            Year = cells[3].text.strip()
            Trans_num = cells[4].text.strip()
            Remaining_num = cells[5].text.strip()
            Details = cells[6].text.strip()
            writer.writerow([Name, Source, Type, Year, Trans_num, Remaining_num, Details])

print('CSV created')

# Quit the driver
driver.quit()
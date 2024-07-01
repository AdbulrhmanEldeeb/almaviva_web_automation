import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Your existing setup code
url = "https://egy.almaviva-visa.it/appointment"
mail = 'abdodebo3@gmail.com'

password = '2$HK6#Fsz@nxRsY'
mail_2='u4uzeinab@gmail.com'
password_2='sS@fY8eQdV6WKJp'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(options=chrome_options)
# driver.delete_all_cookies()
driver.get(url=url)

try:
    # Wait until the email input field is present
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    if email_input:
        # Find other elements after the email input is found
        password_input = driver.find_element(By.ID, "password")
        sign_in = driver.find_element(By.ID, "kc-login")

        # Send keys to input fields and click sign in
        email_input.send_keys(mail)
        password_input.send_keys(password)
        sign_in.click()
        time.sleep(3)

except TimeoutException:
    print("Login form not found, skipping login step.")
time.sleep(3)
# Ensure you're on the target URL
for i in range(3):
    if driver.current_url != url: 
        driver.get(url)    
        time.sleep(3)

try:
    # Wait for the select the center dropdown to be clickable
    select_the_center = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'mat-select-value-1'))
    )
    select_the_center.click()

    # Wait for the Cairo option to be clickable and select it
    choose_cairo = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "mat-option-1"))
    )
    choose_cairo.click()

except TimeoutException:
    print("Center selection or Cairo option not found.")

try:
    select_service_level = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'mat-select-value-5'))
    )
    select_service_level.click()

    service_level = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'mat-option-12'))
    )
    service_level.click()

    select_the_type_and_amount_of_visas_you_need = driver.find_element(By.ID, value='mat-select-value-3')
    select_the_type_and_amount_of_visas_you_need.click()

    visa_type = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'mat-option-9'))
    )
    visa_type.click()

    destination = driver.find_element(By.XPATH, value='//*[@id="cdk-step-content-0-0"]/app-memebers-number/form/div/div[7]/div/input')
    city_destination = 'italy'
    destination.send_keys(city_destination)

    trip_date = driver.find_element(By.ID, value='pickerInput')
    trip_date.click()

    click_next_month = driver.find_element(By.CSS_SELECTOR, value='#mat-datepicker-0 > mat-calendar-header > div > div > button.mat-calendar-next-button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base')
    click_next_month.click()
    click_next_month.click()

    day_chosen = driver.find_element(By.CSS_SELECTOR, value='#mat-datepicker-0 > div > mat-month-view > table > tbody > tr:nth-child(4) > td:nth-child(2) > button')
    day_chosen.click()

    accept_terms_and_conditions = driver.find_element(By.ID, value='mat-mdc-checkbox-1-input')
    accept_terms_and_conditions.click()

    check_availability = driver.find_element(By.CSS_SELECTOR, value='#cdk-step-content-0-0 > app-memebers-number > div.flex.flex-col.lg\:flex-row.lg\:justify-end > div > button')

except TimeoutException:
    print("An element wasn't found or wasn't interactable in time.")
except NoSuchElementException:
    print("An element was not found in the DOM.")

def click_check_availability():
    check_availability.click()
    print(f"check avaliabilty button clicked at {datetime.datetime.now().time()}")

# Function to wait until exactly the target time
def wait_until_time(target_time):
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= target_time:
            
            break
        # Sleep for a very short time to keep the loop tight
        time.sleep(0.001)

# Define the target time for 9:00:00 AM
target_time = datetime.time(8, 0, 0,70000)
wait_until_time(target_time)

# Click the check_availability button
click_check_availability()

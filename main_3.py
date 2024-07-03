import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Your existing setup code
url = "https://egy.almaviva-visa.it/appointment"
email_1 = 'abdodebo3@gmail.com'
password_1 = '2$HK6#Fsz@nxRsY'
email_2 = 'u4uzeinab@gmail.com'
password_2 = 'sS@fY8eQdV6WKJp'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def setup_driver():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver

def login(driver, email, password):
    try:
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        if email_input:
            password_input = driver.find_element(By.ID, "password")
            sign_in = driver.find_element(By.ID, "kc-login")
            email_input.send_keys(email)
            password_input.send_keys(password)
            sign_in.click()
            time.sleep(3)
    except TimeoutException:
        print("Login form not found, skipping login step.")
    except Exception as e:
        print(f"An error occurred during login: {e}")

def select_options(driver):
    try:
        while driver.current_url != url:
            driver.get(url)
            time.sleep(3)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'mat-select-value-1'))
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "mat-option-1"))
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'mat-select-value-5'))
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'mat-option-12'))
        ).click()

        driver.find_element(By.ID, 'mat-select-value-3').click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'mat-option-9'))
        ).click()

        destination = driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-0"]/app-memebers-number/form/div/div[7]/div/input')
        destination.send_keys('italy')

        trip_date = driver.find_element(By.ID, 'pickerInput')
        trip_date.click()

        next_month_button = driver.find_element(By.CSS_SELECTOR, '#mat-datepicker-0 > mat-calendar-header > div > div > button.mat-calendar-next-button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base')
        next_month_button.click()
        next_month_button.click()

        day_chosen = driver.find_element(By.CSS_SELECTOR, '#mat-datepicker-0 > div > mat-month-view > table > tbody > tr:nth-child(4) > td:nth-child(2) > button')
        day_chosen.click()

        driver.find_element(By.ID, 'mat-mdc-checkbox-1-input').click()
        privacy_policy = driver.find_element(By.ID, 'mat-mdc-checkbox-2-input')
        privacy_policy.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"An error occurred during option selection: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def click_check_availability(driver):
    try:
        check_availability.click()
        print(f"Check availability button clicked at {datetime.datetime.now().time()}")
    except NoSuchElementException:
        print("Check availability button not found.")
    except Exception as e:
        print(f"An error occurred while clicking the check availability button: {e}")

def wait_until_time(target_time):
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= target_time:
            break
        time.sleep(0.01)

# تحديد الوقت المستهدف
target_time = datetime.time(8, 0, 0, 300000)

# تهيئة السائقين (المتصفحات) وتسجيل الدخول للحساب 20 مرة
drivers = []
for i in range(15):
    try:
        driver = setup_driver()
        # تحديد بيانات تسجيل الدخول بناءً على الرقم التسلسلي للمتصفح
        if i % 2 == 0:
            login(driver, email_1, password_1)
        else:
            login(driver, email_2, password_2)
        select_options(driver)
        drivers.append(driver)
    except Exception as e:
        print(f"An error occurred while setting up driver {i + 1}: {e}")

# الانتظار حتى الوقت المحدد
check_availability = driver.find_element(By.CSS_SELECTOR, '#cdk-step-content-0-0 > app-memebers-number > div.flex.flex-col.lg\:flex-row.lg\:justify-end > div > button')
wait_until_time(target_time)

# تنفيذ الضغط على زر التحقق من التوافر لكل متصفح
for i, driver in enumerate(drivers): 
    try:
        click_check_availability(driver)
    except Exception as e:
        print(f"An error occurred while clicking check availability on driver {i + 1}: {e}")

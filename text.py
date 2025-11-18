from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
import base64
from pathlib import Path
from selenium.webdriver.chrome.options import Options
import re
import cv2
import matplotlib.pyplot as plt
"""
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service("chromedriver.exe")  # adjust path if needed
driver = webdriver.Chrome(service=service, options=chrome_options)
"""
# Setup Chrome driver
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--disable-infobar")

service = Service("/opt/homebrew/bin/chromedriver")  # adjust path if needed
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open IRCTC login page
driver.get("https://www.irctc.co.in/nget/train-search")

# Wait for page load
time.sleep(5)

# Click on Login button
login_button = driver.find_element(By.XPATH, "//a[contains(text(),'LOGIN')]")
login_button.click()
time.sleep(2)

# Enter username
username = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/input")
username.send_keys("AnshRas221")

# Enter password 
password = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[3]/input")
password.send_keys("ANSH12345")

cap = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[5]/div/app-captcha/div/div/div[2]/span[1]/img")
data_uri  = cap.get_attribute('src')
m = re.match(r"data:(image/[^;]+);base64,(.+)", data_uri)
if not m:
    raise ValueError("Not a valid image data URI")


mime, b64data = m.group(1), m.group(2)
ext = { "image/jpeg": ".jpg","image/jpg": ".jpg","image/png": ".png" }.get(mime.lower(), ".bin")

path = Path("captcha_from_html" + ext)
path.write_bytes(base64.b64decode(b64data))


reader = easyocr.Reader(['en'])

image_path = "captcha_from_html.jpg"

img = cv2.imread(image_path)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()


results = reader.readtext(image_path, detail=0)

if results:
    captcha_text = results[0]         # First detected text
    characters = list(captcha_text)   # Split into chars
    print("Recognized Text:", captcha_text)
    print("Characters List:", characters)
    captcha_ele = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[5]/div/app-captcha/div/div/input")
    # captcha_ele.send_keys(captcha_text)
    for i in characters:
        if i != " ":
            captcha_ele.send_keys(i)
            time.sleep(0.2)

    time.sleep(5)
    submit = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/span/button")
    submit.click()
    time.sleep(3)
else:
    print("No text detected.")
time.sleep(2000)


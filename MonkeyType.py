import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://monkeytype.com/")

# Function to handle the cookie popup
def handle_cookie_popup():
    try:
        # Wait for the cookie popup to appear
        cookie_popup_selector = (By.ID, "cookiePopupWrapper")
        wait.until(EC.visibility_of_element_located(cookie_popup_selector))

        # Wait for the cookie popup to disappear
        wait.until(EC.invisibility_of_element_located(cookie_popup_selector))
    except Exception as e:
        # If any exception, print error and continue, not close
        print("Error handling cookie popup: ", str(e))

# div[mode="words"]  clickable
wait = WebDriverWait(driver, 15)
mode_selector = (By.CSS_SELECTOR, 'div[mode="words"]')
wait.until(EC.element_to_be_clickable(mode_selector))

handle_cookie_popup()

# Click on div[mode="words"]
driver.find_element(*mode_selector).click()

# Typing delay even though I did the calculations at the bottom
def calculate_typing_delay(wpm, word_length=5):
    if wpm == 0:
        return 0
    target_time_per_word = 60 / wpm
    return target_time_per_word / (word_length / 5)

# Define a function to automate typing
def automate_typing(wpm=100):
    typing_enabled = False  # Start with typing disabled
    while True:
        # Check if the user has pressed the "SHIFT" key to toggle typing
        if keyboard.is_pressed("SHIFT"):
            typing_enabled = not typing_enabled
            print("Typing has been", "enabled" if typing_enabled else "disabled")
            while keyboard.is_pressed("SHIFT"):
                pass
        
        if typing_enabled:
            try:
                # Find the active word and get its text
                active_word = driver.find_element(By.CSS_SELECTOR, 'div.word.active')
                word_text = active_word.text

                # Type the entire word at once using ActionChains
                ActionChains(driver).send_keys(word_text).perform()

                # Introduce a delay between typing each word based on the WPM
                time.sleep(calculate_typing_delay(wpm, len(word_text)))

                # Simulate pressing SPACE to move to the next word
                ActionChains(driver).send_keys(Keys.SPACE).perform()
            except NoSuchElementException:
                # If NoSuchElementException occurs, there are no more words to type
                print("All words typed. Stopping typing.")
                typing_enabled = False
            except Exception as e:
                # Exception, just print error and continue
                print("Error while typing: ", str(e))
                continue

typing_wpm = 150

automate_typing(typing_wpm * 1.333327)
# calculations below trying to find out how to get the right wpm
# previous values: 5.5556, 7, 3.4, 1.7, 1.333327
# 25 words (512, 464, 525, 580, 477) = 511.6, 50 words(543, 528, 481, 507, 483) = 508.4
# (508.4 + 511.6)/2 = 510
# 200/255, 1.7*0.78431 = 1.333327 im sticking to this its close enough
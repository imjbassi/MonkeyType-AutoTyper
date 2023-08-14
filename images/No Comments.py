import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
from selenium.common.exceptions import NoSuchElementException, WebDriverException

chrome_driver_path = (
    "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"
)
service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

parser = argparse.ArgumentParser(description="Automate typing on MonkeyType.")
parser.add_argument(
    "--wpm", type=int, default=100, help="Words per minute for typing (default: 100)"
)
args = parser.parse_args()

driver.get("https://monkeytype.com/")


def handle_cookie_popup():
    try:

        cookie_popup_selector = (By.ID, "cookiePopupWrapper")

        wait.until(EC.visibility_of_element_located(cookie_popup_selector))
        wait.until(EC.invisibility_of_element_located(cookie_popup_selector))
    except Exception as e:
        print("Error handling cookie popup:", str(e))


wait = WebDriverWait(driver, 15)

mode_selector = (By.CSS_SELECTOR, 'div[mode="words"]')
wait.until(EC.element_to_be_clickable(mode_selector))

handle_cookie_popup()

driver.find_element(*mode_selector).click()


def calculate_typing_delay(wpm, word_length=5):
    if wpm == 0:
        return 0
    target_time_per_word = 60 / wpm
    return target_time_per_word / (word_length / 5)


def automate_typing(args):
    wpm = args.wpm * 1.333327
    typing_enabled = False
    shift_pressed = False
    while True:
        if keyboard.is_pressed("SHIFT"):
            if not shift_pressed:
                typing_enabled = not typing_enabled
                print("Typing has been", "enabled" if typing_enabled else "disabled")
                shift_pressed = True
        else:
            shift_pressed = False

        if typing_enabled:
            try:

                active_word = driver.find_element(By.CSS_SELECTOR, "div.word.active")
                word_text = active_word.text

                ActionChains(driver).send_keys(word_text).perform()
                time.sleep(calculate_typing_delay(wpm, len(word_text)))

                ActionChains(driver).send_keys(Keys.SPACE).perform()
            except Exception as e:
                print("Error during typing:", str(e))


typing_wpm = 150
automate_typing(args)
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard  # Import the keyboard module

# Replace "[put executable path]" with the actual path to the Chrome WebDriver
chrome_driver_path = "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

class outOfTurnException(Exception):
    pass

class usefulMethods:
    @staticmethod
    def get_element_and_click(by, element):
        w = driver.find_element(by, element)
        w.click()

    @staticmethod
    def send_keys(keys):
        ActionChains(driver).send_keys(keys).perform()

# Navigate to the website
driver.get("https://monkeytype.com/")

# Wait until the element with CSS selector 'div[mode="words"]' becomes clickable
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[mode="words"]'))
)

# Click on the element with CSS selector 'div[mode="words"]' to set typing mode to "words"
usefulMethods.get_element_and_click(By.CSS_SELECTOR, 'div[mode="words"]')

# Set an implicit wait of 1 second for the driver
driver.implicitly_wait(1)

# Function to calculate the typing delay in seconds based on WPM
def calculate_typing_delay(wpm, word_length=5):
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
            # Wait for a brief moment to avoid rapid toggling due to key holding
            while keyboard.is_pressed("SHIFT"):
                pass
        
        if typing_enabled:
            words = driver.find_element(By.ID, "words")

            # Find the active word
            active_word = words.find_element(By.CSS_SELECTOR, 'div[class="word active"]')

            # Find all the letters of the active word by selecting elements with the tag name "letter"
            letters = active_word.find_elements(By.TAG_NAME, "letter")

            l = []

            for letter in letters:
                l.append(letter.text)

            for letter in l:
                # Simulate typing each letter
                usefulMethods.send_keys(letter)
                # Introduce a delay between typing each letter based on the WPM
                time.sleep(calculate_typing_delay(wpm, len(l)))

            # Simulate pressing the SPACE key to move to the next word
            usefulMethods.send_keys(Keys.SPACE)

# User-configurable WPM variable (change this value to set the typing speed)
typing_wpm = 150

# Call the function to start the typing automation with the desired WPM speed
automate_typing(typing_wpm*5.5556)
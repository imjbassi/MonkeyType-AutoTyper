# MonkeyType Auto Typer

Automate your typing practice on MonkeyType!

## Dependencies & Installation (Windows)

| [ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver/01fde32d0ed245141e24151f83b7c2db31d596a4) | [Selenium](https://pypi.org/project/selenium/) |
| ------------------------------------------ | -------------------------------------------- |
| ![ChromeDriver](https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/choco%20install%20chromedriver.png) | ![Selenium](https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/pip%20install%20selenium.png) |

| [Keyboard](https://pypi.org/project/keyboard/) | [Argparse](https://pypi.org/project/argparse/) |
| ------------------------------------------ | -------------------------------------------- |
| ![Keyboard](https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/pip%20install%20keyboard.png) | ![Argparse](https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/pip%20install%20argparse2.png) |



You can also install required dependencies using `pip install -r requirements.txt`, and of course, make sure you have Python (version 3.6 or higher).

## Running

Make sure the Chrome Driver path is set to the right executable.

In the script, it is set to `sh chrome_driver_path = "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"` but you may want to change it depending on where you have installed it.

<del>At the bottom, the WPM is meant to be changed before running the script: typing_wpm = 150</del> This number is not completely accurate but it will get you around the number. Set it to whatever you want.
- Command line arguments have been added to change the WPM directly, however you are free to change it in the script as well.
The script is toggled through the `SHIFT` key.

<img src="https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/Command.png" width="500">


Does not always pass bot detection and remember to **use it at your own risk!**

<img src="https://github.com/imjbassi/MonkeyType-AutoTyper/blob/main/images/MonkeyType.png" width="700">

## Code
<img src="https://github.com/imjbassi/MonkeyType-AutoTyper/blob/main/images/Code.png?raw=true" width="700">


1. **Importing Required Libraries:**
   - Import necessary Python libraries and modules, including `argparse`, `time`, `selenium`, `keyboard`, and exceptions.

2. **Setting Up WebDriver and Command-Line Arguments:**
   - Set up the Chrome WebDriver to control the browser.
   - Parse command-line arguments using `argparse`. Accepts the optional `--wpm` argument with a default value of 100.

3. **Opening the MonkeyType Website:**
   - Navigate to the "https://monkeytype.com/" website.

4. **Handling Cookie Popup:**
   - The `handle_cookie_popup()` function waits for the cookie popup to appear and disappear using `WebDriverWait` and `EC` from `selenium`. Print error message on exception.

5. **Setting Up Mode and Clicking:**
   - Wait for the "div[mode='words']" element to become clickable and click on it to select "words" mode.

6. **Calculating Typing Delay:**
   - The `calculate_typing_delay()` function calculates the delay between typing each word based on target WPM and word length.

7. **Automating Typing:**
   - The `automate_typing()` function controls typing.
   - Check "SHIFT" key press to toggle typing and wait until released.
   - If typing enabled, find active word and type it using `ActionChains`. Wait based on calculated delay and press "SPACE" key.
   - Catch exceptions like `NoSuchElementException` and `WebDriverException`.

8. **Running the Automation:**
   - Set `typing_wpm` (e.g., 150) for desired WPM.
   - Call `automate_typing()` with `args` object as argument to start typing automation.

9. **Comments and Formatting:**
   - Code is well-commented and properly formatted for readability.

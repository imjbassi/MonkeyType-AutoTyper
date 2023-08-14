# MonkeyType-AutoTyper

## Dependencies & Installation (Windows)

[ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver/01fde32d0ed245141e24151f83b7c2db31d596a4)

<img src="https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/choco%20install%20chromedriver.png" width="200">

[Selenium](https://pypi.org/project/selenium/)

<img src="https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/pip%20install%20selenium.png" width="200">

[Keyboard](https://pypi.org/project/keyboard/)

<img src="https://raw.githubusercontent.com/imjbassi/MonkeyType-AutoTyper/main/images/pip%20install%20keyboard.png" width="200">

[Argprase](https://pypi.org/project/argparse/)

<img src="" width="200">

Can also install required dependencies using `pip install -r requirements.txt`

## Running

Make sure the Chrome Driver path is set to the right executable.

In the script, it is set to `sh chrome_driver_path = "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"` but you may want to change it.

At the bottom, the WPM is meant to be changed before running the script: `typing_wpm = 150` This number is not completely accurate but it will get you around the number. Set it to whatever you want.

The script is toggled through the `SHIFT` key.

Does not pass bot detection so use at your own risk.

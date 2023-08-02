# MonkeyType-AutoTyper

## Dependencies & Installation (Windows)

[ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver/01fde32d0ed245141e24151f83b7c2db31d596a4)
`choco install chromedriver`

[Selenium](https://pypi.org/project/selenium/)
`pip install selenium`

[Keyboard](https://pypi.org/project/keyboard/)
`pip install keyboard`

Can also install required dependencies using `pip install -r requirements.txt`

## Running

Make sure the Chrome Driver path is set to the right executable.
In the script, it is set to `sh chrome_driver_path = "C:\\ProgramData\\chocolatey\\lib\\chromedriver\\tools\\chromedriver.exe"` but you may want to change it.
At the bottom, the WPM is meant to be changed before running the script: `typing_wpm = 150`
* This number is not completely accurate but it will get you around the number. Set it to whatever you want.

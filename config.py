from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PATH = "chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("---window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
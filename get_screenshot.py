import string
import time
from datetime import datetime

from selenium.webdriver.common.by import By
from config import driver


def create_screenshot(url: string, fullscreen):
    """
    Paramethers: url String, fullscreen Boolean

    Take a screenshot of the url

    if fullscreen: take a screenshot of the whole page, if not, take 1920x1200
    """
    time_now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    screenshot_name = "screenshot_" + str(time_now)

    driver.get(url)
    time.sleep(2)
    driver.maximize_window()

    if fullscreen:
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height'))                                                                                                           
        driver.find_element(By.TAG_NAME, 'body').screenshot(f'./screenshots/{screenshot_name}.png')
    else:
        driver.get_screenshot_as_file(f"./screenshots/{screenshot_name}.png")

    driver.quit()

    return {"Screenshot": f"{screenshot_name}"}
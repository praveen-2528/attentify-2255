import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the web driver
driver = webdriver.Firefox()  # Make sure geckodriver is installed and its path is configured in your environment variables

# Function to perform random scrolling
def random_scroll():
    # Randomly generate scroll distance
    scroll_distance = random.randint(100, 500)
    # Scroll down with random speed
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

# Function to perform random touch
def random_touch():
    # Get random x, y coordinates within the viewport
    x_coord = random.randint(100, 1000)
    y_coord = random.randint(100, 800)
    # Perform click action at random coordinates
    ActionChains(driver).move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), x_coord, y_coord).click().perform()

# Open the URL
url = "https://attentify-real.godaddysites.com"  # Change this URL to your desired website
driver.get(url)

try:
    # Perform actions for 1000 times or until a keyboard interrupt occurs
    for _ in range(1000):
        start_time = time.time()
        while time.time() - start_time < 10:
            # Perform random scrolling and touching
            random_scroll()
            random_touch()
            # Sleep for random time
            time.sleep(random.uniform(0.5, 2))
        # Refresh the page for the next iteration
        driver.refresh()

except KeyboardInterrupt:
    pass

# Close the browser
driver.quit()

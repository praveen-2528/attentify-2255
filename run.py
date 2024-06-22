import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

# Your Gradio app API endpoint
GRADIO_API_ENDPOINT = 'http://127.0.0.1:8000/gradio'

# Path to the GeckoDriver (if not in PATH, otherwise omit this line)
GECKODRIVER_PATH = '/usr/local/bin/geckodriver'

# Initialize the Firefox WebDriver with options
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(15)  # Adjust the sleep time as needed

def get_latest_message():
    # Get the last message in the conversation
    messages = driver.find_elements(By.CSS_SELECTOR, 'span.selectable-text.invisible-space.copyable-text')
    if messages:
        return messages[-1].text
    return None

def send_message(message):
    # Find the message input box
    message_box = driver.find_element(By.CSS_SELECTOR, 'div._13NKt.copyable-text.selectable-text')
    message_box.send_keys(message + Keys.ENTER)

while True:
    # Get the latest message
    latest_message = get_latest_message()
    if latest_message:
        print(f"Received message: {latest_message}")

        # Send the message to the Gradio app and get the response
        response = requests.post(GRADIO_API_ENDPOINT, json={'query': latest_message})
        gradio_response = response.json().get('response', 'Sorry, I could not process your request.')

        # Send the response back to WhatsApp
        send_message(gradio_response)

    # Wait before checking for new messages
    time.sleep(5)  # Adjust the sleep time as needed

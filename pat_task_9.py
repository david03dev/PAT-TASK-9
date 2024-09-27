"""
Automation using Python Selenium & WebDriver Manager - GOOGLE CHROME Browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class david:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Boot the homepage
    def homepage(self):
        # Maximize the browser window
        self.driver.maximize_window()
        # Boot the URL on the browser
        self.driver.get(self.url)

    # Fetch title and URL, then save the page content to a file
    def fetch_details(self):
        # Wait for the page to load
        time.sleep(3)  # Optional, adjust as needed

        # Fetch the title of the webpage
        title = self.driver.title
        print(f"Title of the webpage: {title}")

        # Fetch the current URL of the webpage
        current_url = self.driver.current_url
        print(f"Current URL of the webpage: {current_url}")

        # Extract the entire contents of the webpage
        page_content = self.driver.page_source

        # Save the content to a text file
        with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
            file.write(page_content)

        print("Webpage content saved to 'Webpage_task_11.txt'.")

    # Shutdown method to close the web-browser after automation
    def shutdown(self):
        self.driver.close()


if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    david = david(url)
    david.homepage()
    david.fetch_details()
    david.shutdown()

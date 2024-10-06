from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need a UI
chrome_service = ChromeService(executable_path='path/to/chromedriver')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)

    # Get the page source and parse with Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Example: Scraping titles of articles (modify according to the target website)
    titles = []
    for title in soup.find_all('h2'):  # Modify the tag based on your needs
        titles.append(title.get_text())

    return render_template('index.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
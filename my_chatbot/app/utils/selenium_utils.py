# C:\Users\Mor\Desktop\curss2\p8\my_bot_project\my_chatbot\app\utils\selenium_utils.py

import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import traceback
from .database_utils import store_results, log_error

def get_open_source_search_history():
    try:
        options = Options()
        options.add_argument('--user-data-dir=./User_Data')  # Adjust to your Firefox user data path
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        # Perform a Google search for programming languages
        driver.get('https://www.google.com')
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys('open source programming languages')
        search_box.submit()
        
        time.sleep(5)  # Wait for the page to load

        # Extract search result titles
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        searches = []
        programming_languages = ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'go', 'swift', 'kotlin', 'typescript']

        for result in results:
            title = result.text.lower()
            for lang in programming_languages:
                if lang in title:
                    searches.append((title, lang))
                    break
            if len(searches) >= 3:
                break
        
        driver.quit()

        # Store results in the database
        for search, category in searches:
            store_results([search], category)

        return searches
    except Exception as e:
        log_error(e, 'get_open_source_search_history')
        return []

def log_error(exception, func_name):
    error_log = {
        'error': str(exception),
        'function': func_name,
        'traceback': traceback.format_exc()
    }
    with open('error_log.json', 'a') as f:
        json.dump(error_log, f)
        f.write('\n')

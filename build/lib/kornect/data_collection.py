from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class landing_page():
    def __init__(self, URL):
        self.url = URL

    def setup(self):
        options = Options()
        options.add_argument('--headless')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print('starting the browser')

    def close(self):
        self.driver.quit()

    def fetch_landing_page(self):
        self.driver.get(self.url)
        print(f'Browsing: {self.url}')

    def get_topic_links(self):
        return [(x.get_attribute('href'), x.text) for x in self.driver.find_elements_by_class_name("subject")]

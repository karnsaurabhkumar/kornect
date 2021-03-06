from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class browser:
    def __init__(self, URL, headless=True, no_image=True) -> object:
        self.url = URL
        self.headless = headless
        self.no_image = no_image

    def setup(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        if self.no_image:
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif not options:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print('starting the browser')

    def close(self):
        self.driver.quit()

    def fetch_landing_page(self):
        self.driver.get(self.url)
        print(f'Browsing: {self.url}')

    def get_topic_links(self):
        return [(x.get_attribute('href'), x.text) for x in self.driver.find_elements_by_class_name("subject")]

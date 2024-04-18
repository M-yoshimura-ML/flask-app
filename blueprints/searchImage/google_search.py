import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSearch:

    def __init__(self, query, language):
        self.query = query
        self.language = language

    def search_images(self, query, language):
        # Google Images検索URLの構築
        url = "https://www.google.com/search?q={}&hl={}&tbm=isch".format(query, language)

        # Seleniumを使用してJavaScriptが実行されたページを取得
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # ヘッドレスモードでブラウザを実行
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

        driver.get(url)
        page_source = driver.page_source
        driver.quit()

        # BeautifulSoupを使用して画像URLを抽出
        soup = BeautifulSoup(page_source, 'html.parser')
        image_tags = soup.find_all('img')
        # image_urls = [img['src'] for img in image_tags]
        img_urls = []

        for img_tag in image_tags:
            url = img_tag.get("src")

            if url is None:
                url = img_tag.get("data-src")

            if url is not None:
                img_urls.append(url)

        return img_urls

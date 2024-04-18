import requests
from bs4 import BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

query = "橋本環奈"
url = "https://www.google.com/search?q={}&hl=ja&tbm=isch".format(query)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# すべての要素が読み込まれるまで待つ。タイムアウトは15秒。
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

driver.get(url)
html = driver.page_source.encode("utf-8")
soup = BeautifulSoup(html, "html.parser")

soup.find_all("img")

img_tags = soup.find_all("img")


img_urls = []

for img_tag in img_tags:
  url = img_tag.get("src")
  if url is None:
    url = img_tag.get("data-src")
  if url is not None:
    img_urls.append(url)
    print(url)


def download_image(url, file_path):
  r = requests.get(url, stream=True)

  if r.status_code == 200:
    with open(file_path, "wb") as f:
      f.write(r.content)


import base64

def save_base64_image(data, file_path):
  """base64の読み込みは4文字ごとに行う。4文字で区切れない部分は「=」で補う"""
  data = data + '=' * (-len(data) % 4)
  img = base64.b64decode(data.encode())
  with open(file_path, "wb") as f:
      f.write(img)


import os
import re

# ご自分の環境に合わせて任意のディレクトリパスを指定してください。
save_dir = "C:/Users/MLCEB-MYOSHIMURA/Downloads/hashimoto_kanna"

os.makedirs(save_dir, exist_ok=True)

base64_string = "data:image/jpeg;base64,"

# png画像も対象にする（動画公開後に追記してます）
png_base64_string = "data:image/png;base64,"


for index, url in enumerate(img_urls):
  """ enumerateを使えばリストのindexを取得できます。このindexをそのままファイル名にします
   formatを使えば文字列内の指定した場所に変数の内容を入れることができます"""
  file_name = "{}.jpg".format(index)
  # print(file_name)
  # print(url)


  """
  os.path.joinを使えば引数に指定した文字列をパスの形に繋げる(joinする）ことができます

  例: os.path.join("A", "B")は「A/B」を出力します
  """
  image_path = os.path.join(save_dir, file_name)

  if len(re.findall(base64_string, url)) > 0 or len(re.findall(png_base64_string, url)) > 0:
    url = url.replace(base64_string, "")
    save_base64_image(data=url, file_path=image_path)
  else:
    download_image(url=url, file_path=image_path)

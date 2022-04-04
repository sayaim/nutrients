# coding: UTF-8

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import json

words = {
    'ビタミンAロッテ': 'va',
    # 'ビタミンDロッテ': 'vd',
    # 'ビタミンEロッテ': 've',
    # 'ビタミンKロッテ': 'vk',
    # 'ビタミンB1ロッテ': 'vb1',
    # 'ビタミンB2ロッテ': 'vb2',
    # 'ナイアシンロッテ': 'niacin',
    # 'ビタミンB6ロッテ': 'vb6',
    # 'ビタミンB12ロッテ': 'vb12',
    # '葉酸ロッテ': 'folic',
    # 'パントテン酸ロッテ': 'panto',
    # 'ビオチンロッテ': 'biotin',
    # 'ビタミンCロッテ': 'vc', 
    # 'カリウムロッテ': 'k',
    # 'カルシウムロッテ': 'ca',
    # 'マグネシウムロッテ': 'mg',
    # 'リンロッテ': 'p',
    # '鉄ロッテ': 'fe',
    # '亜鉛ロッテ': 'zn',
    # '銅ロッテ': 'cu',
    # 'マンガンロッテ': 'mn',
    # 'ヨウ素ロッテ': 'i',
    # 'セレンロッテ': 'se',
    # 'クロムロッテ': 'cr',
    # 'モリブデンロッテ': 'mo',
}

list = []

for word in words: 
    driver = webdriver.Chrome()
    driver.set_window_size(400, 600)
    driver.set_window_position(1000, 0)
    driver.get('https://www.google.com')

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(word)
    search_box.submit()
    time.sleep(2)

    title = driver.find_element(By.CLASS_NAME, 'yuRUbf>a')
    title.click()
    time.sleep(3)

    foods = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]')
    driver.quit()

    for food in foods:
        # 無駄に取得したデータを省く
        if re.search('[0-9]', food.text) == None:
            done_filter = food.text

            dict = {
                'name': done_filter,
                'va': 'false',
                'vd': 'false',
                've': 'false',
                'vk': 'false',
                'vb1': 'false',
                'vb2': 'false',
                'niacin': 'false',
                'vb6': 'false',
                'vb12': 'false',
                'folic': 'false',
                'panto': 'false',
                'biotin': 'false',
                'vc': 'false',
            }
            dict[words[word]] = 'true'

            list.append(dict)
            

# ------テスト------
# words = {1,2}
# list = []
# for word in words: 
#     foods = ['apple', 'lemon1', 'りんご', '123']
#     for food in foods:
#         if re.search('[0-9]', food) == None:
#             done_filter = food
#             dict = {'name': done_filter}
#             list.append(dict)

with open("data.json", "a") as f:
    json.dump(list, f, ensure_ascii=False, indent=4)
    


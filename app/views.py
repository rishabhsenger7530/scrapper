
from django.shortcuts import render, render
# Create your views here.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv
from datetime import datetime
import os


options = Options()
options.headless = True

all_links = ['https://pokeratlas.com/poker-room/the-lodge-poker-club-round-rock/cash-games',
            #  'https://pokeratlas.com/poker-room/shuffle-512-austin/cash-games',
             #  'https://pokeratlas.com/poker-room/52-social-club-round-rock/cash-games',
             #  'https://pokeratlas.com/poker-room/texas-card-house-dallas/cash-games',
             #  'https://pokeratlas.com/poker-room/texas-card-house-austin/cash-games',
             #  'https://pokeratlas.com/poker-room/bullets-card-club-austin/cash-games',
             #  'https://pokeratlas.com/poker-room/georgetown-poker-club/cash-games',
             #  'https://pokeratlas.com/poker-room/red-star-social-austin/cash-games',
             #  'https://pokeratlas.com/poker-room/the-oaks-poker-club-austin/cash-games',
             #  'https://pokeratlas.com/poker-room/101-poker-club-richmond-houston/cash-games',
             #  'https://pokeratlas.com/poker-room/legends-poker-room-houston/cash-games',
             #  'https://pokeratlas.com/poker-room/poker-house-of-dallas/cash-games',
             #  'https://pokeratlas.com/poker-room/prime-social-houston/cash-games',
             #  'https://pokeratlas.com/poker-room/rounders-san-antonio/cash-games',
             #  'https://pokeratlas.com/poker-room/sa-card-house-san-antonio/cash-games',
             #  'https://pokeratlas.com/poker-room/san-antonio-poker-palace/cash-games',
             #  'https://pokeratlas.com/poker-room/shuffle-214-dallas/cash-games',
             #  'https://pokeratlas.com/poker-room/spades-poker-house-webster/cash-games',
             #  'https://pokeratlas.com/poker-room/texas-card-house-spring/cash-games'
             ]


fields = ['Room', 'Poker Games', 'Tables', 'Waiting', '']
td_list = []
data_list = []


def generateprofile_csv(filename):
    with open('static/csv/'+filename, 'w', encoding="utf-8") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(data_list)


def home(request):
    from selenium import webdriver
    import os

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://medium.com")
    print(driver.page_source)
    print("Finished!")
    return render(request, 'index.html')

# def home(request):
#     if request.method == "POST":

#         DRIVER_PATH = './chromedriver'
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-gpu")
#         driver = webdriver.Chrome(options=chrome_options)
#         # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#         username = "amrit0021"
#         password = "Amrit.007"
#         try:
#             driver.get("https://pokeratlas.com/login")
#             driver.implicitly_wait(1)
#         except Exception as e:
#             print(e)

#         driver.find_element_by_id("user_username").send_keys(username)
#         # find password input field and insert password as well
#         driver.find_element_by_id("user_password").send_keys(password)
#         # click login button
#         count = 0
#         try:
#             WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#                 (By.CSS_SELECTOR, "input[name='commit'][value='Sign In']"))).click()
#             WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#                 (By.XPATH, "//button[@class='modal-close']"))).click()
#         except Exception as e:
#             print(e)

#         for link in all_links:
#             driver.get(link)
#             sleep(1)
#             try:
#                 if count == 0:
#                     WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#                         (By.XPATH, "//button[@class='modal-close']"))).click()
#                     sleep(2)
#             except Exception as e:
#                 print(e)

#             url_data = driver.page_source
#             url_soup = BeautifulSoup(url_data, 'html.parser')
#             section_content = url_soup.find(
#                 'section', {'class': "panel live-info-panel live-cash-game-panel dynamic-box"})

#             try:
#                 room_name = url_soup.find(
#                     'span', {'class': "current-name"}).text
#                 table_content = section_content.find(
#                     'table', {'class': 'live-info'})

#                 for tr in table_content.find_all('tr', {'class': 'live-cash-game'}):
#                     td_list = []
#                     for td in tr.find_all('td'):
#                         td_list.append(td.text.strip('\n'))
#                     td_list.insert(0, room_name.strip('\n'))
#                     print(td_list)
#                     data_list.append(td_list)
#             except Exception as e:
#                 print(str(e))
#             count = count+1
#         path = "static/csv/"
#         dir_list = str(len(os.listdir(path))+1)
#         generateprofile_csv(dir_list+".csv")

#     return render(request, 'index.html')



def get_all_files(request):
    path = "static/csv/"
    dir_list = os.listdir(path)
    return render(request, 'all_files.html', {'files': dir_list})

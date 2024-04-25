from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import requests

settingnumber = 140             #設定人數小於這個人數就會通知
courseNumber = '*****'      #設定要查詢的課碼
noticeTimes = 0


def fun():
    wd = webdriver.Edge(service=Service(r"C:\Users\User\OneDrive\桌面\測試用\Selenium\msedgedriver.exe"))
    wd.get('https://querycourse.ntust.edu.tw/querycourse/#/')
    wd.maximize_window()
    wd.implicitly_wait(30)
    element = wd.find_element(By.XPATH, '/html/body/div/div[12]/main/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/input')
    element.send_keys(courseNumber)
    element = wd.find_element(By.XPATH, '/html/body/div/div[11]/main/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[8]/button')
    element.click()
    element = wd.find_element(By.XPATH, '/html/body/div/div[13]/main/div/div/div/div/div[5]/div[1]/table/tbody/tr/td[8]/span[1]').text

    if(element[2]=="("):
        number = eval(element[0] + element[1])
    else:
        number = eval(element[0] + element[1] + element[2])

    if(number < settingnumber):
        print("Y")
        global noticeTimes
        noticeTimes += 1
        string = f'已達成設定要求!({noticeTimes}/5)\n課碼：{courseNumber}'
        url = 'https://notify-api.line.me/api/notify'
        token = '*****'       #請輸入LINE API中的Token
        headers = {
        'Authorization': 'Bearer ' + token
        }
        data = {
        'message': string
        }
        data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法 ref:https://steam.oxxostudio.tw/category/python/spider/line-notify.html
    else:
        print("N")
    wd.close()


while noticeTimes < 5:
    fun()
    time.sleep(120)



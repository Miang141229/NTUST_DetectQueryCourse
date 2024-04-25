# NTUST_DetectQueryCourse

## 警告
### **該程式並不是使用機器人在選課系統直接做加選，也請不要頻繁存取學校系統，後果自負。**
![image](https://github.com/Miang141229/NTUST_DetectQueryCourse/blob/main/image/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-04-24%20232022-1.jpg)
#### 該程式是自行參考網路教學寫出，一定有很多能夠精簡的地方，寫得不好的地方還請見諒，祝各位都能選到想的課。

## 前置作業
1. Python
2. VSCode
3. Selenium
4. Requests
#### Selenium 安裝方法:
```python
pip install selenium
```
#### Requests 安裝方法:
```python
pip install requests
```

## 工作流程圖
![image](https://github.com/Miang141229/NTUST_DetectQueryCourse/blob/main/image/%E6%B5%81%E7%A8%8B%E5%9C%96.png))

## 需要自行調整的參數
```python
settingnumber = 15              #設定人數小於這個人數就會通知
courseNumber = '*****'          #設定要查詢的課碼

wd = webdriver.Edge(service=Service(r"C:\Users\User\OneDrive\桌面\Selenium\msedgedriver.exe"))    #"C:\Users\User\OneDrive\桌面\Selenium\msedgedriver.exe" 請自行更改為電腦Driver的路徑

token = '*****'     #請輸入Line API中的Token
```
#### Driver如何下載
##### 到這邊選擇正確的版本下載
<https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver?form=MA13LH>

#### LINE API Token如何取得
##### 參考下方教學
<https://steam.oxxostudio.tw/category/python/spider/line-notify.html>

## 參考資料
<https://steam.oxxostudio.tw/category/python/spider/line-notify.html>

<https://ithelp.ithome.com.tw/articles/10300961>

<https://ithelp.ithome.com.tw/articles/10323418?sc=rss.iron>

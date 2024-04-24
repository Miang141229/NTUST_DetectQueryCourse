# NTUST_DetectQueryCourse

## 警告
### 本專案並不是使用機器人在選課系統直接做加選，也請不要頻繁存取學校系統，後果自負。
## 前置作業
1. Python
2. VSCode
3. Selenium
4. Request
  #### Selenium 安裝方法:
  ```python
  pip install selenium
  ```
  #### Request 安裝方法:
  ```python
  pip install request
  ```

## 工作流程圖
<img src="https://github.com/Miang141229/NTUST_DetectQueryCourse/blob/main/%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="750" />

## 需要自行調整的參數
```python
settingnumber = 15              #設定人數小於這個人數就會通知
courseNumber = '*****'          #設定要查詢的課碼
wd = webdriver.Edge(service=Service(r"C:\Users\User\OneDrive\桌面\Selenium\msedgedriver.exe"))    #"C:\Users\User\OneDrive\桌面\Selenium\msedgedriver.exe" 請自行更改為電腦Driver的路徑
```
#### Driver如何下載
  ##### 到這邊選擇正確的版本下載
  <https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver?form=MA13LH>

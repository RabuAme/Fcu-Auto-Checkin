import time
import cv2 #pip install opencv-python
import pytesseract #pip install pytesseract
from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
from PIL import Image #pip install pillow
import Myconstants #儲存帳號密碼的檔案

driver = webdriver.Chrome() #開啟瀏覽器,先下載正確版本之chromedrivere(https://chromedriver.chromium.org/downloads)
driver.get('https://signin.fcu.edu.tw/clockin/login.aspx') #開啟學校網站
driver.implicitly_wait(10) #最大等待時間
driver.maximize_window() #最大化畫面
time.sleep(1)

user_input = driver.find_element_by_css_selector('#LoginLdap_UserName') #找到帳號儲存格
user_input.send_keys(Myconstants.NID) #輸入帳號
time.sleep(1)

user_input = driver.find_element_by_css_selector('#LoginLdap_Password') #找到密碼儲存格
user_input.send_keys(Myconstants.Password) #輸入密碼
time.sleep(1)

login_lable = driver.find_element_by_css_selector('#LoginLdap_LoginButton') #找到登入按鈕
login_lable.click() #點擊登入
time.sleep(1)

login_check = driver.find_element_by_css_selector('#ButtonClassClockin') #找到打卡介面按鈕
login_check.click() #點擊進入打卡介面
time.sleep(1)

def GetPNG():
  driver.save_screenshot('screen.png') #取得螢幕截圖
  time.sleep(1)
  try:
    element = driver.find_element_by_css_selector('#form1 > div:nth-child(3) > img:nth-child(13)') #尋找驗證碼
  except:
    print("CaptchaNotFound")
    sreach_windows = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
      driver.switch_to.window(handle)
      driver.quit()
      quit()
  else:
    element.location #驗證碼座標
    #print(element.location) #輸出座標
    element.size #驗證碼尺寸
    #print(element.size) #輸出尺寸
    left = element.location['x']
    right = element.location['x'] + element.size['width']
    top = element.location['y']
    bottom = element.location['y'] + element.size['height']
    left, right, top, bottom
    img = Image.open('screen.png') #開啟螢幕截圖
    img = img.crop((left, top, right, bottom)) #從螢幕截圖裁切驗證碼圖片
    img.save('captcha.png') #儲存驗證碼圖片
  finally:
    time.sleep(1) #取得螢幕截圖

GetPNG()

def ReadCaptcha():
  image = Image.open('captcha.png') #開啟驗證碼圖片
  image.resize((150, 50), Image.ANTIALIAS).save("captcha.png") #縮放驗證碼(大小,銳化),儲存

  img = cv2.imread('captcha.png', 0) #讀取驗證碼圖片
  ret, out1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY) #驗證碼圖片二值化
  name = ['BINARY'] #圖片名稱
  image = [out1] #圖像矩陣暫存名稱

  for i in range(len(image)):
    cv2.imwrite(name[i] + '.png', image[i]) #將圖片矩陣與名稱寫入圖檔
    time.sleep(2)

    image2 = Image.open('BINARY.png') #開啟二值化驗證碼圖片

  pytesseract.pytesseract.tesseract_cmd = (Myconstants.Tesseract) #設定Tesseract路徑
  captcha = pytesseract.image_to_string(image2, config="-c tessedit_char_whitelist=0123456789").replace(" ", "").replace("-", "").replace("$", "") #利用內建pytesseract讀取驗證碼文字
  return captcha #讀取驗證碼

print(ReadCaptcha())

def TypeCaptcha():
  check_input = driver.find_element_by_css_selector('#validateCode') #找到驗證碼儲存格
  check_input.send_keys(ReadCaptcha()) #輸入驗證碼
  time.sleep(3) #輸入驗證碼

TypeCaptcha()

def ClickButton(): #點擊打卡按鈕
  check_button = driver.find_element_by_css_selector('#Button0 ') #找到打卡按鈕
  try:
    check_button.click() #點擊打卡按鈕
  except:
    print("ClickFailed")
  else:
    print("ClickSuccess")
  finally:
    time.sleep(1)

ClickButton()

a = 10

def CheckinResult(): #確認打卡成功與否
  check_input = driver.find_element_by_css_selector('#validateCode') #找到驗證碼儲存格
  check_input.send_keys(Keys.CONTROL+'a') #全選儲存格
  check_input.send_keys(Keys.DELETE) #清空儲存格
  check_input.send_keys(ReadCaptcha()) #輸入新驗證碼
  time.sleep(3)

  check_button = driver.find_element_by_css_selector('#Button0 ') #找到打卡按鈕
  try:
    check_button.click() #點擊打卡
  except:
    print("CheckinSuccess")
    sreach_windows = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
      driver.switch_to.window(handle)
      driver.quit()
      quit()
  else:
    print("CheckinFailed")
  finally:
    time.sleep(1)

while a >5: #(迴圈)
  GetPNG()
  print(ReadCaptcha())
  CheckinResult()

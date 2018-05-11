#To get the screenshot of the page

from selenium import webdriver
# depot = DepotManager.get()
driver = webdriver.PhantomJS()
driver.set_window_size(400, 500) # set the window size that you need 
driver.get('https://targetstudy.com/coaching/19581/chavi-3e-masters')
driver.save_screenshot('email.png')

#To read image file

from pytesseract import image_to_string
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = image_to_string(Image.open("email.png"), lang='eng')
# print (text)

#To find email

match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print (match)
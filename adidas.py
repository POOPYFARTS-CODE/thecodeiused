info = open("info.txt").readlines()
info = list(map(lambda x:x.strip(),info))
first_n = info[1]
last_n = info[2]
addres_line1 = info[3]
addres_line2 = info[4]
city = info[6]
zip = info[5]
phone_no = info[6]
paypal_pass = info[7]

from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def adidas(link):
  global email,first_n,last_n,addres_line1,addres_line2,city,zip,phone,paypal_pass
  print('Try')
  driver = webdriver.Chrome("chromedriver.exe" )
  driver.get(link)
  time.sleep(10)
  element1 = driver.find_element_by_xpath("/html/body/div[20]/div[3]/div[1]/div/div[1]/div[3]/div[12]/div[1]/div/label[1]")
  element1.click()
  time.sleep(10)
  element2 = driver.find_element_by_xpath("/html/body/div[20]/div[3]/div[1]/div/div[1]/div[3]/div[19]/button")
  element2.click()
  time.sleep(15)
  element3 = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[1]/div[2]/div[2]/div[2]/a/button")
  element3.click()



  #            *     ,MMM8&&&.            *
  #                 MMMM88&&&&&    .
  #                MMMM88&&&&&&&
  #    *           MMM88&&&&&&&&
  #                MMM88&&&&&&&&
  #                'MMM88&&&&&&'
  #                  'MMM8&&&'      *
  #         |\___/|
  #         )     (             .              '
  #        =\     /=
  #          )===(       *
  #         /     \
  #         |     |
  #        /       \
  #        \       /
  # _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  # |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  # |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  # |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

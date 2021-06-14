from datetime import datetime
from selenium import webdriver
import time
import _thread as thread


x = datetime.today()
year = x.year
month = x.month
day = x.day


URL = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"


### Step1: Download ChromeDriver and copy path to chromedriver.exe here ###
chrome_driver_path = "C:\Python Dev\Selenium\chromedriver.exe" #example: "C:\Python Dev\Selenium\chromedriver.exe"


#uid_submit_xpath =  '//*[@id="ui_body_container"]/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]'
uid_submit_xpath = '//*[@id="top"]/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]';

#pw_submit_xpath = '//*[@id="ui_body_container"]/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]'
pw_submit_xpath = '//*[@id="top"]/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]';


#final_submit_xpath = '//*[@id="ui_body_container"]/input[1]'
final_submit_xpath = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[11]/td/form/input[1]'
#### Step2: Enter USERNAME here ####
#user_name = "Csow001"
user_name = "jyap033"


#### Final Step: Enter PASSWORD here# ####


#password = "2020PlsBeGood!!"
password = "Blackie@9999999"

def main(hr,min,sec,mili):

   z = datetime(year, month, day, hr, min, sec, mili)

   driver = webdriver.Chrome(executable_path=chrome_driver_path)
   driver.get(URL)

   user_name_field = driver.find_element_by_id('UID')
   user_name_field.send_keys(user_name)

   button1 = driver.find_element_by_xpath(uid_submit_xpath)
   button1.click()
   time.sleep(1.5)

   password_field = driver.find_element_by_id('PW')
   password_field.send_keys(password)

   button2 = driver.find_element_by_xpath(pw_submit_xpath)
   button2.click()
   time.sleep(0.5)



   while 1:
       x = datetime.today()
       if x > z:
           # task to be executed when it's time
           print(x)
           button3 = driver.find_element_by_css_selector('tr td form input')
           button3.click()
           #####
           break

   button4 = driver.find_element_by_xpath(final_submit_xpath)
   button4.click()



try:
   #test2
   # thread.start_new_thread( main,(12,39,59,600000))
   # thread.start_new_thread( main,(12,39,59,700000))
   # thread.start_new_thread( main,(12,39,59,800000))
   # thread.start_new_thread( main,(12,39,59,825000))
   # thread.start_new_thread( main,(12,39,59,850000))

   thread.start_new_thread(main, (13, 29, 59, 850000))
   # thread.start_new_thread(main, (13, 29, 59, 870000))
   # thread.start_new_thread(main, (13, 29, 59, 900000))
   # thread.start_new_thread(main, (13, 30, 0, 0))
   # thread.start_new_thread(main, (13, 30, 0, 100000))


   # thread.start_new_thread( main,(13,22,59,900000))
   ##not sure it is too late or inaccurate





except:
   print ("Error: unable to start thread")

while 1:
   pass







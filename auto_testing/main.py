#SiliconValley
#CryptoBro
#Hacker

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
driver = webdriver.Firefox(service=service)
driver.get('https://www.tradingview.com/')

#  ___                   _       
# |_ _|_ __  _ __  _   _| |_ ___ 
#  | || '_ \| '_ \| | | | __/ __|
#  | || | | | |_) | |_| | |_\__ \
# |___|_| |_| .__/ \__,_|\__|___/
#           |_|                  

print('input settings:')
print('v0:')
XPATH0 = " "
v0min = input("v0min: ")
v0max = input('v0max: ')
i = input('v0 increment: ')

print('v1:')
XPATH1 = " "
v1min = input("v1min: ")
v1max = input('v1max: ')
i1 = input('v2 increment: ')

print('v2:')
XPATH2 = " "
v2min = input("v2min: ")
v2max = input('v2max: ')
i2 = input('v2 increment: ')

print('v3:')
XPATH3 = " "
v3min = input("v3min: ")
v3max = input('v3max: ')
i3 = input('v3 increment: ')

print('v4:')
XPATH4 = " "
v4min = input("v4min: ")
v4max = input('v4max: ')
i4 = input('v4 increment: ')

print('v5:')
XPATH5 = " "
v5min = input("v5min: ")
v5max = input('v5max: ')
i5 = input('v5 increment: ')

print('v6:')
XPATH6 = " "
v6min = input("v6min: ")
v6max = input('v6max: ')
i6 = input('v6 increment: ')

print('v7:')
XPATH7 = " "
v7min = input("v7min: ")
v7max = input('v7max: ')
i7 = input('v7 increment:')

print('v8:')
XPATH8 = " "
v8min = input("v8min: ")
v8max = input('v8max: ')
i8 = input('v8 increment: ')

print('v9:')
XPATH9 = " "
v9min = input("v9min: ")
v9max = input('v9max: ')
i9 = input('v9 increment: ')



PFmin = input('Minimum profit factor: ')
SRmin = input('Minimum Sharpe ratio: ')
Wmin = input('Minimum win percentage: ')

#*you need to manualy navigate to the chart*

#   ____ _                _              _               
#  / ___| |__   __ _ _ __| |_   ___  ___| |_ _   _ _ __  
# | |   | '_ \ / _` | '__| __| / __|/ _ \ __| | | | '_ \ 
# | |___| | | | (_| | |  | |_  \__ \  __/ |_| |_| | |_) |
#  \____|_| |_|\__,_|_|   \__| |___/\___|\__|\__,_| .__/ 
#                                                 |_|    

#wait for you to navigate to the chart
WebDriverWait(driver, 250).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/canvas[2]"))
)

print("reached chart")

#select indicator template
bot = driver.find_element(By.CSS_SELECTOR, "#header-toolbar-study-templates > button:nth-child(1) > div:nth-child(1)")
bot.click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.wrap-JeQoCpvi:nth-child(4) > div:nth-child(1)"))
)

bot = driver.find_element(By.CSS_SELECTOR, "div.wrap-JeQoCpvi:nth-child(4) > div:nth-child(1)")
bot.click()

print("selected indicator template")

#open performance summary
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="Performance Summary"]'))
)

bot = driver.find_element(By.XPATH, '//*[@id="Performance Summary"]')
bot.click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,  "tr.ka-tr:nth-child(9) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1)"))
)
#open settings menu
bot = driver.find_element(By.CSS_SELECTOR, 'button.light-button-bYDQcOkp:nth-child(1)')

print('setup done')

#  ____        __ _       _               _____         _   _             
# |  _ \  ___ / _(_)_ __ (_)_ __   __ _  |_   _|__  ___| |_(_)_ __   __ _ 
# | | | |/ _ \ |_| | '_ \| | '_ \ / _` |   | |/ _ \/ __| __| | '_ \ / _` |
# | |_| |  __/  _| | | | | | | | | (_| |   | |  __/\__ \ |_| | | | | (_| |
# |____/ \___|_| |_|_| |_|_|_| |_|\__, |   |_|\___||___/\__|_|_| |_|\__, |
# |  ___|   _ _ __   ___| |_(_) __|___/__  ___                      |___/ 
# | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|                           
# |  _|| |_| | | | | (__| |_| | (_) | | | \__ \                           
# |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/                           


#cycle through setings
def cycle_setings(vxmin, vxmax, XPATH0, vxmin1, vxmax1, XPATH1, vxmin2, vxmax2, XPATH2, vxmin3, vxmax3, XPATH3, vxmin4, vxmax4, XPATH4, vxmin5, vxmax5, XPATH5, vxmin6, vxmax6, XPATH6, vxmin7, vxmax7, XPATH7, vxmin8, vxmax8, XPATH8, vxmin9, vxmax9, XPATH9):
  
  #open setings tab
  bot = driver.find_element(By.CSS_SELECTOR, 'button.light-button-bYDQcOkp:nth-child(1)')
  bot.click()
  
  WebDriverWait(driver, 60).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="inputs"]'))
  )

  s = vxmin
  while s <= vxmax:
    set = driver.find_element(By.XPATH, XPATH0)
    set.clear()
    set.send_keys(str(s))
    s+=i
    s1 = vxmin1
    
    while s1 <= vxmax1:
      set1 = driver.find_element(By.XPATH, XPATH1)
      set1.clear()
      set1.send_keys(str(s1))
      s1+=i1
      s2 = vxmin2

      while s2 <= vxmax2:
        set2 = driver.find_element(By.XPATH, XPATH2)
        set2.clear()
        set2.send_keys(str(s2))
        s2+=i2
        s3 = vxmin3

        while s3 <= vxmax3:
          set3 = driver.find_element(By.XPATH, XPATH3)
          set3.clear()
          set3.send_keys(str(s3))
          s3+=i3
          s4 = vxmin4

          while s4 <= vxmax4:
            set4 = driver.find_element(By.XPATH, XPATH4)
            set4.clear()
            set4.send_keys(str(s4))
            s4+=i4
            s5 = vxmin5

            while s5 <= vxmax5:
              set5 = driver.find_element(By.XPATH, XPATH5)
              set5.clear()
              set5.send_keys(str(s5))
              s5+=i5
              s6 = vxmin6

              while s6 <= vxmax6:
                set6 = driver.find_element(By.XPATH, XPATH6)
                set6.clear()
                set6.send_keys(str(s6))
                s6+=i6
                s7 = vxmin7

                while s7 <= vxmax7:
                  set7 = driver.find_element(By.XPATH, XPATH7)
                  set7.clear()
                  set7.send_keys(str(s7))
                  s7+=i7
                  s8 = vxmin8

                  while s8 <= vxmax8:
                    set8 = driver.find_element(By.XPATH, XPATH8)
                    set8.clear()
                    set8.send_keys(str(s8))
                    s8+=i8
                    s9 = vxmin9

                    while s9 <= vxmax9:
                      set9 = driver.find_element(By.XPATH, XPATH9)
                      set9.clear()
                      set9.send_keys(str(s9))
                      s9+=i9
                      #  ____                _                   _                       
                      # |  _ \ ___  __ _  __| |   __ _ _ __   __| |  ___  __ ___   _____ 
                      # | |_) / _ \/ _` |/ _` |  / _` | '_ \ / _` | / __|/ _` \ \ / / _ \
                      # |  _ <  __/ (_| | (_| | | (_| | | | | (_| | \__ \ (_| |\ V /  __/
                      # |_| \_\___|\__,_|\__,_|  \__,_|_| |_|\__,_| |___/\__,_| \_/ \___|
                      #  _            _   _                                   _ _        
                      # | |_ ___  ___| |_(_)_ __   __ _   _ __ ___  ___ _   _| | |_ ___  
                      # | __/ _ \/ __| __| | '_ \ / _` | | '__/ _ \/ __| | | | | __/ __| 
                      # | ||  __/\__ \ |_| | | | | (_| | | | |  __/\__ \ |_| | | |_\__ \ 
                      #  \__\___||___/\__|_|_| |_|\__, | |_|  \___||___/\__,_|_|\__|___/ 
                      #                           |___/                                  

                      time.sleep(3)

                      WebDriverWait(driver, 60).until(
                      EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[7]/td[2]/div/div'))
                      )
                      WebDriverWait(driver, 60).until(
                      EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[9]/td[2]/div/div'))
                      )
                      WebDriverWait(driver, 60).until(
                      EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[17]/td[2]/div/div'))
                      )
                      SR = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[7]/td[2]/div/div').text
                      PF = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[9]/td[2]/div/div').text
                      W = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div[2]/div[4]/div/div[2]/div/div/div/table/tbody/tr[17]/td[2]/div/div').text

                      if W == 'N/A':
                        W = 0.0
                      else:
                        W = float(W.replace('%', ""))
                      if SR == 'N/A':
                        SR = 0.0
                      else:
                        SR = float(SR.replace('−','-'))
                      if PF == 'N/A':
                        PF = 0.0
                      else:
                        PF = float(PF.replace('−','-'))

                      if W > Wmin and SR > SRmin and PF > PFmin:
                        file.write(str(s-i)+" "+str(s1-i1)+" "+str(s2-i2)+" "+str(s3-i3)+" "+str(s4-i4)+" "+str(s5-i5)+" "+str(s6-i6)+" "+str(s7-i7)+" "+str(s8-i8)+" "+str(s9-i9)), file.write(' PF= '+str(PF)+' W%= '+str(W)+' SR= '+str(SR)+'\n')
#that's a long ass function.      


#  _____         _   _             
# |_   _|__  ___| |_(_)_ __   __ _ 
#   | |/ _ \/ __| __| | '_ \ / _` |
#   | |  __/\__ \ |_| | | | | (_| |
#   |_|\___||___/\__|_|_| |_|\__, |
#                            |___/ 

file = open('auto_testing/output.txt', 'w')

rerun = 'yes'

while rerun == 'yes':
  input('manualy select timeframe on chart and press enter')
  symbol = input('symbol and timeframe: ')
  file.write(symbol+'\n')

  input('press enter to start testing')
  print('Starting testing...')

  cycle_setings(v0min, v0max, XPATH0, v1min, v1max, XPATH1, v2min, v2max, XPATH2, v3min, v3max, XPATH3, v4min, v4max, XPATH4, v5min, v5max, XPATH5, v6min, v6max, XPATH6, v7min, v7max, XPATH7, v8min, v8max, XPATH8, v9min, v9max, XPATH9)
  rerun = input('do you want to test another symbol or timeframe? ')

print('W code')
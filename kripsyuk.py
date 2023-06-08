from email import message_from_binary_file
from turtle import fd
import requests
import json
import webbrowser
from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import faker
from faker import Faker
import requests
from time import sleep
import os
from random import randint
from selenium.webdriver.support.ui import Select
import os
from discord.ext import commands
import undetected_chromedriver.v2 as uc
import discord
from dotenv import load_dotenv
import random
from twocaptcha import TwoCaptcha
from captchsolve import Capsolve



faker = Faker()



# Import datetime and timedelta 
# class from datetime module 
from datetime import datetime, timedelta 
from webdriver_manager.core.utils import ChromeType

  



#fnamepanera = input("What is your first name?\n  ")
#lnamepanera = input("What is your last name?\n  ")
#phonepanera = input("What is your phone number (no dashes)?\n  ")
#emailpanera = input("What is your email?\n  ")
#passpanera = input("What is your password?  \n  ")




import datetime



def kripuk():
    
    options = uc.ChromeOptions()
    #Get today's date and store it in presentday
    
# Get Tomorrow
# use datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# add day 1 to presentday to get tomorrows date
    days = 1
#So, this is tomorrows date
    

   
    
    finalyear = '2000'
    phonerandom = randint(1000,9999)
    phonerandom2 = randint(10000,99999)

    current_date = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    tomorrow_date = current_date + one_day
    formatted_date = tomorrow_date.strftime("%d/%m")

    fname = faker.first_name()
    lname = faker.last_name()
  

    zipcode = "34224"
    phone1 = str(phonerandom)
    phone2 = str(phonerandom2)
    phone3 = "15389"
    finalphone = phone1+phone2+phone3
    added = faker.year()
    email = fname +lname+ "@staycooking.xyz"
    password = "Focusbetapass911"
    kids = "No"
    location = 'Iowa'
    location_store = 'Hooters of Council Bluffs'
    #options.add_argument('--headless')
   
    

    web = uc.Chrome(options=options)

    web.get('https://www.krispykreme.co.uk/customer/account/create/')
    sleep(4)
    clickcookie= web.find_element(By.ID,'onetrust-accept-btn-handler').click()
    sleep(2)
    fnameinp = web.find_element(By.ID, "firstname")
   
    fnameinp.send_keys(fname)

    lnameinp = web.find_element(By.ID, 'lastname')
   
    lnameinp.send_keys(lname)

    emailinp = web.find_element(By.ID, 'email_address')
    
    emailinp.send_keys(email)

    passwordinp = web.find_element(By.ID, 'password')
    
    passwordinp.send_keys(password)
    sleep(3)

    passwordinp = web.find_element(By.XPATH, '/html/body/div[3]/main/div[3]/div/form/fieldset[2]/div[3]/div/input')
    sleep(1)
    passwordinp.send_keys(password)
    sleep(2)

    privclick= web.find_element(By.ID,'scommerce_gdpr_privacy_consent').click()
    sleep(1)
    privclick2= web.find_element(By.ID,'enrol_in_loyalty').click()
    sleep(1)

    mdateinp = web.find_element(By.ID, 'dob')
    
    mdateinp.send_keys(formatted_date+'/1999')
    sleep(2)
    selectdate = web.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div/form/fieldset[3]/div[2]/div[4]/input').click()
    sleep(2)

    phone1inp = web.find_element(By.XPATH, '/html/body/div[3]/main/div[3]/div/form/fieldset[3]/div[2]/div[3]/input')
    
    phone1inp.send_keys('44'+phone1+phone2)
    sleep(2)

    gender = Select(web.find_element(By.ID,'gender'))
    gender.select_by_value('1')
    sleep(1.2)



    zipcodeinp = web.find_element(By.ID, 'postcode')
    zipcodeinp.send_keys('N19')
    sleep(1)
    buttonlast = web.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div/form/fieldset[3]/div[2]/fieldset/div[1]/input').click()
    sleep(1)
    buttonlast = web.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div/form/fieldset[3]/div[2]/fieldset/div[2]/input').click()
    sleep(1)
    buttonlast = web.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div/form/fieldset[3]/div[2]/div[6]/input').click()

    
    sleep(2)

    buttonlast = web.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div/form/div/div[1]/button').click()
    sleep(5)
    sleep(1)

    with open('kripsyuk.txt','a') as f:
        f.write(email+':'+password+'\n')
    sleep(6)
    web.close()
   

    

if __name__ == '__main__':
    sets = int(input('How many to gen mf?: '))
    for i in range(sets):
        kripuk()
        

    
import os
from time import sleep
import sys   
import undetected_chromedriver.v2 as uc              
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from colorama import Fore
import random
import string
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from dhooks import Webhook
import requests
import socket

load_dotenv()
options = uc.ChromeOptions()
webdriver = uc.Chrome(options = options)
wait = WebDriverWait(webdriver, 60)


WEBSITE_URL = os.getenv("WEBSITE_URL")
COUNTRY = os.getenv("COUNTRY")
LINK = os.getenv("LINK")


def random_string(length, character_set):
    return ''.join(random.choice(character_set) for i in range(length))

email =  "NyoxyGen" + random_string(5, string.ascii_lowercase) + '@outlook.com'
password = "NyoxyGen" + random_string(10, string.ascii_uppercase)

print("Browser is initialized!")

webdriver.get(WEBSITE_URL)


print("Making The Account")



get_ip = lambda : socket.gethostbyname(socket.gethostname())

# I added this ip printer to see if my proxies do work u can just remove the "#" if you want to see and test your proxies
#print('CURRENT IP : ' + get_ip())

print('[!] Set Email.')
wait.until(EC.visibility_of_element_located((By.ID, 'MemberName'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()


print('[!] Set Password.')
wait.until(EC.visibility_of_element_located((By.ID, 'PasswordInput'))).send_keys(password)



print(email + ":" + password)
wait.until(EC.visibility_of_element_located((By.ID, 'iOptinEmail'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()

print('[!] Setting up names.')

wait.until(EC.visibility_of_element_located((By.ID, 'FirstName'))).send_keys('a')
wait.until(EC.visibility_of_element_located((By.ID, 'LastName'))).send_keys('a')
wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()

print('[!] Selecting Country.')

wait.until(EC.visibility_of_element_located((By.ID, 'Country'))).send_keys(COUNTRY)
Select(webdriver.find_element(By.ID, 'BirthMonth')).select_by_value(str(random.randint(1, 12)))
Select(webdriver.find_element(By.ID, 'BirthDay')).select_by_value(str(random.randint(1, 28)))
wait.until(EC.visibility_of_element_located((By.ID, 'BirthYear'))).send_keys('1988')
wait.until(EC.visibility_of_element_located((By.ID, 'iSignupAction'))).click()

print('[!] Finish the Captcha')
    

WebDriverWait(webdriver, 20000).until(EC.visibility_of_element_located((By.ID, 'idSIButton9')))
wait.until(EC.visibility_of_element_located((By.ID, 'idSIButton9'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'KmsiCheckboxField'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'idBtn_Back'))).click()
print('[!] Finished signup, redirecting to buy page.')
print('[!] Done Making an Account')
print('[!] Done Making an Account')
        
    #Webhook if you want!

try:
    requests.post("webhook link", json= {"content": f"@everyone ** new account generated ** \n\n {email   +  password}"})
except:
    pass


sleep(500)

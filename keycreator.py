from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from colorama import Fore
from time import sleep
import string
import random
import sys
import os


d = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
d.get('https://account.shodan.io/register')


mails = 'freeallapp.com', 'microcenter.io', 'zamananow.com'


def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))


user = username()
password = 'Mostazos17'


def generatingEmail():
    return ''.join(user + '@' + random.choice(mails))


fmail = generatingEmail()
d.find_element_by_name('username').send_keys(user)
d.find_element_by_name('password').send_keys(password)
d.find_element_by_name('password_confirm').send_keys(password)
d.find_element_by_name('email').send_keys(fmail, Keys.ENTER)

d.execute_script('window.open('');')
d.switch_to.window(d.window_handles[1])
link = 'https://email-fake.com/' + fmail
d.get(link)
t = d.title
print('\n''\n''\t' + Fore.RESET)
while True:
    if t[:4] == "Fake":
        d.refresh()
        t = d.title
        print(t)
        sleep(1)
    else:
        break
sleep(2)
d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
d.find_element_by_xpath('//*[@id="email-table"]/div[2]/div[4]/div[3]/div/div/a').click()

d.switch_to.window(d.window_handles[2])
sleep(1)

d.find_element_by_name('username').send_keys(user)
d.find_element_by_name('password').send_keys(password, Keys.ENTER)
sleep(2)

d.find_element_by_partial_link_text('Account').click()
sleep(1)
file = open('key.txt', 'r+')
#os.system('stty echo')
_api_key_g = input('\t''Enter the api key (copy the key): ')
file.write(_api_key_g)
#os.system('stty echo')
print('\t' + Fore.WHITE + 'Api key saved.')
print('\n''\t' + Fore.WHITE + 'Goodbye...')
sleep(1.5)
os.system('cls')
sys.exit(1)

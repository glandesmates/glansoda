import argparse as arg
from time import sleep
import requests
import ftplib

import os
import sys
import random

from shodan import Shodan
from colorama import init, Fore, Style

init(autoreset=True)


class Advertisement:
    warning = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTYELLOW_EX + '> '
    message = Fore.LIGHTBLACK_EX + '+' + Fore.LIGHTYELLOW_EX + '> '
    information = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + 'data' + Fore.LIGHTYELLOW_EX + '> '
    end = Fore.LIGHTYELLOW_EX + '/' + Fore.LIGHTBLACK_EX + '>' + '/ '
    suggest = Fore.BLUE + '*' + Fore.LIGHTBLUE_EX + '> '
    step = Fore.LIGHTBLUE_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTBLUE_EX + '> '


def osleping():
    try:
        os.system('cls')
    except:
        os.system('clear')

banner = '\n'"""
  ▄▀  █    ██      ▄          ▄▄▄▄▄   ████▄ ██▄   ██   
▄▀    █    █ █      █        █     ▀▄ █   █ █  █  █ █  
█ ▀▄  █    █▄▄█ ██   █     ▄  ▀▀▀▀▄   █   █ █   █ █▄▄█ 
█   █ ███▄ █  █ █ █  █      ▀▄▄▄▄▀    ▀████ █  █  █  █ 
 ███      ▀   █ █  █ █                      ███▀     █ 
             █  █   ██                              █  
            ▀                                      ▀ 
"""
print('\n\n')

colors = Fore.RED, Fore.WHITE

def cute(var, col):

    def caca():
        sys.stdout.flush()
        sleep(0)

    for char in var:
        if col == 'mocos':
            print(random.choice(colors) + char, end='')
            caca()
        elif col == 'verdes':
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + char, end='')
            caca()
        elif col == 'rojos':
            print(Style.BRIGHT + Fore.LIGHTRED_EX + char, end='')
            caca()

cute(banner, 'mocos')


me = ('\t\t      By Mynor Estrada', """
                 - Youtube: GlandesMates
                 - Github: GlandesMates""")

cute(me[0], 'verdes')
cute(me[1], 'rojos')
print('\n\n')

parser = arg.ArgumentParser()

positional = parser.add_argument_group('POSITIONAL')
positional.add_argument('lim', type=int)
positional.add_argument('search', type=str)

parser.add_argument('--ftp', type=bool)
parser.add_argument('--requests', type=bool)
parser.add_argument('--data', type=bool)
parser.add_argument('--save', type=str)

args = parser.parse_args()

global key

try:
    with open('key.txt', 'r+') as f:
        key = f.readline().rstrip('\n')
except:
    with open('key.txt', 'w') as f:
        key = input('\tEnter your api key: ')
        f.write(key)
        f.close

if args.save:
    if os.path.exists(args.save):
        pass
    else:
        open(args.save, 'w')

api = Shodan(key)
query = args.search

global count
count = 0

for result in api.search_cursor(query):
    try:
        print(Fore.CYAN + f'Result {count + 1} for your search {query}\n')
        if args.requests == True:
            r = requests.get(f"https://{result['ip_str']}:{result['port']}", timeout=1.8)
            if r.status_code != 200 or r.status_code != 302:
                pass
            else:
                print(Fore.GREEN + f"https://{result['ip_str']}:{result['port']} is avaliable")
        else:
            print(Fore.GREEN + f"\tLink: {result['ip_str']}:{result['port']}\n")
        
        print(f"\tIP: {result['ip_str']}")
        print(f"\tPort: {result['port']}")
        print(f"\tOrg: {result['org']}")
        print(f"\tHostnames: {result['hostnames']}")
        print(f"\tDomains: {result['domains']}")
        print(f"\tOS: {result['os']}")

        if args.ftp == True:
            with ftplib.FTP(result['ip_str'], timeout=3.6) as ftp:
                try:
                    print()
                    ftp.login('anonymous', 'anonymous@')
                    ftp.dir()
                    try:
                        ftp.cwd('shares')
                        ftp.dir()
                    except:
                        try:
                            ftp.cwd('USB_Storage')
                            ftp.dir()
                        except:
                            pass
                    ftp.close()
                except:
                    print(Fore.LIGHTRED_EX + '\tIs not accesible')
        if args.data:
            print('\t\t\t\t\t' + Advertisement.information +
                          '\n' + Fore.WHITE + result['data'])

        if args.save:
            with open(args.save, 'a+') as f:
                
                info = f"""
                LINK: https://{result['ip_str']}:{result['port']}

                IP: {result['ip_str']}
                PORT: {result['port']}
                OS: {result['os']}

                HOSTNAME: {result['hostnames']}
                DOMAINS: {result['domains']}

                Result: {count + 1} for your search {query}


                """
                f.write(info)

        count += 1

        print('\n\n')
        if count == args.lim:
            print(Fore.LIGHTCYAN_EX + '\tProcess finished')
            break
    except:
        pass

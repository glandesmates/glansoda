import os

os.system('pip3 install colorama')
os.system('pip3 install requests')
os.system('pip3 install argparse')
os.system('pip3 install shodan')
os.system('pip3 install python3-nmap')

def clear():
  os.system(['clear', 'cls'][os.name == 'nt'])

clear()

print("You can delete this file with security... ")

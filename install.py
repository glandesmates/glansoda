import os

os.system('pip3 install colorama')
os.system('python3 -m pip install requests')
os.system('pip3 install argparse')
os.system('python3 -m pip install shodan')
os.system('python3 -m pip python3-nmap')

def clear():
  os.system(['clear', 'cls'][os.name == 'nt'])

clear()

print("You can delete this file with security... ")

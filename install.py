import os

def install(module):
  os.system('pip3 install ' + module)

install('python3-nmap')
install('shodan')
install('requests')
install('argparse')
install('colorama')

def clear():
  os.system(['clear', 'cls'][os.name == 'nt'])

clear()

print("You can delete this file with security... ")

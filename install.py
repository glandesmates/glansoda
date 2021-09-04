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

print("To make this tool as command 'soda' enter your password")
os.system('sudo cp soda /usr/bin/')

print("Type 'soda' to use this tool in any path. (You can delete this file now)")

import os

print("To make this tool as command 'soda' enter your password")

def install(module):
  os.system('pip3 install ' + module)
  os.system('sudo pip3 install ' + module)

install('python3-nmap')
install('shodan')
install('requests')
install('argparse')
install('colorama')

def clear():
  os.system(['clear', 'cls'][os.name == 'nt'])

clear()

os.system('sudo cp soda /usr/bin/')
print("Type 'soda' to use this tool in any location. (You can delete 'install.py' file now)")

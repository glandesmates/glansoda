import os

c = input('Are you root [y/N] ')
if c == 'y':
  pass
else:
  print('You had to be root before instalation process')
  exit()

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
os.system('sudo chmod +x /usr/bin/soda')
print("Type 'soda' to use this tool in any location. (You can delete 'install.py' file now)")

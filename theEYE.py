import subprocess, os
from termcolor import colored as cl
from pyfiglet import figlet_format as ff
from simple_term_menu import TerminalMenu

subprocess.call('clear', shell=True)

tools_to_download = ['https://github.com/laramies/theHarvester.git', 'https://github.com/maldevel/EmailHarvester.git']

tools = ['theHarvester', 'EmailHarvester']

def check_tools():
    data = subprocess.check_output('ls'.split()).decode().split('\n')
    for i in range(len(tools)):
        if tools[i] not in data:
            cmd1 = f'git clone {tools_to_download[i]}'
            cmd2 = f'pip install -r {tools[i]}/requirements.txt'
            subprocess.call(cmd1, shell=True)
            subprocess.call(cmd2, shell=True)
            subprocess.call('clear', shell=True)

check_tools()

while True:
    print(cl('''
  █████    █████               ██████████ █████ █████ ██████████
 ░░███    ░░███               ░░███░░░░░█░░███ ░░███ ░░███░░░░░█
 ███████   ░███████    ██████  ░███  █ ░  ░░███ ███   ░███  █ ░ 
░░░███░    ░███░░███  ███░░███ ░██████     ░░█████    ░██████   
  ░███     ░███ ░███ ░███████  ░███░░█      ░░███     ░███░░█   
  ░███ ███ ░███ ░███ ░███░░░   ░███ ░   █    ░███     ░███ ░   █
  ░░█████  ████ █████░░██████  ██████████    █████    ██████████
   ░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░░░░░░    ░░░░░    ░░░░░░░░░░  
          '''
    , 'red'))

    options = ['[1] IP Information', '[2] Phonenumber Information', '[3] Domain harvester', '[4] Email Harvester', '[5] WHOIS', '[-] Quit']
    menu_highlight_style = ('standout', 'fg_gray', 'bold')
    terminal_menu = TerminalMenu(options, menu_highlight_style=menu_highlight_style)
    option_number = terminal_menu.show()

    if option_number == 0:
        subprocess.call('python ./ip_info.py', shell=True)
    elif option_number == 1:
        subprocess.call('python ./phonenumber_info/phonenumber_info.py', shell=True)
    elif option_number == 2:
        subprocess.call('python ./domain_harvester.py', shell=True)
    elif option_number == 3:
        subprocess.call('python ./mail_harvester.py', shell=True)
    elif option_number == 4:
        subprocess.call('python ./whois.py', shell=True)
    elif option_number == 5:
        break
    else:
        print(cl('Wrong option.', 'red'))
        subprocess.call('clear', shell=True)

    os.system('clear')

import requests, os
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

def is_public(ip):
    global data
    data = requests.get('http://ip-api.com/json/'+ip).json()
    try:
        if data['message'] == 'private range':
            return False
    except:
        return True

os.system('clear')

print(cl('='*30, 'red'))
print(cl(ff('IPInfo'), 'red'))
print(cl('\t-An IP info provider\n\t-AN AYLIT production', 'red'))
print(cl('='*30, 'red'))

ip = input(cl('Enter the IP address:', 'yellow'))
if is_public(ip):
    print(cl('-'*10+f'Data for {ip}'+'-'*10, 'blue'))
    print(cl(f"ISP: {data['isp']}", 'blue'))
    print(cl(f"ORG: {data['org']}", 'blue'))
    print(cl(f"Country: {data['country']}", 'blue'))
    print(cl(f"Country Code: {data['countryCode']}", 'blue'))
    print(cl(f"Region: {data['regionName']}", 'blue'))
    print(cl(f"City: {data['city']}", 'blue'))
    print(cl(f"Timezone: {data['timezone']}", 'blue'))

inp = input(cl('Press enter to exit', 'red'))
if inp == '':
    os.system('clear')
else:
    os.system('clear')

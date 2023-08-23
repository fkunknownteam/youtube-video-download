import requests
import time
import requests
import os
import time
import signal
import sys
import webbrowser

# text in horizontal centre

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)


# check internet connection 

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

if check_internet_connection():
   
   print()
else:
   print_centered("\033[1;31m Check your internet connection and try again.")
   sys.exit()
   
#open URL 
   
   url = "https://github.com/fkunknownteam"
flag_file = "url_opened_flag.txt"

if not os.path.exists(flag_file):
    webbrowser.open(url)
    with open(flag_file, "w") as f:
        f.write("URL opened")
else:
    print()
   
   
# loading animation 

os.system(" clear")
def load():

	def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
		percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
		if iteration == total:
			print()

	items = list(range(0, 30))
	l = len(items)

	loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
	for i, item in enumerate(items):
		time.sleep(0.08)
		loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
print()		
load()
os.system("clear")

#bannar

banner = """\033[1;96m_____       _                          _       
|  __ \     | |                       | |      
| |  \/ ___ | |_   _   _ __ ___   ___ | |_   _ 
| | __ / _ \| | | | | | '_ ` _ \ / _ \| | | | |
| |_\ \ (_) | | |_| | | | | | | | (_) | | |_| |
 \____/\___/|_|\__,_| |_| |_| |_|\___/|_|\__,_|
 
 ======================  By-Fk Unknwon Team  ======================
     
"""


 # User input
 
print()
print(banner) 
number = str(input("\033[1;96m\n\n\t[\033[1;31m+\033[1;96m] ENTER VICTIMS NUMBER : +88"))
message = str(input("\033[1;96m\n\n\t[\033[1;31m+\033[1;96m] ENTER MESSAGE :\033[1;31m "))
import requests
params = {
    'number' : number,
    'senderid': '8809601004489',
    'message': message,
}
 
 
 # check internet connection 

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

if check_internet_connection():
   
  print()
else:
   os.system(" clear")
   print_centered("\033[1;31m Check your internet connection and try again.")
   sys.exit()
   
 # Requests send to server
 
os.system(" clear")
response = requests.post('http://bulksmsbd.net/api/smsapi?api_key=UD89ozmAxaWYtp3xjlXR&type=text&number=$', params=params)

if response.status_code == 200:
  
  print("\033[1;32m \n\n\t[+] SMS SEND SUCCESSFUL ")
else:
  print("[-] UNABLE TO SEND SMS")
  
 
   
  #CLUOR

a="\033[1;30m" # Black
r="\033[1;31m" # Red
g="\033[1;32m" # Green
y="\033[1;33m" # Yellow
b="\033[1;34m" # Blue
p="\033[1;35m" # Purple
c="\033[1;36m" # Cyan
w="\033[1;37m" # White
bir="\033[1;31m"
bi="\033[0;34m"
bic="\033[0;36m"
r="\033[1;31m"
g="\033[1;32m"
n="\n"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
t="\t"
c1="\033[1;31m"
c2="\033[1;32m"
c3="\033[1;33m"
c4="\033[1;34m"
c5="\033[1;36m"
c6="\033[1;37m"

print("\n\n\t\tTHANKS FOR USING THIS TOOL ❤️")
input("\n\t\t\tEnter For Continue \>")
os.system("clear")
os.system("python custom_sms.py")

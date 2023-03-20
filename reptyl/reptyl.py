__name__='Reptyl'
__version__='2.0'
__author__='0ut0flin3'
__license__='Apache-2 License'
import os
import sys
import platform
import socket
import json

import requests


## TRY TO LOAD CONFIGURATION FILE AND EXIT IF ERROR
global config_json
if os.path.isfile("config.json")==False:
    print("Creating a new configuration file because one was not found...")
    
    js={"console_preferences":{"askconfirm":True, "use_python":False}}
    f=open("config.json","w")
    json.dump(js,f)
    f.close()
    
    if os.name=='nt':
       os.system('cls')
    if os.name=='posix':
       os.system('clear')
try:
    config_json=json.load(open("config.json"))
except Exception as ex:
    print(ex)
    sys.exit()
####################################################
global OS_LANG

global ASKCONFIRM;ASKCONFIRM=config_json["console_preferences"]["askconfirm"]
if os.name=='nt':
   if config_json["console_preferences"]["use_python"]==True:
      OS_LANG='Python'
   else:
      OS_LANG='powershell scripting language'
if os.name=='posix':
   if config_json["console_preferences"]["use_python"]==True:
      OS_LANG='Python'
   else:
      OS_LANG='bash'



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Device():
    info = {'USER':os.getlogin(),'WORKINGDIR':os.getcwd(),'PLATFORM':platform.uname()._asdict()}
class Network():
    name=socket.gethostname()
    host=socket.gethostbyname(name)
    
    def is_connected(name=name,host=host):
        return True if 0 == os.system(f'ping {host} -n 3 -l 32 -w 3 > clear') else False
global PRE
PRE=f'''
the info of my computer: {Device.info} 
the info of my network: {Network.name}, {Network.host},

if I ask you to do some actions on my computer, always reply with the {OS_LANG} code,only the {OS_LANG} code to use to do these actions.when the text must wrap use '\n', so as to always remain on one line.If I ask you a question don't do anything and say that you accept only orders and no questions. avoid printing description of the code but only print the code 
'''

class Gpt3():
    
    def __init__(self):
        pass
        

    
    def replyto(self, pr):
        try:
            session = requests.Session()
            payload = {"model": "text-davinci-003", "messages": [{"role": "system", "content": PRE},{"role": "user", "content": pr}]}
            r = requests.post("https://sharegpt.churchless.tech/share/v1/chat", headers = {'Content-Type': 'application/json'}, data= json.dumps(payload))
            answer = json.loads(r.text)["choices"][0]['message']['content']
            answer=answer.replace("```python","")
            answer=answer.replace("```","")
            return answer
        except Exception as ex:
            print(ex)


class Console():
      def execute(cmd):
        try:
            reply=gpt3.replyto(cmd)
            print(reply)
            exec(reply)
        except Exception as ex:
            print(ex)
      def clear(self):
        if os.name=='nt':
            os.system('cls')
        if os.name=='posix':
            os.system('clear')
      def __init__(self):
          self.clear()
          print(f'''{bcolors.BOLD}
|REPTYL v{__version__} [http://reptyl.org]|
|LICENSE: {__license__}|
|AUTHOR: {__author__}|
|PROJECT HOME: https://github.com/0ut0flin3/Reptyl|{bcolors.ENDC}\n
{bcolors.OKCYAN}Reptyl is released open-source and free. If you found this software useful please consider a donation {bcolors.ENDC}[{bcolors.HEADER} https://github.com/0ut0flin3/Reptyl/blob/main/README.md#donate{bcolors.ENDC} ] {bcolors.OKCYAN}You will help 0ut0flin3 improve this and other software. Thank you{bcolors.ENDC}\n\n''')
          while True:
                q=input(f'{bcolors.OKGREEN}{Device().info["USER"]}{bcolors.ENDC}{bcolors.BOLD}@{bcolors.ENDC}{bcolors.OKCYAN}REPTYL{bcolors.ENDC} $ ')       
                try:
                    gpt3=Gpt3()
                    reply=gpt3.replyto(q)
                    reply=f'''{reply}'''
                    if os.name=='posix':
                       if reply.startswith("$"):
                          reply=reply.replace("$","")
                        

                    kk=Gpt3().replyto("Say what the following code do in naturale language:\n"+reply)
                    
                    if ASKCONFIRM==True:
                        ask=input("Do you confirm to do the following stuff?\n\n"+bcolors.OKCYAN+kk+bcolors.ENDC+"\n"+reply+"\n\nC to abort, ENTER to continue:\n\n> ")
                        
                        if ask=="C" or ask=="c":

                            
                            pass
                            print("Aborted.")
                        else:
                            if OS_LANG=='bash':
                               os.system(reply)
                            if OS_LANG=='powershell scripting language':
                               PRE[f'''
the info of my computer: {Device.info} 
the info of my network: {Network.name}, {Network.host},

if I ask you to do some actions on my computer, always reply with the {OS_LANG} code to use to do these actions.when the text must wrap use '\n', so as to always remain on one line.If I ask you a question don't do anything and say that you accept only orders and no questions. Only if I'm on Windows do this: never include "powershell -Command" before the command and make sure you load the following assemblies at the top of the code (only if needed)''']=PRE.pop(list(PRE.keys())[0])
                               f=open('cmd.ps1','w')
                               f.write(reply)
                               f.close()
                               os.system("PowerShell -File cmd.ps1")
                            if OS_LANG=='Python':
                               exec(reply)
                    else:
                         if OS_LANG=='bash':
                            os.system(reply)
                         if OS_LANG=='powershell scripting language':
                            PRE[f'''
                            
the info of my computer: {Device.info} 
the info of my network: {Network.name}, {Network.host},

if I ask you to do some actions on my computer, always reply with the {OS_LANG} code to use to do these actions.when the text must wrap use '\n', so as to always remain on one line.If I ask you a question don't do anything and say that you accept only orders and no questions. Only if I'm on Windows do this: never include "powershell -Command" before the command and make sure you load the following assemblies at the top of the code (only if needed)''']=PRE.pop(list(PRE.keys())[0])
                            f=open('cmd.ps1','w')
                            f.write(reply)
                            f.close()
                            os.system("PowerShell -File cmd.ps1")
                         if OS_LANG=='Python':
                            exec(reply)
                    
                except Exception as ex:
                       print(ex)
Console()

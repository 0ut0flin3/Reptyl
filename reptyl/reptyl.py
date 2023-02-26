__name__='Reptyl'
__version__='0.0.0.1'
__author__='0ut0flin3'
__license__='Apache-2 L'
import os
import sys
import platform
import socket
import json
import openai


## TRY TO LOAD CONFIGURATION FILE AND EXIT IF ERROR
global config_json
if os.path.isfile("config.json")==False:
    print(f"Can't load configuration: config.json : file doesn't exists in current working direcory")
    sys.exit()
try:
    config_json=json.load(open("config.json"))
except Exception as ex:
    print(ex)
    sys.exit()
####################################################



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

PRE={f'''
the info of my computer: {Device.info} 
the info of my network: {Network.name}, {Network.host}
if I ask you to do some actions on my computer, always reply with the python code to use to do these actions.when the text must wrap use '\n', so as to always remain on one line.
''':"Ok, I will do"}

class Gpt3():
    
    def __init__(self, api_key=config_json["AI_settings"]["apikey"]):
        self.api_key=api_key
        
        try:
            openai.api_key=self.api_key
        except Exception as ex:
            print(ex)
    
    def replyto(self, pr,model=config_json["AI_settings"]["use_model"][config_json["AI_settings"]["use_model"].find(":")+1:]):
        try:
        
            response = openai.Completion.create(
            model=model,
            
            
            prompt="Human: "+list(PRE.keys())[0]+"\nAI:"+list(PRE.values())[0]+"\n"+"Human: "+pr+"\nAI:\n",
            temperature=1,
            max_tokens=3500,
            top_p=1,
            
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=[" Human:", " AI:"],
            
            )
            return response.choices[0].text
        except Exception as ex:
            print(ex)


class Console():
      def execute(cmd,use_AI=False):
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
          while True:
                q=input(f'{bcolors.OKGREEN}{Device().info["USER"]}{bcolors.ENDC}{bcolors.BOLD}@{bcolors.ENDC}{bcolors.OKCYAN}REPTYL{bcolors.ENDC} $ ')       
                try:
                    gpt3=Gpt3()
                    reply=gpt3.replyto(q)
                    reply=f'''{reply}'''
                    #rint(reply)
                    exec(reply)
                except Exception as ex:
                       print(ex)
Console()

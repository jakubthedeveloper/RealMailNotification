#!/usr/bin/python3

import getpass, imaplib
import string
import time
import serial
import argparse

# Allow access on https://myaccount.google.com/lesssecureapps

class App:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Application for checking and informing arduino if there are unread messages on imap mailbox.')
        parser.add_argument('--serial-port', default='/dev/ttyUSB0', help='Serial port for arduino communication')
        parser.add_argument('--imap-server', default='imap.gmail.com', help='Imap server hostname')
        parser.add_argument('--imap-user', default='/dev/ttyUSB0', help='Imap account name', required=True)
        args = parser.parse_args()

        self.mail = imaplib.IMAP4_SSL(args.imap_server)
        self.mail.login(args.imap_user, getpass.getpass())

        self.ser = serial.Serial(args.serial_port)

    def run(self):
        while True:
            self.mail.select("Inbox", True)
            status, response = self.mail.search(None, ('UNSEEN'))

            unreadNumber = len(response[0].split())
            gotMail = unreadNumber > 0

            print(unreadNumber, gotMail)
            self.ser.write(str('mail' if gotMail else 'nomail').encode())
            time.sleep(1)

app = App()
app.run()

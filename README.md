# Advanced-Python-Keylogger
  

This repository contains an advanced Python keylogger that captures various types of system information, including keystrokes, clipboard data, microphone audio, and screenshots. The captured data is then encrypted and sent to a specified email address.  

## Features  

- **Keystroke Logging**: Captures and logs all keystrokes made by the user.  
- **Clipboard Monitoring**: Logs the contents of the clipboard.  
- **Microphone Recording**: Records audio from the microphone for a specified duration.  
- **Screenshot Capture**: Takes screenshots of the user's screen.  
- **System Information Gathering**: Collects system information such as hostname, IP address, processor type, and more.  
- **Data Encryption**: Encrypts the captured data using Fernet symmetric encryption.  
- **Email Reporting**: Sends the captured and encrypted data to a specified email address.

 # Keylogger Prerequisites

Before running the keylogger, ensure you have the following Python libraries installed:

## Required Libraries

- `pynput` - To capture keyboard and mouse input.
- `pywin32` - Provides Windows API bindings.
- `Pillow` - For handling images and screenshots.
- `sounddevice` - To capture audio input.
- `scipy` - Used for processing audio data.
- `cryptography` - For encrypting logged data.
- `requests` - To send logged data to a remote server.

## Installation

Run the following command to install all required dependencies:

```bash
pip install pynput pywin32 Pillow sounddevice scipy cryptography requests


